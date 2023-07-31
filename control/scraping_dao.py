#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20221229
# Update   : 20230223
# Function : scraping

import importlib , sys , logging
importlib.reload(sys)

import pymysql , time , requests , datetime , control.config
from bs4 import BeautifulSoup

####################################################################################################################################################################################
# link_db
####################################################################################################################################################################################
class link_db:

    ########
    # log   
    ########
    log_format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%H:%M:%S")

    ##############
    #
    # __connect
    #
    ##############
    def __connect__(self):
        try:
            self.conn = pymysql.connect(host=control.config.tinfar_db['host'],port=control.config.tinfar_db['port'],user=control.config.tinfar_db['user'],password=control.config.tinfar_db['pwd'],database=control.config.tinfar_db['db'],charset=control.config.tinfar_db['charset'])
            self.curr = self.conn.cursor()
        except Exception as e:
            logging.info('Error __connect__ : ' + str(e))
            exit()
        
    #################
    #
    # __disconnect
    #
    #################
    def __disconnect__(self):
        try:
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            logging.info('Error __disconnect__ : ' + str(e))
            exit()

    #######################
    #           
    # 工商時報 - realtime
    #
    #######################
    def add_commercial_times_news(self,url):
        try:
            #############
            # variable
            #############
            self.title = 'commercial_times_news'
            kind       = 'commercial_times_news'
            logging.info('Message : start scraping ' + self.title + ' ...')

            self.__connect__()            
            
            headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
                    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language" : "en-us",
                    "Connection" : "keep-alive",
                    "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}

            self.url      = url
            html          = requests.get(self.url , headers=headers , allow_redirects=False)
            html.encoding = 'utf8'
            soup          = BeautifulSoup(html.text , 'html.parser')
            content       = soup.findAll('a')
        
            r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        
            for data in content:            
                title = data.get('title')
                href = data.get('href')
                logging.info(title)
                logging.info(href)
            
                sql = "select title from scraping_news where title='{0}'".format(title)
                self.curr.execute(sql)
                res = self.curr.fetchone()
            
                if res is None:
                    sql2 = "insert into scraping_news(r_time , kind , title , url) values('{0}','{1}','{2}','{3}')".format(r_date,kind,title,href)
                    self.curr.execute(sql2)  

                    ##################
                    # save txt file
                    ##################
                    ### variable
                    self.item = kind
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

                    self.add = open(control.config.txt_path['commercial_times_news'] + self.item + self.r_day + '.txt','a')
                    self.add_content = str(self.r_time) + ' , ' + str(kind) + ' , ' + str(title) +  ' , '  + str(href) + '\n'
                    self.add.write(self.add_content)
                    self.add.close()  
        
            ###############
            # record log
            ###############
            
            ### total counts
            total_counts_sql = "select count(*) from scraping_news"
            self.curr.execute(total_counts_sql)
            res_total_counts = self.curr.fetchone()
            
            ### final record
            final_record_sql = "select r_time from scraping_news order by no desc limit 0,1"
            self.curr.execute(final_record_sql)
            res_final_record = self.curr.fetchone()

            self.record_log(kind , 'scraping finish. ', str(res_total_counts[0]) , str(res_final_record[0]))
            logging.info('Message : end scraping ' + kind + ' finish , total counts : ' + str(res_total_counts[0]) + ' , final record : ' + str(res_final_record[0]) + '\n')
       
        except Exception as e:
            logging.info("<< ERROR >> " + kind + " : " , str(e))
            
        finally:
            self.__disconnect__()   

    #####################
    #           
    # 卡提諾論壇 - 時事版
    #
    #####################
    def add_ck101_news(self,url):
        try:
            #############
            # variable
            #############
            self.title = 'ck101_news'
            kind       = 'ck101_news'
            logging.info('Message : start scraping ' + self.title + ' ...')

            self.__connect__()            
            
            headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
                    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language" : "en-us",
                    "Connection" : "keep-alive",
                    "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}

            self.url = url
            html = requests.get(self.url , headers=headers , allow_redirects=False)
            html.encoding = 'utf8'
            soup = BeautifulSoup(html.text , 'html.parser')
            content = soup.findAll('a')
        
            r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        
            for data in content:            
                title = data.get('title')
                href = data.get('href')
                #print(title)
                #print(href)
            
                sql = "select title from scraping_news where title='{0}'".format(title)
                self.curr.execute(sql)
                res = self.curr.fetchone()
            
                if res is None:
                    sql2 = "insert into scraping_news(r_time , kind , title , url) values('{0}','{1}','{2}','{3}')".format(r_date,kind,title,href)
                    self.curr.execute(sql2)  

                    ##################
                    # save txt file
                    ##################
                    ### variable
                    self.item = kind
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

                    self.add = open(control.config.txt_path['ck101_news'] + self.item + self.r_day + '.txt','a')
                    self.add_content = str(self.r_time) + ' , ' + str(kind) + ' , ' + str(title) +  ' , '  + str(href) + '\n'
                    self.add.write(self.add_content)
                    self.add.close()  
        
            ###############
            # record log
            ###############
            
            ### total counts
            total_counts_sql = "select count(*) from scraping_news"
            self.curr.execute(total_counts_sql)
            res_total_counts = self.curr.fetchone()
            
            ### final record
            final_record_sql = "select r_time from scraping_news order by no desc limit 0,1"
            self.curr.execute(final_record_sql)
            res_final_record = self.curr.fetchone()

            self.record_log(kind , 'scraping finish. ', str(res_total_counts[0]) , str(res_final_record[0]))
            logging.info('Message : end scraping ' + kind + ' finish , total counts : ' + str(res_total_counts[0]) + ' , final record : ' + str(res_final_record[0]) + '\n')
       
        except Exception as e:
            logging.info("<< ERROR >> " + kind + " : " , str(e))
            
        finally:
            self.__disconnect__()   
    
    ###################
    #           
    # add_duck_comic
    #
    ###################
    def add_duck_comic(self,url):
        try:
            #############
            # variable
            #############
            self.title = 'duck comic'
            kind       = 'duck_comic'
            logging.info('Message : start scraping ' + self.title + ' ...')

            self.__connect__()            
            
            self.url = url
            html = requests.get(self.url)
            html.encoding = 'utf8'
            soup = BeautifulSoup(html.text , 'html.parser')
            content = soup.findAll('a')
        
            r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        
            for data in content:            
                title = data.get('title')
                href = data.get('href')
                #print(title)
                #print(href)
            
                sql = "select title from scraping_film where title='{0}'".format(title)
                self.curr.execute(sql)
                res = self.curr.fetchone()
            
                if res is None:
                    sql2 = "insert into scraping_film(r_time , kind , title , url) values('{0}','{1}','{2}','{3}')".format(r_date,kind,title,href)
                    self.curr.execute(sql2)  

                    ##################
                    # save txt file
                    ##################
                    ### variable
                    self.item = kind
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

                    self.add = open(control.config.txt_path['duck_comic'] + self.item + self.r_day + '.txt','a')
                    self.add_content = str(self.r_time) + ' , ' + str(kind) + ' , ' + str(title) +  ' , https://777tv.app'  + str(href) + '\n'
                    self.add.write(self.add_content)
                    self.add.close()  
        
            ###############
            # record log
            ###############
            
            ### total counts
            total_counts_sql = "select count(*) from scraping_film"
            self.curr.execute(total_counts_sql)
            res_total_counts = self.curr.fetchone()
            
            ### final record
            final_record_sql = "select r_time from scraping_film order by no desc limit 0,1"
            self.curr.execute(final_record_sql)
            res_final_record = self.curr.fetchone()

            self.record_log(kind , 'scraping finish. ', str(res_total_counts[0]) , str(res_final_record[0]))
            logging.info('Message : end scraping ' + kind + ' finish , total counts : ' + str(res_total_counts[0]) + ' , final record : ' + str(res_final_record[0]) + '\n')
       
        except Exception as e:
            logging.info("<< ERROR >> " + kind + " : " , str(e))
            
        finally:
            self.__disconnect__()   
    
    ######################
    #           
    # add_duck_teleplay
    #
    ######################
    def add_duck_teleplay(self,url):
        try:
            #############
            # variable
            #############
            self.title = 'duck teleplay'
            kind       = 'duck_teleplay'
            logging.info('Message : start scraping ' + self.title + ' ...')

            self.__connect__()            
            
            self.url = url
            html = requests.get(self.url)
            html.encoding = 'utf8'
            soup = BeautifulSoup(html.text , 'html.parser')
            content = soup.findAll('a')
        
            r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        
            for data in content:            
                title = data.get('title')
                href = data.get('href')
                #print(title)
                #print(href)
            
                sql = "select title from scraping_film where title='{0}'".format(title)
                self.curr.execute(sql)
                res = self.curr.fetchone()
            
                if res is None:
                    sql2 = "insert into scraping_film(r_time , kind , title , url) values('{0}','{1}','{2}','{3}')".format(r_date,kind,title,href)
                    self.curr.execute(sql2)

                    ##################
                    # save txt file
                    ##################
                    ### variable
                    self.item = kind
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

                    self.add = open(control.config.txt_path['duck_teleplay'] + self.item + self.r_day + '.txt','a')
                    self.add_content = str(self.r_time) + ' , ' + str(kind) + ' , ' + str(title) +  ' , https://777tv.app'  + str(href) + '\n'
                    self.add.write(self.add_content)
                    self.add.close()  
        
            ###############
            # record log
            ###############
            
            ### total counts
            total_counts_sql = "select count(*) from scraping_film"
            self.curr.execute(total_counts_sql)
            res_total_counts = self.curr.fetchone()
            
            ### final record
            final_record_sql = "select r_time from scraping_film order by no desc limit 0,1"
            self.curr.execute(final_record_sql)
            res_final_record = self.curr.fetchone()

            self.record_log(kind , 'scraping finish. ', str(res_total_counts[0]) , str(res_final_record[0]))
            logging.info('Message : end scraping ' + kind + ' finish , total counts : ' + str(res_total_counts[0]) + ' , final record : ' + str(res_final_record[0]) + '\n')
       
        except Exception as e:
            logging.info("<< ERROR >> " + kind + " : " , str(e))
        finally:
            self.__disconnect__()   
    
    #################
    #           
    # add udn news
    #
    #################
    def add_udn_news(self,url):
        try:
            #############
            # variable
            #############
            self.title  = 'UDN news'
            self.url    = url
            self.kind   = "udn"
            logging.info('Message : start scraping ' + self.title + ' ...')
            
            html = requests.get(self.url)
            soup = BeautifulSoup(html.text , 'html.parser')
            #content = soup.findAll('a')
            content = soup.find_all('a')

            for data in content:
                title = data.string
                href = data.get('href')
                #print(title)
                #print(href)  
            
                if title == "":
                    self.title = "none"
                else:
                    self.title = title
            
                #####################
                # save DB and file
                #####################
                self.add_data_db(self.title, href , self.kind)
       
            ###############
            # record log
            ###############
            self.__connect__()
            
            ### total counts
            total_counts_sql = "select count(*) from scraping_news where kind='{0}'".format(self.kind)
            self.curr.execute(total_counts_sql)
            res_total_counts = self.curr.fetchone()
            
            ### final record
            final_record_sql = "select r_time from scraping_news where kind='{0}' order by no desc limit 0,1".format(self.kind)
            self.curr.execute(final_record_sql)
            res_final_record = self.curr.fetchone()

            self.record_log(str(self.kind) , 'scraping ' + str(self.title) + ' finish.' , str(res_total_counts[0]) , str(res_final_record[0]))
            logging.info('Message : end scraping ' + self.title + ' finish , total counts : ' + str(res_total_counts[0]) , ' , final record : ' + str(res_final_record[0]) + '\n')
            
        except Exception as e:
            logging.info("<< ERROR >> " + str(self.title) + " : " , str(e) , '\n')
        finally:
            self.__disconnect__()

    ##################          
    # add tech news
    ##################          
    def add_tech_news(self,url):
        try:
            self.title = 'TECH news'
            logging.info('Message : start scraping ' + self.title + ' ...')
            
            self.url = url
            self.kind = "tech"
            html = requests.get(self.url)
            soup = BeautifulSoup(html.text , 'html.parser')
            content = soup.findAll('a')
        
            for data in content:
                title = data.get_text().strip()
                href = data.get('href')
                #print(title)
                #print(href)            
            
                if title == "":
                    self.title = "none"
                else:
                    self.title = title
            
                ################
                # add data db
                ################
                self.add_data_db(self.title, href , self.kind)
       
            ### record log
            self.__connect__()
            # total counts
            total_counts_sql = "select count(*) from scraping_news where kind='tech'"
            self.curr.execute(total_counts_sql)
            res_total_counts = self.curr.fetchone()
            # final record
            final_record_sql = "select r_time from scraping_news where kind='tech' order by no desc limit 0,1"
            self.curr.execute(final_record_sql)
            res_final_record = self.curr.fetchone()

            self.record_log('TECH news', 'scraping tech news finish.' , str(res_total_counts[0]) , str(res_final_record[0]))
            logging.info('Message : end scraping TECH news finish , total counts : ' + str(res_total_counts[0]) , ' , final record : ' + str(res_final_record[0]) + '\n')
            
        except Exception as e:
            logging.info("<< ERROR >> TECH news : " , str(e) , '\n')
        finally:
            self.__disconnect__()

    ##################   
    #  
    # add duck film
    #
    ##################    
    def add_duck_film(self,url):
        try:
            #############
            # variable
            #############
            self.title = 'Duck film'
            kind       = 'all'
            logging.info('Message : start scraping ' + self.title + ' ...')

            self.__connect__()            
            
            self.url      = url
            html          = requests.get(self.url)
            html.encoding = 'utf8'
            soup          = BeautifulSoup(html.text , 'html.parser')
            content       = soup.findAll('a')
            r_date        = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        
            for data in content:            
                title = data.get('title')
                href  = data.get('href')
                #print(title)
                #print(href)
            
                sql = "select title from scraping_film where title='{0}'".format(title)
                self.curr.execute(sql)
                res = self.curr.fetchone()
            
                if res is None:
                    sql2 = "insert into scraping_film(r_time , kind , title , url) values('{0}','{1}','{2}','{3}')".format(r_date,kind,title,href)
                    self.curr.execute(sql2)  

                    ##################
                    # save txt file
                    ##################
                    ### variable
                    self.item = 'duck_film_'
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

                    self.add = open(control.config.txt_path['duck_film'] + self.item + self.r_day + '.txt','a')
                    self.add_content = str(r_date) + ' , ' + str(kind) + ' , ' + str(title) +  ' , http://www.149mov.com'  + str(href) + '\n'
                    self.add.write(self.add_content)
                    self.add.close()
        
            ###############
            # record log
            ###############
            
            ### total counts
            total_counts_sql = "select count(*) from scraping_film"
            self.curr.execute(total_counts_sql)
            res_total_counts = self.curr.fetchone()
            
            ### final record
            final_record_sql = "select r_time from scraping_film order by no desc limit 0,1"
            self.curr.execute(final_record_sql)
            res_final_record = self.curr.fetchone()

            self.record_log('Duck film', 'scraping finish.', str(res_total_counts[0]) , str(res_final_record[0]))
            logging.info('Message : end scraping Duck film finish , total counts : ' + str(res_total_counts[0]) + ' , final record : ' + str(res_final_record[0]) + '\n')
       
        except Exception as e:
            logging.info("<< ERROR >> Duck film : " , str(e) , '\n')
            
        finally:
            self.__disconnect__()    


    #########################    
    #
    # add PCDIY news  
    #
    #########################      
    def add_pcdiy_news(self,url,tb,kind):
        try:
            self.s_kind  = kind
            self.s_title = 'PCDIY news'
            logging.info('Message : start scraping ' +  self.s_title + ' ... ')        
            
            self.__connect__()
            
            self.url = url
            html = requests.get(self.url)
            html.encoding = 'utf8'
            soup = BeautifulSoup(html.text , 'html.parser')
            content = soup.findAll('a')
        
            r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        
            for data in content:            
                if kind == self.s_kind:                             
                    s_title2 = data.get_text()
                    s_href2 = data.get('href')                
                    complete_url = s_href2
                    #print(s_title2)
                    #print(s_href2)                                              
            
                    sql = "select `title` from " + tb  + " where `title`='{0}' ".format(s_title2)
                    self.curr.execute(sql)
                    res = self.curr.fetchone()            

                if res is None:                    
                    sql2 = "insert into " + tb + "(`title`,`url`,`kind`,`r_time`) values('{0}','{1}','{2}','{3}')".format(s_title2,complete_url,kind,r_date)
                    self.curr.execute(sql2)

                    ##################
                    # save txt file
                    ##################
                    ### variable
                    self.item = 'pc_diy_'
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

                    self.add = open(control.config.txt_path['pc_diy'] + self.item + self.r_day + '.txt','a')
                    self.add_content = str(r_date) + ' , ' + str(kind) + ' , ' + str(s_title2) +  ' , '  + str(complete_url) + '\n'
                    self.add.write(self.add_content)
                    self.add.close()

            ### record log
            # total counts
            total_counts_sql = "select count(*) from " + tb + " where `kind`='" + self.s_kind + "'"
            self.curr.execute(total_counts_sql)
            res_total_counts = self.curr.fetchone()
            # final record
            final_record_sql = "select r_time from " + tb + " where `kind`='" + self.s_kind + "' order by no desc limit 0,1"
            self.curr.execute(final_record_sql)
            res_final_record = self.curr.fetchone()

            self.record_log(self.s_title , 'scraping ' + self.s_title + ' finish.' , str(res_total_counts[0]) , str(res_final_record[0]))        
            
            logging.info('Message : end scraping ' + self.s_title + ' finish , total counts : ' + str(res_total_counts[0]) + ' , final record : ' + str(res_final_record[0]) + '\n')        

        except Exception as e:
            logging.info("<< ERROR >> " + self.s_title + " : " , str(e) , '\n')
        finally:
            self.__disconnect__()  

    #########################
    #     
    # add realtime ET news  
    #
    #########################      
    def add_realtime_et_news(self,url,tb,kind):
        try:
            
            self.title = 'ET realtime news'
            logging.info('Message : start scraping ' +  self.title + ' ... ')        

            self.__connect__()
            
            self.url = url
            html = requests.get(self.url)
            html.encoding = 'utf8'
            soup = BeautifulSoup(html.text , 'html.parser')
            content = soup.findAll('a')
        
            r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        
            for data in content:            
                if kind == "realtime":                             
                    title = data.get_text()
                    href = data.get('href')                
                    complete_url = href
                    #print(title)
                    #print(href)                                              
            
                    sql = "select title from " + tb  + " where title='{0}'".format(title)
                    self.curr.execute(sql)
                    res = self.curr.fetchone()            

                if res is None:                    
                    sql2 = "insert into " + tb + "(title,url,kind,r_time) values('{0}','{1}','{2}','{3}')".format(title,complete_url,kind,r_date)
                    self.curr.execute(sql2)

                    ##################
                    # save txt file
                    ##################
                    ### variable
                    self.item = 'ET_news_'

                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

                    self.add = open(control.config.txt_path['et_news'] + self.item + self.r_day + '.txt','a')
                    self.add_content = str(r_date) + ' , ' + str(kind) + ' , ' + str(title) +   ' , https://www.ettoday.net'  + str(complete_url) + '\n'
                    self.add.write(self.add_content)
                    self.add.close()

                    ####################
                    # line notify one
                    ####################
                    #self.line_notify_one(title)

            ### record log
            # total counts
            total_counts_sql = "select count(*) from " + tb + " where kind='realtime' "
            self.curr.execute(total_counts_sql)
            res_total_counts = self.curr.fetchone()
            # final record
            final_record_sql = "select r_time from " + tb + " where kind='realtime' order by no desc limit 0,1"
            self.curr.execute(final_record_sql)
            res_final_record = self.curr.fetchone()

            self.record_log(self.title , 'scraping ET realtime news finish.' , str(res_total_counts[0]) , str(res_final_record[0]))        
            
            logging.info('Message : end scraping ET realtime news finish , total counts : ' + str(res_total_counts[0]) + ' , final record : ' + str(res_final_record[0]) + '\n')        

        except Exception as e:
            logging.info("<< ERROR >> ET realtime news : " , str(e) , '\n')
        finally:
            self.__disconnect__()  
        
    ##########################
    # line notify - 一對一
    ##########################
    def line_notify_one(self , msg):

        ### variables
        token3  = 'etECmdmXAitOol7GnYBbrccF8m9Fx7IrZ8v7j45cYuN'
        headers = {'Authorization':'Bearer ' + token3}
        message = msg
        data    = {'message':message}

        try:
            res = requests.post("https://notify-api.line.me/api/notify" , headers=headers , data=data)
            if res:
                logging.info('< success > line notify : ' + message)
            else:
                logging.info('< Fail > line notify : ' + message)
        except Exception as e:
            logging.info('< Error > line notify : ' + str(e))

    ##############
    #
    #record log
    #
    ##############        
    def record_log(self,kind,content,total_counts,final_record):
        try:
            self.r_kind = kind
            self.r_content = content
            self.r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime()) 
        
            r_sql = "insert into scraping_log(s_time,kind,content,total_counts,e_time) values('{0}','{1}','{2}','{3}','{4}')".format(self.r_date,self.r_kind,self.r_content,total_counts,final_record)
            self.curr.execute(r_sql)
        except Exception as e:
            logging.info("<< ERROR >> record log : " , str(e) , '\n')    
        
    ##############
    #     
    # add to db
    #
    ##############    
    def add_data_db(self,title,url,kind):
        try:
            self.__connect__()
        
            self.r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        
            self.sql = "select title from scraping_news where title='{0}'".format(title)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchone()
        
            if self.res is None:
                self.sql2 = "insert into scraping_news(title,url,kind,r_time) values('{0}','{1}','{2}','{3}')".format(title,self.conn.escape_string(url),kind,self.r_date)                
                self.curr.execute(self.sql2)

                ##################
                # save txt file
                ##################
                if kind == 'tech':
                    ### variable
                    self.item = kind
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

                    ### write txt file
                    self.add = open(control.config.txt_path['tech'] + self.item + self.r_day + '.txt','a')
                    self.add_content = str(self.r_time) + ' , ' + str(self.kind) + ' , ' + str(title) +  ' , '  + str(url) + '\n'
                    self.add.write(self.add_content)
                    self.add.close()

                    ### line notify
                    #self.line_notify_one(title)

                elif kind == 'udn':
                    ### variable
                    self.item = kind
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())

                    ### write txt file
                    self.add = open(control.config.txt_path['udn'] + self.item + self.r_day + '.txt','a')
                    self.add_content = str(self.r_time) + ' , ' + str(self.kind) + ' , ' + str(title) +  ' , https://udn.com'  + str(url) + '\n'
                    self.add.write(self.add_content)
                    self.add.close()

                    ### line notify
                    #self.line_notify_one(title)

        except Exception as e:
            logging.info("< ERROR > add data db : " , str(e) , '\n')
            
        finally:
            self.__disconnect__()    
        
