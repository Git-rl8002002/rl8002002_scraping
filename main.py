#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20221229
# Update   : 20230307
# Function : scraping

import sys , pymysql , time , hashlib , logging , requests 
from bs4 import BeautifulSoup
from PyQt6 import QtCore, QtGui , QtWidgets , QtWebEngineWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCharts import *
import matplotlib.pyplot as plt

from control.config import *
from gui.ui_login import *
from gui.ui_main import *
from line_notify import *

########################################################################################################################
#
# main_content
#
########################################################################################################################
class main_content(QMainWindow):

    ########
    # log
    ########
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format , level=logging.INFO , datefmt="%H:%M:%S")

    #########
    #
    # init
    #
    #########
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Scraping()
        self.ui.setupUi(self)

        self.main_init()
    
    ##############
    #
    # main_init
    #
    ##############
    def main_init(self):
        
        #############
        # page_log
        #############
        self.ui.action_log.triggered.connect(self.load_page_log)
        self.ui.btn_et_news_chart.clicked.connect(lambda:self.show_chart('ET realtime news'))
        self.ui.btn_tech_news_chart.clicked.connect(lambda:self.show_chart('TECH news'))
        self.ui.btn_duck_film_chart.clicked.connect(lambda:self.show_chart('Duck film'))
        self.ui.btn_udn_news_chart.clicked.connect(lambda:self.show_chart('udn'))
        self.ui.btn_analysis_total.clicked.connect(self.show_analysis_chart)
        
        ##############
        # page_film
        ##############
        self.ui.action_film.triggered.connect(self.load_page_film)

        ##############
        # page_news
        ##############
        self.ui.action_news.triggered.connect(self.load_page_news)
        self.ui.btn_et_news_statistics.clicked.connect(lambda:self.show_news_statistics_chart('realtime'))
        self.ui.btn_tech_news_statistics.clicked.connect(lambda:self.show_news_statistics_chart('tech'))
        self.ui.btn_pc_diy_statistics.clicked.connect(lambda:self.show_news_statistics_chart('pcdiy'))
        self.ui.btn_udn_news_statistics.clicked.connect(lambda:self.show_news_statistics_chart('udn'))
        self.ui.btn_total_statistics.clicked.connect(self.show_news_total_statistics_chart)

        #########
        # work
        #########
        self.ui.action_work_record.triggered.connect(self.work_record)
        self.ui.action_work_calendar.triggered.connect(self.work_calendar)
        self.ui.btn_work_calendar_month_statistics.clicked.connect(self.work_calendar_by_month_statistics_chart)
        self.ui.btn_work_calendar_year_statistics.clicked.connect(self.work_calendar_by_year_statistics_chart)

        self.ui.action_line_notify.triggered.connect(self.line_notify)

        ##########
        # money
        ##########
        self.ui.action_money_record.triggered.connect(self.money_record)
        self.ui.btn_money_record_detail_list.clicked.connect(self.money_record_by_year_statistics)
        self.ui.btn_money_record_month_list.clicked.connect(self.money_record_by_month_statistics)
        self.ui.btn_money_record_day_list.clicked.connect(self.money_record_by_day_statistics)
        
        self.add_money_record_date()
        self.add_money_record_kind()
        self.ui.btn_money_record_submit.clicked.connect(self.submit_add_money_record)
        self.ui.btn_money_record_del.clicked.connect(self.add_money_record_del)

        ##############
        # page_DDos
        ##############
        self.ui.action_DDos.triggered.connect(self.page_DDos)

        ################
        # sell record
        ################
        self.ui.action_sell_record.triggered.connect(self.sell_record)
        
        self.add_sell_order_record_date()
        self.add_sell_order_record_kind()
        self.add_sell_trade_record_date()
        self.add_sell_trade_record_kind()
        
        self.ui.btn_sell_submit.clicked.connect(self.submit_add_sell_record)

        #########
        # file 
        #########
        self.ui.action_close.triggered.connect(self.scraping_close)

        ############
        # welcome
        ############
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_title)
    
    ###########################
    # submit_add_sell_record
    ###########################
    def submit_add_sell_record(self):
        
        order_date   = self.ui.sell_time.text()
        order_name   = self.ui.sell_name.text()
        order_phone  = self.ui.sell_phone.text()
        order_kind   = self.ui.sell_kind.text()
        order_amount = self.ui.sell_amount.text()
        order_price  = self.ui.sell_price.text()
        order_total_price = self.ui.sell_total_price.text()
        trade_date    = self.ui.sell_trade_time.text()
        trade_place   = self.ui.sell_trade_place.text()
        trade_comment = self.ui.sell_comment.toPlainText()

        ##########
        # check 
        ##########
        if len(order_name) < 1 :
            QMessageBox.information(self , 'Msg' , str('訂購姓名沒填 !'))
        elif len(order_phone) < 1 :
            QMessageBox.information(self , 'Msg' , str('訂購手機沒填 !'))
        elif len(order_kind) < 1 :
            QMessageBox.information(self , 'Msg' , str('訂購種類沒填 !'))
        elif len(order_amount) < 1 :
            QMessageBox.information(self , 'Msg' , str('訂購數量沒填 !'))
        elif len(order_price) < 1 :
            QMessageBox.information(self , 'Msg' , str('訂購單價沒填 !'))
        elif len(order_total_price) < 1 :
            QMessageBox.information(self , 'Msg' , str('訂購總價沒填 !'))
        elif len(trade_date) < 1 :
            QMessageBox.information(self , 'Msg' , str('面交日期沒填 !'))
        elif len(trade_place) < 1 :
            QMessageBox.information(self , 'Msg' , str('面交地點沒填 !'))

        ####################
        # add sell record
        ####################
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%m" , time.localtime())
        r_day   = time.strftime("%d" , time.localtime())  
        r_time  = time.strftime("%H:%M:%S" , time.localtime())
        
        conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
        curr = conn.cursor()
        
        try:
            sql = "insert into sell_record(name,phone,order_time,kind,amount,sell_price,total_price,trade_time,trade_place,comment,o_year,o_month,o_day) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')".format(order_name , order_phone , order_date , order_kind , order_amount , order_price , order_total_price , trade_date , trade_place , trade_comment , r_year , r_month , r_day)
            res = curr.execute(sql)

            if res:
                logging.info('add sell record successful.')
                QMessageBox.information(self , 'Msg' , '新增網購紀錄成功.')

                ### clear all item
                self.ui.sell_name.clear()
                self.ui.sell_phone.clear()
                self.ui.sell_kind.clear()
                self.ui.sell_amount.clear()
                self.ui.sell_price.clear()
                self.ui.sell_total_price.clear()
                self.ui.sell_trade_time.clear()
                self.ui.sell_trade_place.clear()
                self.ui.sell_comment.clear()

            else:
                logging.info('add sell record failed.')
                QMessageBox.information(self , 'Msg' , '新增網購紀錄失敗.')

        except Exception as e:
            logging.info('< Error > submit_add_sell_record : ' + str(e))
        finally:
            conn.commit()
            conn.close()

        ### reload sell record
        self.sell_record()

    ##############
    # page_DDos
    ##############
    def page_DDos(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_DDos)
        self.loading_ddos_statistics()

        self.ui.btn_ddos_analysis_submit.clicked.connect(self.analysis_ddos_address)
        self.ui.btn_refresh_ddos_statistics.clicked.connect(self.loading_ddos_statistics)
    
    ##########################
    # analysis_ddos_address
    ##########################
    def analysis_ddos_address(self):

        submit_val = self.ui.analysis_ddos_address.text()
        
        if len(submit_val) < 1:
            QMessageBox.information(self , 'Msg' , 'DDos解析內容，不能空白 !')
            logging.info('< Error > DDos解析內容，不能空白 !')
        else:
            data  = self.ui.analysis_ddos_address.text().split(']')
            
            ### attack ip
            data2 = data[3].split('->')
            a_ip  = data2[0][1:]

            ### attack time
            data3  = data[0].split('--')
            a_time = data3[0]

            ### attack_type
            data4  = data[4][1:]
            a_type = data4

            ### attack_format
            data5     = data[5][1:]
            a_package = data5
            
            ### check ip address
            check_ip = 'https://whatismyipaddress.com/ip/' + a_ip
            header = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                }

            data6 = requests.get(check_ip , headers=header)
            data6.encoding = data6.apparent_encoding
            #soup = BeautifulSoup(data6.text , 'html.parser')
            #content = soup.findAll('span')
            #r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            #for val in content:            
                #logging.info(val.string)

            self.ui.ddos_attack_ip_list.setHeaderLabels(['攻擊時間','攻擊種類','攻擊IP','封包'])
            self.ui.ddos_attack_ip_list.setColumnWidth(0 , 180)
            self.ui.ddos_attack_ip_list.setColumnWidth(1 , 80)
            self.ui.ddos_attack_ip_list.setColumnWidth(2 , 150)
            self.ui.ddos_attack_ip_list.setColumnWidth(3 , 300)
            
            root  = QTreeWidgetItem(self.ui.ddos_attack_ip_list)
            root.setText(0,str(a_time))
            root.setText(1,str(a_type))
            root.setText(2,str(a_ip))
            root.setText(3,str(a_package))

            logging.info(a_time + ' : ' + a_ip + ' , ' + a_type + ' , ' + a_package)

            conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db'],charset=tinfar_db['charset'])    
            curr = conn.cursor()

            ### analysis_ddos_address
            try:
                sql = "insert into network_attack(a_time , a_type , a_ip , a_package) values('{0}','{1}','{2}','{3}')".format(a_time , a_type , a_ip , a_package)
                res = curr.execute(sql)

                if res:
                    self.loading_ddos_statistics()
                    logging.info('save network attack data successful.')
                    QMessageBox.information(self , 'Msg' , 'save network attack data successful.')
                    self.ui.analysis_ddos_address.clear()

                else:
                    logging.info('save network attack data failed.')
                    QMessageBox.information(self , 'Msg' , 'save network attack data failed.')
                    self.ui.analysis_ddos_address.clear()

            except Exception as e:
                logging.info('< Error > analysis_ddos_address : ' + str(e))
            finally:
                conn.commit()
                conn.close()
            
            
            ### write network attack txt file
            try:
                ### record time
                r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                r_year  = time.strftime("%Y" , time.localtime())
                r_month = time.strftime("%Y-%m" , time.localtime())
                r_day   = time.strftime("%Y-%m-%d" , time.localtime())  

                if sys.platform == 'linux':
                    add = open(txt_path['network_attack_linux'] + r_month + '.txt','a')
                    add_content = str(a_time) + ' , ' + str(a_type) + ' , ' + str(a_ip) +  ' , '  + str(a_package) + '\n'
                    add.write(add_content)

                    logging.info('write network attack txt successful.')
                elif sys.platform == 'darwin':
                    add = open(txt_path['network_attack_mac'] + r_month + '.txt','a')
                    add_content = str(a_time) + ' , ' + str(a_type) + ' , ' + str(a_ip) +  ' , '  + str(a_package) + '\n'
                    add.write(add_content)

                    logging.info('write network attack txt successful.')
                
            except Exception as e:
                logging.info('< Error > write network attack txt : ' + str(e))
            finally:
                add.close()
    
    ############################
    # loading_ddos_statistics
    ############################
    def loading_ddos_statistics(self):        
        
        ### clear ddos_statistics_list
        self.ui.ddos_statistics_list.clear()
        
        ### loading DDos statistics
        conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db'],charset=tinfar_db['charset'])    
        curr = conn.cursor()
        try:
            sql = "select a_time , a_type , a_ip , a_package from network_attack order by a_time desc"    
            curr.execute(sql)
            res = curr.fetchall()

            for val in res:
                self.ui.ddos_statistics_list.setHeaderLabels(['攻擊時間','攻擊種類','攻擊IP','封包'])
                self.ui.ddos_statistics_list.setColumnWidth(0 , 180)
                self.ui.ddos_statistics_list.setColumnWidth(1 , 80)
                self.ui.ddos_statistics_list.setColumnWidth(2 , 150)
                self.ui.ddos_statistics_list.setColumnWidth(3 , 300)
            
                root  = QTreeWidgetItem(self.ui.ddos_statistics_list)
                root.setText(0,str(val[0]))
                root.setText(1,str(val[1]))
                root.setText(2,str(val[2]))
                root.setText(3,str(val[3]))

            logging.info('loading DDos statistics successful.')

        except Exception as e:
            logging.info('< Error > loading DDos statistics : ' + str(e))
        finally:
            conn.commit()
            conn.close()

    ##########################
    # add_money_record_del
    ##########################
    def add_money_record_del(self):

        self.ui.money_record_add_kind.clear()
        self.ui.money_record_add_money.clear()
        self.ui.money_record_add_content.clear()
    
    ###############################
    # add_sell_trade_record_date
    ###############################
    def add_sell_trade_record_date(self):
        
        self.ui.sell_trade_time_selected.setFixedWidth(230)
        self.ui.sell_trade_time_selected.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.ui.sell_trade_time_selected.setDateTime(QDateTime.currentDateTime())
        self.ui.sell_trade_time_selected.dateTimeChanged.connect(self.sell_trade_record_date_val)
    
    ###############################
    # sell_trade_record_date_val
    ###############################
    def sell_trade_record_date_val(self):
        date_val = self.ui.sell_trade_time_selected.text()
        self.ui.sell_trade_time.setText(date_val)
    
    ###############################
    # add_sell_order_record_date
    ###############################
    def add_sell_order_record_date(self):
        
        self.ui.sell_time_selected.setFixedWidth(230)
        self.ui.sell_time_selected.setDisplayFormat("yyyy-MM-dd")
        self.ui.sell_time_selected.setDate(QDate.currentDate())
        self.ui.sell_time_selected.dateChanged.connect(self.sell_order_record_date_val)

        r_day = time.strftime("%Y-%m-%d" , time.localtime())
        self.ui.sell_time.setText(r_day)
    
    ###############################
    # sell_order_record_date_val
    ###############################
    def sell_order_record_date_val(self):
        date_val = self.ui.sell_time_selected.text()
        self.ui.sell_time.setText(date_val)
    
    ##########################
    # add_money_record_date
    ##########################
    def add_money_record_date(self):
        
        self.ui.money_record_set_date.setFixedWidth(230)
        self.ui.money_record_set_date.setDisplayFormat("yyyy-MM-dd")
        self.ui.money_record_set_date.setDate(QDate.currentDate())
        self.ui.money_record_set_date.dateChanged.connect(self.money_record_date_val)

        r_day = time.strftime("%Y-%m-%d" , time.localtime())
        self.ui.money_record_add_date.setText(r_day)

    ##########################
    # money_record_date_val
    ##########################
    def money_record_date_val(self):
        date_val = self.ui.money_record_set_date.text()
        self.ui.money_record_add_date.setText(date_val)

    ###############################
    #
    # add_sell_trade_record_kind
    #
    ###############################
    def add_sell_trade_record_kind(self):
        
        conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
        curr = conn.cursor()

        try:
            sql = "select distinct trade_place from sell_record order by trade_place desc"
            curr.execute(sql)
            res = curr.fetchall()

            self.ui.sell_trade_place_selected.setFixedWidth(230)
            self.ui.sell_trade_place_selected.addItem("")

            for val in res:
                self.ui.sell_trade_place_selected.addItem(val[0])
            
            ### current index changed
            self.ui.sell_trade_place_selected.currentIndexChanged.connect(self.change_sell_trade_record_kind)
            
        except Exception as e:
            logging.info("< Error > add_sell_trade_record_kind : " + str(e))
        finally:
            conn.commit()
            conn.close()  

    ##################################
    #
    # change_sell_order_record_kind
    #
    ##################################
    def change_sell_trade_record_kind(self):
        kind_val = self.ui.sell_trade_place_selected.currentText()
        self.ui.sell_trade_place.setText(kind_val)
    
    ###############################
    #
    # add_sell_order_record_kind
    #
    ###############################
    def add_sell_order_record_kind(self):
        
        conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
        curr = conn.cursor()

        try:
            sql = "select distinct kind from sell_record order by kind desc"
            curr.execute(sql)
            res = curr.fetchall()

            self.ui.sell_kind_selected.setFixedWidth(230)
            self.ui.sell_kind_selected.addItem("")

            for val in res:
                self.ui.sell_kind_selected.addItem(val[0])
            
            ### current index changed
            self.ui.sell_kind_selected.currentIndexChanged.connect(self.change_sell_order_record_kind)
            
        except Exception as e:
            logging.info("< Error > add_sell_order_record_kind : " + str(e))
        finally:
            conn.commit()
            conn.close()  
              
    ##################################
    #
    # change_sell_order_record_kind
    #
    ##################################
    def change_sell_order_record_kind(self):
        kind_val = self.ui.sell_kind_selected.currentText()
        self.ui.sell_kind.setText(kind_val)
    
    ##########################
    #
    # add_money_record_kind
    #
    ##########################
    def add_money_record_kind(self):
        
        conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
        curr = conn.cursor()

        try:
            sql = "select distinct kind from money_record where account='rl8002002' order by kind desc"
            curr.execute(sql)
            res = curr.fetchall()

            self.ui.money_record_set_kind.setFixedWidth(230)
            self.ui.money_record_set_kind.addItem("")

            for val in res:
                self.ui.money_record_set_kind.addItem(val[0])
            
            ### current index changed
            self.ui.money_record_set_kind.currentIndexChanged.connect(self.change_money_record_kind)
            
        except Exception as e:
            logging.info("< Error > add_money_record_kind : " + str(e))
        finally:
            conn.commit()
            conn.close()    
    
    #############################
    #
    # change_money_record_kind
    #
    #############################
    def change_money_record_kind(self):
        kind_val = self.ui.money_record_set_kind.currentText()
        self.ui.money_record_add_kind.setText(kind_val)

    ############################
    #
    # submit_add_money_record
    #
    ############################
    def submit_add_money_record(self):
        
        ### variables
        date    = self.ui.money_record_add_date.text()
        kind    = self.ui.money_record_add_kind.text()
        money   = self.ui.money_record_add_money.text()
        content = self.ui.money_record_add_content.text()

        if len(kind) == 0:
            self.ui.money_record_add_kind.setStyleSheet('background-color:#cccccc')
            QMessageBox.information(self , 'Msg' , '種類不能空白')
            logging.info('種類不能空白')
        elif len(money) == 0:
            self.ui.money_record_add_money.setStyleSheet('background-color:#cccccc')
            QMessageBox.information(self , 'Msg' , '金額不能空白')
            logging.info('金額不能空白')
        elif len(content) == 0:
            self.ui.money_record_add_content.setStyleSheet('background-color:#cccccc')
            QMessageBox.information(self , 'Msg' , '內容不能空白')
            logging.info('內容不能空白')
        else:
            set_date = self.ui.money_record_set_date.text()

            ### record time
            r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            r_year  = time.strftime("%Y" , time.localtime())
            r_month = time.strftime("%Y-%m" , time.localtime())
            r_day   = time.strftime("%d" , time.localtime()) 
            
            conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
            curr = conn.cursor()

            try:
                sql = "insert into money_record(record_time , kind , money , content , record_year , record_month , record_day , status , account) value('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(date , kind , money , content , r_year , r_month , r_day , 'ok' , 'rl8002002')
                res = curr.execute(sql)

                if res:
                    QMessageBox.information(self , 'Msg' , str(kind) + " , 新增完成.")
                    logging.info(str(kind) + " , 新增完成.")

                    self.ui.money_record_add_kind.clear()
                    self.ui.money_record_add_money.clear()
                    self.ui.money_record_add_content.clear()

                else:
                    logging.info(str(kind) + " , 新增失敗.")
                
            except Exception as e:
                logging.info("< Error >  submit_add_money_record : " + str(e))
            finally:
                conn.commit()
                conn.close()
            
            ### reload money record
            self.money_record()

    
    ################
    #
    # line_notify
    #
    ################
    def line_notify(self):
        try:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_line_notify)
            
            #####################
            # line_notify_goods
            #####################
            self.ui.line_notify_goods.textChanged.connect(self.show_msg3)
            
            self.send_msg = item_fun()
            self.ui.btn_send_line_notify_3.clicked.connect(lambda:self.send_msg.line_notify_goods(self.ui.line_notify_goods.text()))

            #####################
            # line_notify_ming 
            #####################
            self.ui.line_notify_ming.textChanged.connect(self.show_msg2)
            
            self.send_msg = item_fun()
            self.ui.btn_send_line_notify_2.clicked.connect(lambda:self.send_msg.line_notify_ming(self.ui.line_notify_ming.text()))
            
            ################
            # line_notify 
            ################
            self.ui.line_notify.textChanged.connect(self.show_msg)
            
            self.send_msg = item_fun()
            self.ui.btn_send_line_notify.clicked.connect(lambda:self.send_msg.line_notify(self.ui.line_notify.text()))

        except Exception as e:
            QMessageBox.information(self , 'Msg' , str(e))
            logging.info(str(e))
        finally:
            pass

    def show_msg3(self):
        self.ui.line_notify_goods_msg.setText(self.ui.line_notify_goods.text())
    def show_msg2(self):
        self.ui.line_notify_ming_msg.setText(self.ui.line_notify_ming.text())
    def show_msg(self):
        self.ui.line_notify_msg.setText(self.ui.line_notify.text())

    ################
    #
    # sell_record
    #
    ################
    def sell_record(self):
        try:
            
            ################
            # select page
            ################
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_sell_record)
            
            self.ui.sell_record_mother_kind_list.setHeaderLabels(['面交時間','種類','姓名','手機','購買總數','總金額','面交地點'])
            self.ui.sell_record_mother_kind_list.setColumnWidth(0 , 150)
            self.ui.sell_record_mother_kind_list.setColumnWidth(1 , 50)
            self.ui.sell_record_mother_kind_list.setColumnWidth(2 , 150)
            self.ui.sell_record_mother_kind_list.setColumnWidth(3 , 180)
            self.ui.sell_record_mother_kind_list.setColumnWidth(4 , 80)
            self.ui.sell_record_mother_kind_list.setColumnWidth(5 , 80)
            self.ui.sell_record_mother_kind_list.setColumnWidth(6 , 100)
            
            ##########
            # clear
            ##########
            self.ui.sell_record_mother_list.clear()
            self.ui.sell_record_mother_year_list.clear()
            self.ui.sell_record_mother_month_list.clear()

            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()

            #################
            # sell_record
            #################
            self.sql = "select kind , count(*) from sell_record group by kind"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.sell_record_mother_list.setHeaderLabels(['種類','總購買次數'])
            self.ui.sell_record_mother_list.setColumnWidth(0 , 70)

            for val in self.res:
                
                self.root  = QTreeWidgetItem(self.ui.sell_record_mother_list)
                self.root.setText(0,str(val[0]))
                self.root.setText(1,str(val[1]))
            
            ### click tree list
            self.ui.sell_record_mother_list.doubleClicked.connect(self.sell_record_tree_list)
            
            ########################
            # sell_record_by_year
            ########################
            self.year_sql = "SELECT o_year  FROM `sell_record` group by o_year order by o_year desc"
            self.curr.execute(self.year_sql)
            self.year_res = self.curr.fetchall()
            
            self.ui.sell_record_mother_year_list.setHeaderLabels(['年','種類','購買次數'])
            self.ui.sell_record_mother_year_list.setColumnWidth(0 , 70)
            self.ui.sell_record_mother_year_list.setColumnWidth(1 , 50)

            for val in self.year_res:

                self.year_sql = "SELECT kind , count(*) FROM `sell_record` where o_year='{0}' group by kind".format(val[0])
                self.curr.execute(self.year_sql)
                self.res = self.curr.fetchall()
                
                self.root  = QTreeWidgetItem(self.ui.sell_record_mother_year_list)
                self.root.setText(0,str(val[0]))

                for val2 in self.res:

                    self.child = QTreeWidgetItem(self.ui.sell_record_mother_year_list)
                    self.child.setText(1 , str(val2[0]))
                    self.child.setText(2 , str(val2[1]))

            #########################
            # sell_record_by_month
            #########################
            self.year_sql = "SELECT o_year  FROM `sell_record` group by o_year order by o_year desc"
            self.curr.execute(self.year_sql)
            self.year_res = self.curr.fetchall()
            
            self.ui.sell_record_mother_month_list.setHeaderLabels(['年', '月' , '種類' , '購買次數' , '姓名' , '手機' , '購買總計 (斤)'])
            self.ui.sell_record_mother_month_list.setColumnWidth(0 , 70)
            self.ui.sell_record_mother_month_list.setColumnWidth(1 , 30)
            self.ui.sell_record_mother_month_list.setColumnWidth(2 , 50)
            self.ui.sell_record_mother_month_list.setColumnWidth(3 , 70)
            self.ui.sell_record_mother_month_list.setColumnWidth(4 , 180)
            self.ui.sell_record_mother_month_list.setColumnWidth(5 , 120)

            for year_val in self.year_res:

                self.month_sql = "SELECT o_month FROM `sell_record` where o_year='{0}' group by o_month order by o_month desc".format(year_val[0])
                self.curr.execute(self.month_sql)
                self.month_res = self.curr.fetchall()
                
                self.root  = QTreeWidgetItem(self.ui.sell_record_mother_month_list)
                self.root.setText(0,str(year_val[0]))

                for month_val in self.month_res:

                    self.kind_sql = "SELECT kind , count(*) FROM `sell_record` where o_year='{0}' and o_month='{1}' group by kind".format(year_val[0] , month_val[0])
                    self.curr.execute(self.kind_sql)
                    self.kind_res = self.curr.fetchall()

                    self.child = QTreeWidgetItem(self.ui.sell_record_mother_month_list)
                    self.child.setText(1 , str(month_val[0]))

                    for kind_val in self.kind_res:
                        
                        self.detail_sql = "SELECT name , phone , amount FROM `sell_record` where o_year='{0}' and o_month='{1}' and kind='{2}'".format(year_val[0] , month_val[0] , kind_val[0])
                        self.curr.execute(self.detail_sql)
                        self.detail_res = self.curr.fetchall()

                        self.child2 = QTreeWidgetItem(self.ui.sell_record_mother_month_list)
                        self.child2.setText(2 , str(kind_val[0]))
                        self.child2.setText(3 , str(kind_val[1]))

                        for detail_val in self.detail_res:
                            self.child3 = QTreeWidgetItem(self.ui.sell_record_mother_month_list)
                            self.child3.setText(4 , str(detail_val[0]))
                            self.child3.setText(5 , str(detail_val[1]))
                            self.child3.setText(6 , str(detail_val[2]))

            ### click tree list
            self.ui.sell_record_mother_month_list.doubleClicked.connect(self.sell_record_month_tree_list)

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > sell record : ' + str(e) )
            logging.info('< Error > sell record : ' + str(e) )
        finally:
            self.conn.commit()
            self.conn.close()
    
    ################################
    #
    # sell_record_month_tree_list
    #
    ################################
    def sell_record_month_tree_list(self):
        
        try:
            #############
            # variable
            #############
            self.item   = self.ui.sell_record_mother_month_list.currentItem()
            self.b_name   = self.item.text(4)
            self.b_phone  = self.item.text(5)

            ##########
            # clear 
            ##########
            self.ui.sell_record_mother_kind_list.clear()

            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()
            
            ####################################
            # sell_record_by_year_statistics
            ####################################
            self.sql = "select order_time , kind , name , phone , sell_price , total_price , trade_place  from sell_record where name='{0}' order by order_time desc".format(self.b_name)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()
            
            self.ui.sell_record_mother_kind_list.setHeaderLabels(['面交時間','種類','姓名','手機','購買總數','總金額','面交地點'])
            self.ui.sell_record_mother_kind_list.setColumnWidth(0 , 150)
            self.ui.sell_record_mother_kind_list.setColumnWidth(1 , 50)
            self.ui.sell_record_mother_kind_list.setColumnWidth(2 , 150)
            self.ui.sell_record_mother_kind_list.setColumnWidth(3 , 180)
            self.ui.sell_record_mother_kind_list.setColumnWidth(4 , 80)
            self.ui.sell_record_mother_kind_list.setColumnWidth(5 , 80)
            self.ui.sell_record_mother_kind_list.setColumnWidth(6 , 100)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.sell_record_mother_kind_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))
                self.root.setText(2 , str(val[2]))
                self.root.setText(3 , str(val[3]))
                self.root.setText(4 , str(val[4]))
                self.root.setText(5 , str(val[5]))
                self.root.setText(6 , str(val[6]))

                ### old show style - QListWidgets
                #self.ui.sell_record_mother_kind_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' , ' + str(val[2]) + ' , ' + str(val[3]) + ' , ' + str(val[4]) + ' , ' + str(val[5]) + ' , ' + str(val[6]))
        
        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > sell record tree list : ' + str(e) )
            logging.info('< Error > sell record tree list : ' + str(e) )
        finally:
            self.conn.commit()
            self.conn.close()

    ##########################
    #
    # sell_record_tree_list
    #
    ##########################
    def sell_record_tree_list(self):
        
        try:
            #############
            # variable
            #############
            self.item = self.ui.sell_record_mother_list.currentItem()
            self.kind = self.item.text(0)
            self.amount = self.item.text(1)

            ##########
            # clear 
            ##########
            self.ui.sell_record_mother_kind_list.clear()

            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()
            
            ####################################
            # sell_record_by_year_statistics
            ####################################
            self.sql = "select order_time , kind , name , phone , sell_price , total_price , trade_place  from sell_record where kind='{0}' order by order_time desc".format(self.kind)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.sell_record_mother_kind_list.setHeaderLabels(['面交時間','種類','姓名','手機','購買總數','總金額','面交地點'])
            self.ui.sell_record_mother_kind_list.setColumnWidth(0 , 150)
            self.ui.sell_record_mother_kind_list.setColumnWidth(1 , 50)
            self.ui.sell_record_mother_kind_list.setColumnWidth(2 , 150)
            self.ui.sell_record_mother_kind_list.setColumnWidth(3 , 180)
            self.ui.sell_record_mother_kind_list.setColumnWidth(4 , 80)
            self.ui.sell_record_mother_kind_list.setColumnWidth(5 , 80)
            self.ui.sell_record_mother_kind_list.setColumnWidth(6 , 100)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.sell_record_mother_kind_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))
                self.root.setText(2 , str(val[2]))
                self.root.setText(3 , str(val[3]))
                self.root.setText(4 , str(val[4]))
                self.root.setText(5 , str(val[5]))
                self.root.setText(6 , str(val[6]))
                
                ### old show style - QListWidgets
                #self.ui.sell_record_mother_kind_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' , ' + str(val[2]) + ' , ' + str(val[3]) + ' , ' + str(val[4]) + ' , ' + str(val[5]) + ' , ' + str(val[6]))
        
        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > sell record tree list : ' + str(e) )
            logging.info('< Error > sell record tree list : ' + str(e) )
        finally:
            self.conn.commit()
            self.conn.close()
    
    ##########
    #
    # close
    #
    ##########
    def scraping_close(self):
        QApplication.closeAllWindows()

    ####################################
    #
    # money_record_by_kind_statistics
    #
    ####################################
    def money_record_by_kind_statistics(self):
        try:
            #############
            # variable
            #############
            self.data  = self.ui.money_record_kind_list.currentItem()
            self.kind  = self.data.text(0)

            ##########
            # clear 
            ##########
            self.ui.money_record_detail_list.clear()

            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()
            
            ####################################
            # money_record_by_year_statistics
            ####################################
            self.sql = "select record_time , money , content from money_record where account='rl8002002' and kind='{0}' and status='ok' order by record_time desc".format(self.kind)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.money_record_detail_list.setHeaderLabels(['最後記錄','總金額','帳務內容'])
            self.ui.money_record_detail_list.setColumnWidth(0 , 150)

            ##################
            # data to chart
            ##################
            self.charts     = QChart()
            self.charts.setTitle(self.kind)
            self.charts.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
            self.chart_view = QChartView(self.charts)
            self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

            ### line 1
            self.series0       = QLineSeries()
            self.series0.setPen(QPen(QColor('skyblue') , 3))
            self.series1       = QScatterSeries()
            self.series1.setColor(QColor('skyblue'))
            self.series1.setPen(QPen(QColor('skyblue') , 1))

            for val in self.res:

                ### chart para
                self.series0.setName('帳務記錄 種類 統計')
                self.series1.setName('目前(總數)')
                self.date_fmt = "yyyy-MM-dd"
                self.time = str(val[0]).strip()
                self.x = QDateTime().fromString(self.time , self.date_fmt).toMSecsSinceEpoch()
                self.y = int(val[1])
                self.series0.append(self.x , self.y)
                self.series1.append(self.x , self.y)
                self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_value_by_day)

                self.root = QTreeWidgetItem(self.ui.money_record_detail_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]) + ' 元')
                self.root.setText(2 , str(val[2]))

                ### detail by kind , old show style - QListWidgets 
                #self.ui.money_record_detail_list.addItem(str(val[0]) + ' , ( ' + str(val[1]) + ' 元 ) , ' + str(val[2]))
            
            ### line 1
            self.charts.addSeries(self.series0)
            self.charts.addSeries(self.series1)

            ### TEMP X-axis
            self.axis_x = QDateTimeAxis()
            self.axis_x.setTickCount(20)
            self.axis_x.setFormat("yyyy-MM-dd")
            self.axis_x.setTitleText("時間")
            self.charts.addAxis(self.axis_x , Qt.AlignmentFlag.AlignBottom)
            self.series0.attachAxis(self.axis_x)
            
            ### TEMP Y-axis
            self.axis_y = QValueAxis()
            self.axis_y.setTickCount(20)
            self.axis_y.setLabelFormat("%i")
            self.axis_y.setTitleText("數值")
            self.charts.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
            self.series0.attachAxis(self.axis_y)

            ### chart 
            self.chart1 = QWidget()
            self.sub1   = QHBoxLayout()
            self.sub1.addWidget(self.chart_view)
            self.chart1.setLayout(self.sub1)
            self.chart1.resize(800,600)
            self.chart1.show()
            
        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > money record detail by kind statistics : ' + str(e) )
            logging.info('< Error > money record detail by kind statistics : ' + str(e) )
        finally:
            self.conn.commit()
            self.conn.close()

    ###################################
    #
    # money_record_by_day_statistics
    #
    ###################################
    def money_record_by_day_statistics(self):
        try:
            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()
            
            ####################################
            # money_record_by_year_statistics
            ####################################
            self.sql = "select record_time , count(*) from money_record where account='rl8002002' group by record_time order by record_time desc"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            ##################
            # data to chart
            ##################
            self.charts     = QChart()
            self.charts.setTitle('Total money year Statistics')
            self.charts.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
            self.chart_view = QChartView(self.charts)
            self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

            ### line 1
            self.series0       = QLineSeries()
            self.series0.setPen(QPen(QColor('skyblue') , 3))
            self.series1       = QScatterSeries()
            self.series1.setColor(QColor('skyblue'))
            self.series1.setPen(QPen(QColor('skyblue') , 1))

            for val in self.res:
                
                self.sql2 = "select sum(money) from money_record where account='rl8002002' and record_time='{0}'".format(val[0])
                self.curr.execute(self.sql2)
                self.res2 = self.curr.fetchone()
                
                ### chart para
                self.series0.setName('帳務記錄 日 統計')
                self.series1.setName('目前(總數)')
                self.date_fmt = "yyyy-MM-dd"
                self.time = str(val[0]).strip()
                self.x = QDateTime().fromString(self.time , self.date_fmt).toMSecsSinceEpoch()
                self.y = int(self.res2[0])
                self.series0.append(self.x , self.y)
                self.series1.append(self.x , self.y)
                self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_value_by_day)
            
            ### line 1
            self.charts.addSeries(self.series0)
            self.charts.addSeries(self.series1)

            ### TEMP X-axis
            self.axis_x = QDateTimeAxis()
            self.axis_x.setTickCount(20)
            self.axis_x.setFormat("yyyy-MM-dd")
            self.axis_x.setTitleText("時間")
            self.charts.addAxis(self.axis_x , Qt.AlignmentFlag.AlignBottom)
            self.series0.attachAxis(self.axis_x)
            
            ### TEMP Y-axis
            self.axis_y = QValueAxis()
            self.axis_y.setTickCount(20)
            self.axis_y.setLabelFormat("%i")
            self.axis_y.setTitleText("數值")
            self.charts.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
            self.series0.attachAxis(self.axis_y)

            ### chart 
            self.chart1 = QWidget()
            self.sub1   = QHBoxLayout()
            self.sub1.addWidget(self.chart_view)
            self.chart1.setLayout(self.sub1)
            self.chart1.resize(800,600)
            self.chart1.show()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > money record by month statistics : ' + str(e) )
            logging.info('< Error > money record by month statistics : ' + str(e) )
        finally:
            self.conn.commit()
            self.conn.close()
    
    #####################################
    #
    # money_record_by_month_statistics
    #
    #####################################
    def money_record_by_month_statistics(self):
        try:
            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()
            
            ####################################
            # money_record_by_year_statistics
            ####################################
            self.sql = "select record_month , count(*) from money_record where account='rl8002002' group by record_month order by record_month desc"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            ##################
            # data to chart
            ##################
            self.charts     = QChart()
            self.charts.setTitle('Total money year Statistics')
            self.charts.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
            self.chart_view = QChartView(self.charts)
            self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

            ### line 1
            self.series0       = QLineSeries()
            self.series0.setPen(QPen(QColor('skyblue') , 3))
            self.series1       = QScatterSeries()
            self.series1.setColor(QColor('skyblue'))
            self.series1.setPen(QPen(QColor('skyblue') , 1))

            for val in self.res:
                
                self.sql2 = "select sum(money) from money_record where account='rl8002002' and record_month='{0}'".format(val[0])
                self.curr.execute(self.sql2)
                self.res2 = self.curr.fetchone()
                
                ### chart para
                self.series0.setName('帳務記錄 月 統計')
                self.series1.setName('目前(總數)')
                self.date_fmt = "yyyy-MM"
                self.x = QDateTime().fromString(val[0] , self.date_fmt).toMSecsSinceEpoch()
                self.y = int(self.res2[0])
                self.series0.append(self.x , self.y)
                self.series1.append(self.x , self.y)
                self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_value_by_month)
            
            ### line 1
            self.charts.addSeries(self.series0)
            self.charts.addSeries(self.series1)

            ### TEMP X-axis
            self.axis_x = QDateTimeAxis()
            self.axis_x.setTickCount(20)
            self.axis_x.setFormat("yyyy-MM")
            self.axis_x.setTitleText("時間")
            self.charts.addAxis(self.axis_x , Qt.AlignmentFlag.AlignBottom)
            self.series0.attachAxis(self.axis_x)
            
            ### TEMP Y-axis
            self.axis_y = QValueAxis()
            self.axis_y.setTickCount(20)
            self.axis_y.setLabelFormat("%i")
            self.axis_y.setTitleText("數值")
            self.charts.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
            self.series0.attachAxis(self.axis_y)

            ### chart 
            self.chart1 = QWidget()
            self.sub1   = QHBoxLayout()
            self.sub1.addWidget(self.chart_view)
            self.chart1.setLayout(self.sub1)
            self.chart1.resize(800,600)
            self.chart1.show()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > money record by month statistics : ' + str(e) )
            logging.info('< Error > money record by month statistics : ' + str(e) )
        finally:
            self.conn.commit()
            self.conn.close()

    ####################################
    #
    # money_record_by_year_statistics
    #
    ####################################
    def money_record_by_year_statistics(self):
        try:
            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()
            
            ####################################
            # money_record_by_year_statistics
            ####################################
            self.sql = "select record_year , count(*) from money_record where account='rl8002002' group by record_year order by record_year desc"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            ##################
            # data to chart
            ##################
            self.charts     = QChart()
            self.charts.setTitle('Total money year Statistics')
            self.charts.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
            self.chart_view = QChartView(self.charts)
            self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

            ### line 1
            self.series0       = QLineSeries()
            self.series0.setPen(QPen(QColor('skyblue') , 3))
            self.series1       = QScatterSeries()
            self.series1.setColor(QColor('skyblue'))
            self.series1.setPen(QPen(QColor('skyblue') , 1))

            for val in self.res:
                
                self.sql2 = "select sum(money) from money_record where account='rl8002002' and record_year='{0}'".format(val[0])
                self.curr.execute(self.sql2)
                self.res2 = self.curr.fetchone()
                
                ### chart para
                self.series0.setName('帳務記錄 年 統計')
                self.series1.setName('目前(總數)')
                self.date_fmt = "yyyy"
                self.x = QDateTime().fromString(val[0] , self.date_fmt).toMSecsSinceEpoch()
                self.y = int(self.res2[0])
                self.series0.append(self.x , self.y)
                self.series1.append(self.x , self.y)
                self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_value_by_year)
            
            ### line 1
            self.charts.addSeries(self.series0)
            self.charts.addSeries(self.series1)

            ### TEMP X-axis
            self.axis_x = QDateTimeAxis()
            self.axis_x.setTickCount(20)
            self.axis_x.setFormat("yyyy")
            self.axis_x.setTitleText("時間")
            self.charts.addAxis(self.axis_x , Qt.AlignmentFlag.AlignBottom)
            self.series0.attachAxis(self.axis_x)
            
            ### TEMP Y-axis
            self.axis_y = QValueAxis()
            self.axis_y.setTickCount(20)
            self.axis_y.setLabelFormat("%i")
            self.axis_y.setTitleText("數值")
            self.charts.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
            self.series0.attachAxis(self.axis_y)

            ### chart 
            self.chart1 = QWidget()
            self.sub1   = QHBoxLayout()
            self.sub1.addWidget(self.chart_view)
            self.chart1.setLayout(self.sub1)
            self.chart1.resize(800,600)
            self.chart1.show()

        except Exception as e:
            QMessageBox.sinformation(self , 'Msg' , '< Error > money record statistics : ' + str(e) )
            logging.info(self , 'Msg' , '< Error > money record statistics : ' + str(e) )
        finally:
            self.conn.commit()
            self.conn.close()
    
    ###########################################
    #
    # work_calendar_by_year_statistics_chart
    #
    ###########################################
    def work_calendar_by_year_statistics_chart(self):
        try:
            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()
            
            #######################
            # work_calendar_year
            #######################
            self.sql = "select record_year , count(*) from calendar_content where account='rl8002002' group by record_year order by record_year desc"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            ##################
            # data to chart
            ##################
            self.charts     = QChart()
            self.charts.setTitle('Total news Statistics')
            self.charts.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
            self.chart_view = QChartView(self.charts)
            self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

            ### line 1
            self.series0       = QLineSeries()
            self.series0.setPen(QPen(QColor('skyblue') , 3))
            self.series1       = QScatterSeries()
            self.series1.setColor(QColor('skyblue'))
            self.series1.setPen(QPen(QColor('skyblue') , 1))

            for val in self.res:
                ### chart para
                self.series0.setName('工作日誌 年 統計')
                self.series1.setName('目前(總數)')
                self.date_fmt = "yyyy"
                self.x = QDateTime().fromString(str(val[0]) , self.date_fmt).toMSecsSinceEpoch()
                self.y = int(val[1])
                self.series0.append(self.x , self.y)
                self.series1.append(self.x , self.y)
                self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_value_by_year)

                self.ui.work_calendar_year_list.addItem(str(val[0]) + ' , ( ' + str(val[1]) + ' )')
            
            ### line 1
            self.charts.addSeries(self.series0)
            self.charts.addSeries(self.series1)

            ### TEMP X-axis
            self.axis_x = QDateTimeAxis()
            self.axis_x.setTickCount(20)
            self.axis_x.setFormat("yyyy")
            self.axis_x.setTitleText("時間")
            self.charts.addAxis(self.axis_x , Qt.AlignmentFlag.AlignBottom)
            self.series0.attachAxis(self.axis_x)
            
            ### TEMP Y-axis
            self.axis_y = QValueAxis()
            self.axis_y.setTickCount(20)
            self.axis_y.setLabelFormat("%i")
            self.axis_y.setTitleText("數值")
            self.charts.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
            self.series0.attachAxis(self.axis_y)

            ### chart 
            self.chart = QWidget()
            self.sub   = QHBoxLayout()
            self.sub.addWidget(self.chart_view)
            self.chart.setLayout(self.sub)
            self.chart.resize(800,600)
            self.chart.show()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > work_calendar_by_year_statistics : ' + str(e) )
            logging.info('< Error > work_calendar_by_year_statistics : ' + str(e) )
        finally:
            self.conn.commit()
            self.conn.close()
    
    ############################################
    #
    # work_calendar_by_month_statistics_chart
    #
    ############################################
    def work_calendar_by_month_statistics_chart(self):
        try:
            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()
            
            ########################
            # work_calendar_month
            ########################
            self.sql = "select record_month , count(*) from calendar_content where account='rl8002002' group by record_month order by record_month desc"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            ##################
            # data to chart
            ##################
            self.charts     = QChart()
            self.charts.setTitle('Total news Statistics')
            self.charts.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
            self.chart_view = QChartView(self.charts)
            self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

            ### line 1
            self.series0       = QLineSeries()
            self.series0.setPen(QPen(QColor('skyblue') , 3))
            self.series1       = QScatterSeries()
            self.series1.setColor(QColor('skyblue'))
            self.series1.setPen(QPen(QColor('skyblue') , 1))

            for val in self.res:
                ### chart para
                self.series0.setName('工作日誌 月 統計')
                self.series1.setName('目前(總數)')
                self.date_fmt = "yyyy-MM"
                self.x = QDateTime().fromString(val[0] , self.date_fmt).toMSecsSinceEpoch()
                self.y = int(val[1])
                self.series0.append(self.x , self.y)
                self.series1.append(self.x , self.y)
                self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_value_by_month)

                self.ui.work_calendar_month_list.addItem(str(val[0]) + ' , ( ' + str(val[1]) + ' )')
            
            ### line 1
            self.charts.addSeries(self.series0)
            self.charts.addSeries(self.series1)

            ### TEMP X-axis
            self.axis_x = QDateTimeAxis()
            self.axis_x.setTickCount(20)
            self.axis_x.setFormat("yyyy-MM")
            self.axis_x.setTitleText("時間")
            self.charts.addAxis(self.axis_x , Qt.AlignmentFlag.AlignBottom)
            self.series0.attachAxis(self.axis_x)
            
            ### TEMP Y-axis
            self.axis_y = QValueAxis()
            self.axis_y.setTickCount(20)
            self.axis_y.setLabelFormat("%i")
            self.axis_y.setTitleText("數值")
            self.charts.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
            self.series0.attachAxis(self.axis_y)

            ### chart 
            self.chart = QWidget()
            self.sub   = QHBoxLayout()
            self.sub.addWidget(self.chart_view)
            self.chart.setLayout(self.sub)
            self.chart.resize(800,600)
            self.chart.show()

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > work_calendar_by_month_statistics : ' + str(e) )
            logging.info('< Error > work_calendar_by_month_statistics : ' + str(e) )
        finally:
            self.conn.commit()
            self.conn.close()
    
    ##################
    #
    # work_calendar
    #
    ##################
    def work_calendar(self):
        try:
            
            ################
            # select page
            ################
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_work_calendar)

            ##########
            # clear
            ##########
            self.ui.work_calendar_year_list.clear()
            self.ui.work_calendar_month_list.clear()

            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()

            ##################
            # work_calendar
            ##################
            self.sql = "select date , title , line_record from calendar_content where account='rl8002002' and status='enable' order by date desc"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.work_calendar_list.setHeaderLabels(['最後記錄','標題'])
            self.ui.work_calendar_list.setColumnWidth(0 , 120)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.work_calendar_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))

                ### old show style - QListWidgets
                #self.ui.work_calendar_list.addItem(str(val[0]) + ' , ' + str(val[1]))
            
            #######################
            # work_calendar_year
            #######################
            self.sql = "select record_year , count(*) from calendar_content where account='rl8002002' group by record_year order by record_year desc"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.work_calendar_year_list.setHeaderLabels(['年 統計','總筆數'])

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.work_calendar_year_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))

                ### old show style - QListWidgets
                #self.ui.work_calendar_year_list.addItem(str(val[0]) + ' , ( ' + str(val[1]) + ' )')
            
            ########################
            # work_calendar_month
            ########################
            self.sql = "select record_month , count(*) from calendar_content where account='rl8002002' group by record_month order by record_month desc"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.work_calendar_month_list.setHeaderLabels(['月 統計','總筆數'])

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.work_calendar_month_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))

                ### old show style - QListWidgets
                #self.ui.work_calendar_month_list.addItem(str(val[0]) + ' , ( ' + str(val[1]) + ' )')
            

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > work_calendar : ' + str(e) )
            logging.info('< Error > work_calendar : ' + str(e) )
        finally:
            self.conn.commit()
            self.conn.close()

   
    #################
    #
    # money_record
    #
    #################
    def money_record(self):
        try:
            
            ################
            # select page
            ################
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_money_record)

            self.ui.money_record_detail_list.setHeaderLabels(['最後記錄','總金額','帳務內容'])
            self.ui.money_record_detail_list.setColumnWidth(0 , 150)
            
            ##########
            # clear
            ##########
            self.ui.money_record_list.clear()
            self.ui.money_record_kind_list.clear()
            self.ui.money_record_year_statistics_list.clear()
            self.ui.money_record_month_statistics_list.clear()
            self.ui.money_record_day_statistics_list.clear()

            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()

            #################
            # money_record
            #################
            self.sql = "select record_time , money , content from money_record where account='rl8002002' and status='ok' order by record_time desc"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.money_record_list.setHeaderLabels(['最後記錄','總金額','帳務內容'])
            self.ui.money_record_list.setColumnWidth(0 , 150)
            self.ui.money_record_list.setColumnWidth(1 , 80)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.money_record_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]) + ' 元')
                self.root.setText(2 , str(val[2]))

                ### old show style - QListWidgets
                #self.ui.money_record_list.addItem(str(val[0]) + ' , ' + str(val[2]) + ' , ( ' + str(val[1]) + ' 元 )')
            
            ######################
            # money_record_kind
            ######################
            self.sql = "select kind , count(*) from money_record where account='rl8002002' group by kind"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.money_record_kind_list.setHeaderLabels(['種類','總筆數','總金額'])
            self.ui.money_record_kind_list.setColumnWidth(0 , 150)

            for val in self.res:
                self.sql2 = "select sum(money) from money_record where kind='{0}' and account='rl8002002'".format(val[0])
                self.curr.execute(self.sql2)
                self.res2 = self.curr.fetchall()
                
                for val2 in self.res2:
                    self.root = QTreeWidgetItem(self.ui.money_record_kind_list)
                    self.root.setText(0 , str(val[0]))
                    self.root.setText(1 , str(val[1]))
                    self.root.setText(2 , str(val2[0]) + ' 元')

                    ### old show style - QListWidgets
                    #self.ui.money_record_kind_list.addItem(str(val[0]) + ' , ( ' + str(val[1]) + ' ) , ' + str(val2[0]) + ' 元')
            
            ### select money record kind 
            self.ui.money_record_kind_list.doubleClicked.connect(self.money_record_by_kind_statistics)
            
            ####################################
            # money_record_by_year_statistics
            ####################################
            self.sql = "select record_year , count(*) from money_record where account='rl8002002' group by record_year order by record_year desc"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.money_record_year_statistics_list.setHeaderLabels(['年 統計','總筆數','總金額'])
            self.ui.money_record_year_statistics_list.setColumnWidth(0 , 100)

            for val in self.res:
                
                self.sql2 = "select sum(money) from money_record where account='rl8002002' and record_year='{0}'".format(val[0])
                self.curr.execute(self.sql2)
                self.res2 = self.curr.fetchone()

                self.root = QTreeWidgetItem(self.ui.money_record_year_statistics_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))
                self.root.setText(2 , str(self.res2[0]) + '  元')

                ### old show style - QListWidgets
                #self.ui.money_record_year_statistics_list.addItem(str(val[0]) + ' , ( ' + str(val[1]) + ' ) , 共 ' + str(self.res2[0]) + ' 元')
            
            #####################################
            # money_record_by_month_statistics
            #####################################
            self.sql = "select record_month , count(*) from money_record where account='rl8002002' group by record_month order by record_month desc"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.money_record_month_statistics_list.setHeaderLabels(['月 統計','總筆數','總金額'])
            self.ui.money_record_month_statistics_list.setColumnWidth(0 , 100)

            for val in self.res:
                
                self.sql2 = "select sum(money) from money_record where account='rl8002002' and record_month='{0}'".format(val[0])
                self.curr.execute(self.sql2)
                self.res2 = self.curr.fetchone()

                self.root = QTreeWidgetItem(self.ui.money_record_month_statistics_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))
                self.root.setText(2 , str(self.res2[0]) + ' 元')

                ### old show style - QListWidgets
                #self.ui.money_record_month_statistics_list.addItem(str(val[0]) + ' , ( ' + str(val[1]) + ' ) , 共 ' + str(self.res2[0]) + ' 元')
            
            ###################################
            # money_record_by_day_statistics
            ###################################
            self.sql = "select record_time , count(*) from money_record where account='rl8002002' group by record_time order by record_time desc"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.money_record_day_statistics_list.setHeaderLabels(['日 統計','總筆數','總金額'])
            self.ui.money_record_day_statistics_list.setColumnWidth(0 , 150)

            for val in self.res:
                
                self.sql2 = "select sum(money) from money_record where account='rl8002002' and record_time='{0}'".format(val[0])
                self.curr.execute(self.sql2)
                self.res2 = self.curr.fetchone()

                self.root = QTreeWidgetItem(self.ui.money_record_day_statistics_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))
                self.root.setText(2 , str(self.res2[0]) + ' 元')

                ### old show style - QListWidgets
                #self.ui.money_record_day_statistics_list.addItem(str(val[0]) + ' , ( ' + str(val[1]) + ' ) , 共 ' + str(self.res2[0]) + ' 元')

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > money_page : ' + str(e) )
            logging.info('< Error > money_page : ' + str(e) )
        finally:
            self.conn.commit()
            self.conn.close()
    
    ################
    #
    # work_record
    #
    ################
    def work_record(self):
        try:
            
            ################
            # select page
            ################
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_work_record)

            #self.ui.line_notify.setFixedHeight()
            
            ##########
            # clear
            ##########
            self.ui.work_record_tb_list.clear()
            self.ui.work_record_kind_list.clear()

            #self.ui.work_record_tb_list.setColumnCount(2)
            #self.ui.work_record_tb_list.setHorizontalHeaderLabels(['record time','kind','amount'])

            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db2'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()

            ################
            # work_record
            ################
            self.sql = "select date , title , line_record from work_record where account='rl8002002' and status='enable' order by date desc"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.work_record_tb_list.setHeaderLabels(['最後記錄','標題'])
            self.ui.work_record_tb_list.setColumnWidth(0,120)

            for val in self.res:

                self.root = QTreeWidgetItem(self.ui.work_record_tb_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))

                ### old show style - QListWidgets
                #self.ui.work_record_tb_list.addItem(str(val[0]) + ' , ' + str(val[1]))
            
            #####################
            # work_record_kind
            #####################
            self.sql = "select kind , count(*) from work_record where account='rl8002002' group by kind"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.work_record_kind_list.setHeaderLabels(['種類','總筆數','最後記錄'])
            self.ui.work_record_kind_list.setColumnWidth(0,160)
            self.ui.work_record_kind_list.setColumnWidth(1,70)

            for val in self.res:
                self.sql2 = "select date from work_record where kind='{0}' and status='enable' and account='rl8002002' order by date desc limit 0,1".format(val[0])
                self.curr.execute(self.sql2)
                self.res2 = self.curr.fetchall()

                for val2 in self.res2:
                    self.root = QTreeWidgetItem(self.ui.work_record_kind_list)
                    self.root.setText(0 , str(val[0]))
                    self.root.setText(1 , str(val[1]))
                    self.root.setText(2 , str(val2[0]))

                    ### old show style - QListWidgets
                    #self.ui.work_record_kind_list.addItem(str(val[0]) + ' , ' + str(val2[0]) + ' ( ' + str(val[1]) + ' )')

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > work_page : ' + str(e) )
            logging.info('< Error > work_page : ' + str(e) )
        finally:
            self.conn.commit()
            self.conn.close()
        

    ########################
    #
    # show_analysis_chart
    #
    ########################
    def show_analysis_chart(self):

        #############
        # variable
        #############
        self.kind = 'log analysis'

        try:
            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()

            ###############
            # log record
            ###############
            self.sql = "select  kind , count(*) from scraping_log group by kind"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()
            
            self.kind = []
            self.amount = []

            for val in self.res:
                self.kind.append(str(val[0]))
                self.amount.append(str(val[1]))


            #####################
            # matplotlib chart
            #####################
            fig , ax = plt.subplots()
                
            bar_labels = ['red'    , 'blue'    , '_red'   , 'orange'     , 'pink'     , 'green'     , 'gray'     , 'green'     ]
            bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange' , 'tab:pink' , 'tab:green' , 'tab:gray' , 'tab:green' ]

            ax.bar(self.kind , self.amount , label=bar_labels, color=bar_colors)

            ax.set_ylabel('Value')
            ax.set_title('log analysis')
            ax.legend(title='kind color')

            plt.show()
            

        except Exception as e:
            QMessageBox.information(self, "Msg", "< Error > show_chart : " + str(e))
            logging.info("< Error > show_chart : " + str(e))
        finally:
            self.conn.commit()
            self.conn.close()

    

    #####################################
    #
    # show_news_total_statistics_chart
    #
    #####################################
    def show_news_total_statistics_chart(self):

        try:
            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()

            ############
            # et news
            ############
            self.sql = "select r_time , count(*) from scraping_news where kind='realtime' group by r_time order by r_time desc limit 0,36"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()
            #########
            # tech
            #########
            self.sql2 = "select r_time , count(*) from scraping_news where kind='tech' group by r_time order by r_time desc limit 0,36"
            self.curr.execute(self.sql2)
            self.res2 = self.curr.fetchall()
            ##########
            # pcdiy
            ##########
            self.sql3 = "select r_time , count(*) from scraping_news where kind='pcdiy' group by r_time order by r_time desc limit 0,36"
            self.curr.execute(self.sql3)
            self.res3 = self.curr.fetchall()
            ########
            # udn
            ########
            self.sql4 = "select r_time , count(*) from scraping_news where kind='udn' group by r_time order by r_time desc limit 0,36"
            self.curr.execute(self.sql4)
            self.res4 = self.curr.fetchall()
            
            ##################
            # data to chart
            ##################
            self.charts     = QChart()
            self.charts.setTitle('Total news Statistics')
            self.charts.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
            self.chart_view = QChartView(self.charts)
            self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

            ### line 1
            self.series0       = QLineSeries()
            self.series0.setPen(QPen(QColor('blue') , 3))
            self.series1       = QScatterSeries()
            self.series1.setColor(QColor('blue'))
            self.series1.setPen(QPen(QColor('blue') , 1))
            
            ### line 2
            self.series0_2       = QLineSeries()
            self.series0_2.setPen(QPen(QColor("red"),3))
            self.series0_2_p     = QScatterSeries()
            self.series0_2_p.setColor(QColor('red'))
            self.series0_2_p.setPen(QPen(QColor("red"),1))

            ### line 3
            self.series0_3       = QLineSeries()
            self.series0_3.setPen(QPen(QColor('darkgreen'),3))
            self.series0_3_p     = QScatterSeries()
            self.series0_3_p.setColor(QColor('darkgreen'))
            self.series0_3_p.setPen(QPen(QColor("darkgreen"),1))

            ### line 4
            self.series0_4       = QLineSeries()
            self.series0_4.setPen(QPen(QColor('darkyellow'),3))
            self.series0_4_p     = QScatterSeries()
            self.series0_4_p.setColor(QColor('darkyellow'))
            self.series0_4_p.setPen(QPen(QColor('darkyellow'),1))

            for val in self.res:
                ### chart para
                self.series0.setName('ET news')
                self.series1.setName('目前(總數)')
                self.date_fmt = "HH:mm:ss"
                self.data = str(val[0]).split(" ")
                self.time = self.data[1]
                self.x = QDateTime().fromString(self.time , self.date_fmt).toMSecsSinceEpoch()
                self.y = int(val[1])
                self.series0.append(self.x , self.y)
                self.series1.append(self.x , self.y)
                #self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_value)
            
            for val in self.res2:
                ### chart para
                self.series0_2.setName('TECH news')
                self.series0_2_p.setName('目前(總數)')
                self.date_fmt = "HH:mm:ss"
                self.data = str(val[0]).split(" ")
                self.time = self.data[1]
                self.x = QDateTime().fromString(self.time , self.date_fmt).toMSecsSinceEpoch()
                self.y = int(val[1])
                self.series0_2.append(self.x , self.y)
                self.series0_2_p.append(self.x , self.y)
                #self.series0_2.hovered.connect(self.history_record_to_chart_mouse_hover_value)

            for val in self.res3:
                ### chart para
                self.series0_3.setName('PC DIY')
                self.series0_3_p.setName('目前(總數)')
                self.date_fmt = "HH:mm:ss"
                self.data = str(val[0]).split(" ")
                self.time = self.data[1]
                self.x = QDateTime().fromString(self.time , self.date_fmt).toMSecsSinceEpoch()
                self.y = int(val[1])
                self.series0_3.append(self.x , self.y)
                self.series0_3_p.append(self.x , self.y)
                #self.series0_2.hovered.connect(self.history_record_to_chart_mouse_hover_value)
            
            for val in self.res4:
                ### chart para
                self.series0_4.setName('UDN news')
                self.series0_4_p.setName('目前(總數)')
                self.date_fmt = "HH:mm:ss"
                self.data = str(val[0]).split(" ")
                self.time = self.data[1]
                self.x = QDateTime().fromString(self.time , self.date_fmt).toMSecsSinceEpoch()
                self.y = int(val[1])
                self.series0_4.append(self.x , self.y)
                self.series0_4_p.append(self.x , self.y)
                #self.series0_2.hovered.connect(self.history_record_to_chart_mouse_hover_value)
            
            ### line 1
            self.charts.addSeries(self.series0)
            self.charts.addSeries(self.series1)
            ### line 2
            self.charts.addSeries(self.series0_2)
            self.charts.addSeries(self.series0_2_p)
            ### line 3
            self.charts.addSeries(self.series0_3)
            self.charts.addSeries(self.series0_3_p)
            ### line 4
            self.charts.addSeries(self.series0_4)
            self.charts.addSeries(self.series0_4_p)

            ### TEMP X-axis
            self.axis_x = QDateTimeAxis()
            self.axis_x.setTickCount(20)
            self.axis_x.setFormat("HH:mm:ss")
            self.axis_x.setTitleText("時間")
            self.charts.addAxis(self.axis_x , Qt.AlignmentFlag.AlignBottom)
            self.series0.attachAxis(self.axis_x)
            
            ### TEMP Y-axis
            self.axis_y = QValueAxis()
            self.axis_y.setTickCount(20)
            self.axis_y.setLabelFormat("%i")
            self.axis_y.setTitleText("數值")
            self.charts.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
            self.series0.attachAxis(self.axis_y)

            ### chart 
            self.chart = QWidget()
            self.sub   = QHBoxLayout()
            self.sub.addWidget(self.chart_view)
            self.chart.setLayout(self.sub)
            self.chart.resize(800,600)
            self.chart.show()

        except Exception as e:
            QMessageBox.information(self, "Msg", "< Error > show_news_statistics_chart : " + str(e))
            logging.info("< Error > show_news_statistics_chart : " + str(e))
        finally:
            self.conn.commit()
            self.conn.close()

    ###############################
    #
    # show_news_statistics_chart
    #
    ###############################
    def show_news_statistics_chart(self , kind):

        #############
        # variable
        #############
        self.kind = kind

        try:
            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()

            ###############
            # log record
            ###############
            self.sql = "select r_time , count(*) from scraping_news where kind='{0}' group by r_time order by r_time desc limit 0,36".format(self.kind)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            ##################
            # data to chart
            ##################
            self.charts     = QChart()
            self.charts.setTitle(self.kind)
            self.charts.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

            self.chart_view = QChartView(self.charts)
            self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

            ### 曲線
            self.series0       = QLineSeries()
            self.series0.setPen(QPen(QColor('skyblue') , 3))

            ### 顯示點的值
            self.series1       = QScatterSeries()
            self.series1.setColor(QColor('skyblue'))
            self.series1.setPen(QPen(QColor('skyblue') , 1))

            for val in self.res:
                ### chart para
                self.series0.setName(self.kind)
                self.series1.setName('目前(總數)')
                self.date_fmt = "HH:mm:ss"
                self.data = str(val[0]).split(" ")
                self.time = self.data[1]
                self.x = QDateTime().fromString(self.time , self.date_fmt).toMSecsSinceEpoch()
                self.y = int(val[1])
                self.series0.append(self.x , self.y)
                self.series1.append(self.x , self.y)
                self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_value)
            
            self.charts.addSeries(self.series0)
            self.charts.addSeries(self.series1)

            ### TEMP X-axis
            self.axis_x = QDateTimeAxis()
            self.axis_x.setTickCount(20)
            self.axis_x.setFormat("HH:mm:ss")
            self.axis_x.setTitleText("時間")
            self.charts.addAxis(self.axis_x , Qt.AlignmentFlag.AlignBottom)
            self.series0.attachAxis(self.axis_x)
            
            ### TEMP Y-axis
            self.axis_y = QValueAxis()
            self.axis_y.setTickCount(20)
            self.axis_y.setLabelFormat("%i")
            self.axis_y.setTitleText("數值")
            self.charts.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
            self.series0.attachAxis(self.axis_y)

            ### chart 
            self.chart = QWidget()
            self.sub   = QHBoxLayout()
            self.sub.addWidget(self.chart_view)
            self.chart.setLayout(self.sub)
            self.chart.resize(800,600)
            #self.chart.showFullScreen()
            self.chart.show()

        except Exception as e:
            QMessageBox.information(self, "Msg", "< Error > show_news_statistics_chart : " + str(e))
            logging.info("< Error > show_news_statistics_chart : " + str(e))
        finally:
            self.conn.commit()
            self.conn.close()

    ###############
    #
    # show_chart
    #
    ###############
    def show_chart(self , kind):

        #############
        # variable
        #############
        self.kind = kind

        try:
            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()

            ###############
            # log record
            ###############
            self.sql = "select s_time , total_counts from scraping_log where kind='{0}'  order by s_time desc limit 0,36;".format(self.kind)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            ##################
            # data to chart
            ##################
            self.charts     = QChart()
            self.charts.setTitle(self.kind)
            self.charts.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
            self.chart_view = QChartView(self.charts)
            self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
                    

            ### 曲線
            self.series0       = QLineSeries()
            self.series0.setPen(QPen(QColor('darkgreen'),3))

            ### 顯示點的值
            self.series1       = QScatterSeries()
            self.series1.setColor(QColor('darkgreen'))
            self.series1.setPen(QPen(QColor('darkgreen'),1))

            for val in self.res:
                ### TEMP chart para
                self.series0.setName(self.kind)
                self.series1.setName('目前(總數)')
                self.date_fmt = "HH:mm:ss"
                self.data = str(val[0]).split(" ")
                self.time = self.data[1]
                self.x = QDateTime().fromString(self.time , self.date_fmt).toMSecsSinceEpoch()
                self.y = int(val[1])
                self.series0.append(self.x , self.y)
                self.series1.append(self.x , self.y)
                self.series1.hovered.connect(self.history_record_to_chart_mouse_hover_value)
            
            self.charts.addSeries(self.series0)
            self.charts.addSeries(self.series1)

            ### TEMP X-axis
            self.axis_x = QDateTimeAxis()
            self.axis_x.setTickCount(20)
            self.axis_x.setFormat("HH:mm:ss")
            self.axis_x.setTitleText("時間")
            self.charts.addAxis(self.axis_x , Qt.AlignmentFlag.AlignBottom)
            self.series0.attachAxis(self.axis_x)
            
            ### TEMP Y-axis
            self.axis_y = QValueAxis()
            self.axis_y.setTickCount(20)
            self.axis_y.setLabelFormat("%i")
            self.axis_y.setTitleText("數值")
            self.charts.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
            self.series0.attachAxis(self.axis_y)

            ### chart 
            self.chart = QWidget()
            self.sub   = QHBoxLayout()
            self.sub.addWidget(self.chart_view)
            self.chart.setLayout(self.sub)
            self.chart.resize(800,600)

            self.chart.show()

        except Exception as e:
            QMessageBox.information(self, "Msg", "< Error > show_chart : " + str(e))
            logging.info("< Error > show_chart : " + str(e))
        finally:
            self.conn.commit()
            self.conn.close()
    
    ######################################################
    #
    # history record to chart mouse hover value by year
    #
    ######################################################
    def history_record_to_chart_mouse_hover_value_by_year(self , point):
        
        ################################
        # timemark transfer localtime
        ################################
        self.n_time = QDateTime.fromMSecsSinceEpoch(int(point.x())).toString("yyyy")
        self.series1.setName( self.n_time + ' , 目前  ' + str(int(point.y()))) 

    #######################################################
    #
    # history record to chart mouse hover value by month
    #
    #######################################################
    def history_record_to_chart_mouse_hover_value_by_month(self , point):
        
        ################################
        # timemark transfer localtime
        ################################
        self.n_time = QDateTime.fromMSecsSinceEpoch(int(point.x())).toString("yyyy-MM")
        self.series1.setName( self.n_time + ' , 目前  ' + str(int(point.y())))  

    #####################################################
    #
    # history record to chart mouse hover value by day
    #
    #####################################################
    def history_record_to_chart_mouse_hover_value_by_day(self , point):
        
        ################################
        # timemark transfer localtime
        ################################
        self.n_time = QDateTime.fromMSecsSinceEpoch(int(point.x())).toString("yyyy-MM-dd")
        self.series1.setName( self.n_time + ' , 目前  ' + str(int(point.y()))) 
    
    ##############################################
    #
    # history record to chart mouse hover value
    #
    ##############################################
    def history_record_to_chart_mouse_hover_value(self , point):
        
        ################################
        # timemark transfer localtime
        ################################
        self.n_time = QDateTime.fromMSecsSinceEpoch(int(point.x())).toString("HH:mm:ss")
        self.series1.setName( self.n_time + ' , 目前  ' + str(int(point.y())) + ' 筆') 

    ##################
    #
    # load_page_log
    #
    ##################
    def load_page_log(self):
        
        ################
        # select page
        ################
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_log)

        ##########
        # clear
        ##########
        self.ui.scraping_record_list.clear()
        self.ui.scraping_analysis_list.clear()

        try:
            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()

            ###############
            # log record
            ###############
            self.sql = "select s_time , e_time , kind from scraping_log  order by s_time desc limit 0,100"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.scraping_record_list.setHeaderLabels(['Start time','End time','Scraping item'])
            self.ui.scraping_record_list.setColumnWidth(0 , 180)
            self.ui.scraping_record_list.setColumnWidth(1 , 180)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.scraping_record_list)
                self.root.setText(0 , str(val[1]))
                self.root.setText(1 , str(val[0]))
                self.root.setText(2 , str(val[2]))
                
                ### old show style - QListWidgets
                #self.ui.scraping_record_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' , ' + str(val[2]))
            
            #################
            # log analysis
            #################
            self.sql = "select  kind , count(*) from scraping_log group by kind"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.scraping_analysis_list.setHeaderLabels(['Kind','Scraping total amount'])
            self.ui.scraping_analysis_list.setColumnWidth(0 , 180)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.scraping_analysis_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))

                ### old show style - QListWidgets
                #self.ui.scraping_analysis_list.addItem(str(val[0]) + ' , ' + str(val[1]))

        except Exception as e:
            QMessageBox.information(self, "Msg", "< Error > load_page_log : " + str(e))
            logging.info("< Error > load_page_log : " + str(e))
        finally:
            self.conn.commit()
            self.conn.close()
    
    ###################
    #
    # load_page_film
    #
    ###################
    def load_page_film(self):
        
        ################
        # select page
        ################
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_film)

        ##########
        # clear
        ##########
        self.ui.duck_film_list.clear()

        try:
            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()

            ##############
            # Duck film
            ##############
            self.sql = "select r_time , title , url from scraping_film where kind='all' order by no desc limit 0,200"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.duck_film_list.setHeaderLabels(['最後記錄','小鴨影音'])
            self.ui.duck_film_list.setColumnWidth(0 , 180)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.duck_film_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))
                self.root.setText(2 , str(val[2]))

                ### old show list - QListWidgets
                #self.ui.duck_film_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' , \t\t\t\t\t\t\t\t\t\t' + str(val[2]))
            
            self.ui.duck_film_list.doubleClicked.connect(lambda:self.open_website('duck_film'))

            ##################
            # Duck teleplay
            ##################
            self.sql = "select r_time , title , url from scraping_film where kind='duck_teleplay' order by no desc limit 0,200"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.duck_teleplay_list.setHeaderLabels(['最後記錄','小鴨電視劇'])
            self.ui.duck_teleplay_list.setColumnWidth(0 , 180)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.duck_teleplay_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))
                self.root.setText(2 , str(val[2]))

                ### old show style - QListWidgets
                #self.ui.duck_teleplay_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' , \t\t\t\t\t\t\t\t\t\t' + str(val[2]))
            
            self.ui.duck_teleplay_list.doubleClicked.connect(lambda:self.open_website('duck_teleplay'))
            
            ###############
            # Duck comic
            ###############
            self.sql = "select r_time , title , url from scraping_film where kind='duck_comic' order by no desc limit 0,200"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.duck_comic_list.setHeaderLabels(['最後記錄','小鴨動漫'])
            self.ui.duck_comic_list.setColumnWidth(0 , 180)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.duck_comic_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))
                self.root.setText(2 , str(val[2]))
                
                ### old show style - QListWidgets
                #self.ui.duck_comic_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' , \t\t\t\t\t\t\t\t\t\t' + str(val[2]))
            
            self.ui.duck_comic_list.doubleClicked.connect(lambda:self.open_website('duck_comic'))

        except Exception as e:
            QMessageBox.information(self, "Msg", "< Error > load_page_film : " + str(e))
            logging.info("< Error > load_page_film : " + str(e))
        finally:
            self.conn.commit()
            self.conn.close()
    
    ###################
    #
    # load_page_news
    #
    ###################
    def load_page_news(self):
        
        ################
        # select page
        ################
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_news)

        ### record time
        self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        self.r_year  = time.strftime("%Y" , time.localtime())
        self.r_month = time.strftime("%Y-%m" , time.localtime())
        self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 

        ##########
        # clear
        ##########
        self.ui.et_news_list.clear()
        self.ui.tech_news_list.clear()
        self.ui.pc_diy_list.clear()

        try:
            self.conn = pymysql.connect(host=tinfar_db['host'],port=tinfar_db['port'],user=tinfar_db['user'],passwd=tinfar_db['pwd'],database=tinfar_db['db'],charset=tinfar_db['charset'])    
            self.curr = self.conn.cursor()

            ############
            # ET News
            ############
            self.sql = "select r_time , title , url from scraping_news where kind='realtime' order by no desc limit 0,200"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.et_news_list.setHeaderLabels(['最後記錄','新聞標題'])
            self.ui.et_news_list.setColumnWidth(0 , 180)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.et_news_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))
                self.root.setText(2 , str(val[2]))
            
            ### open et news website
            self.ui.et_news_list.doubleClicked.connect(lambda:self.open_website('et_news'))

            ##############
            # Tech News
            ##############
            self.sql = "select r_time , title , url from scraping_news where kind='tech' order by no desc limit 0,200"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.tech_news_list.setHeaderLabels(['最後記錄','新聞標題'])
            self.ui.tech_news_list.setColumnWidth(0 , 180)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.tech_news_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))
                self.root.setText(2 , str(val[2]))

                ### old show style - QListWidgets
                #self.ui.tech_news_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' , \t\t\t\t\t\t\t\t\t\t' + str(val[2]))
            
            ### open et news website
            self.ui.tech_news_list.doubleClicked.connect(lambda:self.open_website('tech_news'))
            
            ##############
            # PC DIY
            ##############
            self.sql = "select r_time , title , url from scraping_news where kind='pcdiy' order by no desc limit 0,100"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.pc_diy_list.setHeaderLabels(['最後記錄','新聞標題'])
            self.ui.pc_diy_list.setColumnWidth(0 , 180)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.pc_diy_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))
                self.root.setText(2 , str(val[2]))

                ### old show style - QListWidgets
                #self.ui.pc_diy_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' , \t\t\t\t\t\t\t\t\t\t' + str(val[2]))

            #############
            # UDN news
            #############
            self.sql = "select r_time , title , url from scraping_news where kind='udn' order by no desc limit 0,100"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()

            self.ui.udn_news_list.setHeaderLabels(['最後記錄' , '新聞標題'])
            self.ui.udn_news_list.setColumnWidth(0 , 180)

            for val in self.res:
                self.root = QTreeWidgetItem(self.ui.udn_news_list)
                self.root.setText(0 , str(val[0]))
                self.root.setText(1 , str(val[1]))
                self.root.setText(2 , str(val[2]))

                ### old show style - QListWidgets
                #self.ui.udn_news_list.addItem(str(val[0]) + ' , ' + str(val[1]) + ' , \t\t\t\t\t\t\t\t\t\t' + str(val[2]))
                
            ### open et news website
            self.ui.udn_news_list.doubleClicked.connect(lambda:self.open_website('udn_news'))

        except Exception as e:
            QMessageBox.information(self, "Msg", "< Error > load_page_news : " + str(e))
            logging.info("< Error > load_page_news : " + str(e))
        finally:
            self.conn.commit()
            self.conn.close()
    
    #################
    #
    # open_website
    #
    #################
    def open_website(self , item):
        try:
            
            #############
            # variable
            #############
            if item == 'duck_film':
                self.data  = self.ui.duck_film_list.currentItem()
                self.data2 = self.data.text(2)
                self.data2 = self.data2.strip()
                self.url   = 'http://www.149mov.com' + self.data2
            elif item == 'duck_teleplay':
                self.data  = self.ui.duck_teleplay_list.currentItem()
                self.data2 = self.data.text(2)
                self.data2 = self.data2.strip()
                self.url   = 'https://777tv.app' + self.data2
            elif item == 'duck_comic':
                self.data  = self.ui.duck_comic_list.currentItem()
                self.data2 = self.data.text(2)
                self.data2 = self.data2.strip()
                self.url   = 'https://777tv.app' + self.data2
            elif item == 'udn_news':
                self.data  = self.ui.udn_news_list.currentItem()
                self.data2 = self.data.text(2)
                self.data2 = self.data2.strip()
                self.url   = 'https://udn.com' + self.data2
            elif item == 'et_news':
                self.data  = self.ui.et_news_list.currentItem()
                self.data2 = self.data.text(2)
                self.data2 = self.data2.strip()
                self.url   = 'https://www.ettoday.net' + self.data2
            elif item == 'tech_news':
                self.data  = self.ui.tech_news_list.currentItem()
                self.data2 = self.data.text(2)
                self.data2 = self.data2.strip()
                self.url   = self.data2


            #################
            # show website
            #################
            self.form    = QWidget()
            self.sub     = QVBoxLayout()
            self.menu    = QHBoxLayout()
            self.content = QHBoxLayout()

            self.line         = QLineEdit()
            self.btn_back     = QPushButton()
            self.btn_forward  = QPushButton()
            self.btn_reload   = QPushButton()
            self.btn_go       = QPushButton()
            self.website      = QtWebEngineWidgets.QWebEngineView()
            
            ### url
            self.line.setText(self.url)
            self.line.setObjectName('website_url')
            self.font = QFont()
            self.font.setFamily("Microsoft JhengHei")
            self.font.setPointSize(15)
            self.line.setFont(self.font)
            self.line.setStyleSheet("#website_url{background-color:#cccccc; padding:5px 5px;} #website_url:hover{background-color:gray; color:white;}")
            
            ### btn back
            self.btn_back.setObjectName("btn_back")
            self.btn_back.setText('上一頁')
            self.btn_back.setFont(self.font)
            self.btn_back.setStyleSheet("#btn_back{background-color:#cccccc; border-radius:5px; padding:5px 5px;} #btn_back:hover{background-color:gray; color:white;}")
            ### btn forward
            self.btn_forward.setObjectName("btn_forward")
            self.btn_forward.setText('下一頁')
            self.btn_forward.setFont(self.font)
            self.btn_forward.setStyleSheet("#btn_forward{background-color:#cccccc; border-radius:5px; padding:5px 5px;} #btn_forward:hover{background-color:gray; color:white;}")
            ### btn reload
            self.btn_reload.setObjectName("btn_reload")
            self.btn_reload.setText('重新整理')
            self.btn_reload.setFont(self.font)
            self.btn_reload.setStyleSheet("#btn_reload{background-color:#cccccc; border-radius:5px; padding:5px 5px;} #btn_reload:hover{background-color:gray; color:white;}")

            ### btn go
            self.btn_go.setObjectName("btn_go")
            self.btn_go.setText('Go')
            self.btn_go.setFont(self.font)
            self.btn_go.setStyleSheet("#btn_go{background-color:#cccccc; border-radius:5px; padding:5px 5px;} #btn_go:hover{background-color:gray; color:white;}")
            
            ### content
            self.website.load(QtCore.QUrl(self.url))
            self.btn_back.clicked.connect(self.website.back)
            self.btn_forward.clicked.connect(self.website.forward)
            self.btn_reload.clicked.connect(self.website.reload)
            self.btn_go.clicked.connect(lambda:self.website.load(QtCore.QUrl(str(self.line.text()))))

            self.menu.addWidget(self.btn_back)
            self.menu.addWidget(self.btn_forward)
            self.menu.addWidget(self.btn_reload)
            self.menu.addWidget(self.line)
            self.menu.addWidget(self.btn_go)
            self.content.addWidget(self.website)
            
            self.sub.addLayout(self.menu)
            self.sub.addLayout(self.content)

            self.form.setLayout(self.sub)
            self.form.resize(800,600)
            self.form.show() 

        except Exception as e:
            QMessageBox.information(self , 'Msg' , '< Error > open websiet : ' + str(e))    
            logging.info('< Error > open websiet : ' + str(e))    
        finally:
            pass

