#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20221229
# Update   : 20230307
# Function : scraping - line notify

import requests , time , pymysql , smtplib , pysftp as sftp
from control.config import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

############################################################################################################################
#
# main
#
############################################################################################################################
class main_content():
    
    #####################
    # send_line_notify
    #####################
    def main(self):
        
        self.item = item_fun()
        self.item.send_email()
        self.item.push_sftp()
        self.item.line_notify()

############################################################################################################################
#
# item_fun
#
############################################################################################################################
class item_fun():

    #####################
    # line_notify_goods
    #####################
    def line_notify_goods(self , msg):
        try:
            ### varuables
            self.msg = msg

            ### record time
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y-%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 

            ##########################
            # line notify - 好康報報
            ##########################
            token   = 'K9xcpuuFmnMmiBvrTBpG8oFte3g5oZ7VaXHoeisgxae'
            headers = {'Authorization':'Bearer ' + token}
            message = self.msg
            data    = {'message':message}

            try:
                res = requests.post("https://notify-api.line.me/api/notify" , headers=headers , data=data)
                if res:
                    print('< success > ' + message)
                else:
                    print('< Fail > ' + message)
            except Exception as e:
                print('< Error > line notify : ' + str(e))
            

        except Exception as e:
            print('< Error > line_notify_goods : ' + str(e))
        finally:
            pass

    #####################
    # line_notify_ming
    #####################
    def line_notify_ming(self , msg):
        try:
            ### varuables
            self.msg = msg

            ### record time
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y-%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 

            ##########################
            # line notify - 阿明一家
            ##########################
            
            token2  = 'ESwsm3lrwhMsvDKP906sn6vAAsTeR7UNSYAU9drcaxI'
            headers = {'Authorization':'Bearer ' + token2}
            message = self.msg
            data    = {'message':message}

            try:
                res = requests.post("https://notify-api.line.me/api/notify" , headers=headers , data=data)
                if res:
                    print('< success > ' + message)
                else:
                    print('< Fail > ' + message)
            except Exception as e:
                print('< Error > line notify : ' + str(e))

        except Exception as e:
            print('< Error > line_notify_ming : ' + str(e))
        finally:
            pass


    ################
    # line notify
    ################
    def line_notify(self):
        try:
            ### varuables
            self.msg = "test line notify msg."

            ### record time
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y-%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
            
            ##########################
            # line notify - 一對一
            ##########################
            token3  = line_nootify_token['1by1']
            headers = {'Authorization':'Bearer ' + token3}
            message = self.msg
            data    = {'message':message}

            try:
                res = requests.post("https://notify-api.line.me/api/notify" , headers=headers , data=data)
                if res:
                    self.update_db(self.r_time , message)
                    print('< success > ' + message)
                else:
                    print('< Fail > ' + message)
            except Exception as e:
                print('< Error > line notify : ' + str(e))
        except Exception as e:
            pass
        finally:
            pass

    ##############
    # push_sftp
    ##############
    def push_sftp(self):
        try:
            ### record time
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y-%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
            
            cnopts = sftp.CnOpts()
            cnopts.hostkeys = None
            self.sftp = sftp.Connection(host=tinfar_nb_sftp['host'] , username=tinfar_nb_sftp['user'] , password=tinfar_nb_sftp['pwd'] , port=tinfar_nb_sftp['port'] , cnopts=cnopts)
            self.sftp.chdir(tinfar_nb_sftp['path'])
            self.sftp.put('test.py')
            
            ### print msg
            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' , sftp put file successful.')
            print('----------------------------------------------------------------------------------------------')
            self.sftp.close()
        except Exception as e:
            print('< Error > push_sftp : ' + str(e))
        finally:
            pass

    ###############
    # semd_email 
    ###############
    def send_email(self):
        
        ### variables
        self.email = 'Jason@tinfar.com.tw'
        
        ### record time
        self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        self.r_year  = time.strftime("%Y" , time.localtime())
        self.r_month = time.strftime("%Y-%m" , time.localtime())
        self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 

        try:
            smtpobj = smtplib.SMTP(tinfar_smtp['host'] , tinfar_smtp['port'])
            ### start smtp 
            smtpobj.ehlo() 
            ### use TLS transmission   
            smtpobj.starttls()

            smtpobj.login(tinfar_smtp['user'],tinfar_smtp['pwd'])
            
            msg = MIMEMultipart()
            msg["subject"] = "自動發信記錄"
            msg["from"]    = 'Jason@tinfar.com.tw'
            msg["to"]      = self.email
            msg.attach(MIMEText('自動發信記錄\n\t' + str(self.r_time) + " , 自動發信記錄 成功."))
            smtpobj.send_message(msg=msg)

            print('----------------------------------------------------------------------------------------------')
            print(self.r_time + ' , ' + str(' send ' + self.email + ' successful.'))
            print('----------------------------------------------------------------------------------------------')
            smtpobj.quit()
        except Exception as e:
            print('< Error > send email : ' + str(e))
        finally:
            pass

    ##############
    # update_db
    ##############
    def update_db(self , s_time , content):
        
        ### variables
        self.s_time  = s_time
        self.content = content

        try:
            ### insert into MySQL by this month
            self.conn2 = pymysql.connect(host=tinfar_VM['host'],port=tinfar_VM['port'],user=tinfar_VM['user'],passwd=tinfar_VM['pwd'],database=tinfar_VM['db'],charset=tinfar_VM['charset'])
            self.curr2 = self.conn2.cursor()

            self.sql2 = "insert into scraping_line_notify(s_time , content) value('{0}' , '{1}')".format(self.r_time , self.content)
            self.res = self.curr2.execute(self.sql2)
            
            print('----------------------------------------------------------------------------------------------')
            if self.res:
                print('< Notify > update db success.')
            else:
                print('< Notify > update db failed.')
            print('----------------------------------------------------------------------------------------------')

        except Exception as e:
            print('< Error > update_db : ' + str(e))
        finally:
            self.conn2.commit()
            self.conn2.close()
            

############################################################################################################################
#
# main
#
############################################################################################################################
if __name__ == '__main__':
    send = main_content()
    send.main()