########################################################################################################################
#
# login
#
########################################################################################################################
class login(QWidget):
    
    ########
    # log 
    ########
    log_format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%H:%M:%S")
    
    #########
    # init
    #########
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.login_init()
    
    ###############
    # login_init
    ###############
    def login_init(self):

        ### login submit
        self.ui.btn_login_submit.clicked.connect(self.login_submit)

        ### login cancel
        self.ui.btn_login_cancel.clicked.connect(self.login_cancel)

    #################
    # login_submit
    #################
    def login_submit(self):
        
        ### variables
        self.user = self.ui.login_user.text()
        self.pwd  = self.ui.login_pwd.text()

        ### pwd encode MD5
        self.pwd_str = hashlib.md5()
        self.pwd_str.update(self.pwd.encode(encoding='utf8'))
        self.pwd_md5 = self.pwd_str.hexdigest()

        if self.user == 'rl8002002' and self.pwd_md5 == '274aca9430419de1a941eddcd4b647a0':
            
            ### close login form
            self.close()

            ### show main from
            self.main = main_content()
            self.main.show()

        elif len(self.user) == 0 or len(self.pwd) == 0:
            self.ui.login_msg.setStyleSheet('color:blue')
            self.ui.login_msg.setText('Username or Password not null !')
            logging.info('Username or Password not null !')
        else:
            self.ui.login_msg.setStyleSheet('color:blue')
            self.ui.login_msg.setText('Username or Password Error !')
            logging.info('Username or Password Error !')

    #################
    # login_cancel
    #################
    def login_cancel(self):
        QApplication.closeAllWindows()
    

########################################################################################################################
#
# start
#
########################################################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = login()
    main.show()
    sys.exit(app.exec())
