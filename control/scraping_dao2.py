#!/usr/bin/python
# -*- coding: utf-8 -*-
import importlib
import sys
importlib.reload(sys)

# python3 default unicode so disabled utf-8
#sys.setdefaultencoding('utf-8')  

import pymysql , time , requests , datetime , config 
from bs4 import BeautifulSoup


HOST = config.host
USER = config.user
PWD  = config.pwd
DB   = config.db


class link_db:
        
    def __connect__(self):
        self.conn = pymysql.connect(host=HOST,user=USER,password=PWD,database=DB,charset='utf8')
        self.curr = self.conn.cursor()

    def __disconnect__(self):
        self.conn.commit()
        self.conn.close()
          
    def check(self,url):
        try:
            print('Message : start scraping tech news...')
            
            self.url = url
            html = requests.get(self.url)
            soup = BeautifulSoup(html.text , 'html.parser')
            content = soup.findAll('a')
        
            self.kind = "tech"
        
            for data in content:
                title = data.get_text().strip()
                href = data.get('href')
                #print(title)
                #print(href)            
            
                if title == "":
                    self.title = "none"
                else:
                    self.title = title
            
                self.add_data_db(self.title, href , self.kind)
       
            ### record log
            self.__connect__()
            self.record_log('Tech news', 'scraping tech news finish.')
            print('Message : tech news scraping finish.')
            
        except Exception as e:
            print("error check : " , e)
            
        finally:
            self.__disconnect__()
        
        
    def add_duck_film(self,url):
        try:
            print('Message : start scraping 小鴨影音...')
            self.__connect__()            
            
            self.url = url
            html = requests.get(self.url)
            html.encoding = 'utf8'
            soup = BeautifulSoup(html.text , 'html.parser')
            content = soup.findAll('a')
        
            r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            kind = 'all'
        
            for data in content:            
                title = data.get('title')
                href = data.get('href')
                #print(title)
                #print(href)
            
                sql = "select title from btn11_film where title='{0}'".format(title);
                self.curr.execute(sql)
                res = self.curr.fetchone()
            
                if res is None:
                    sql2 = "insert into btn11_film(record_time , kind , title , url) values('{0}','{1}','{2}','{3}')".format(r_date,kind,title,href)
                    self.curr.execute(sql2)  
        
            ### record log
            self.record_log('Duck film', 'scraping 小鴨影音 finish.')
            print('Message : scraping 小鴨影音 finish.')
       
        except Exception as e:
            print("error add_duck_film : " , e)
            
        finally:
            self.__disconnect__()    
        
        
    ### realtime ET news    
    def add_realtime_et_news(self,url,tb,kind):
        try:
            print('Message : scraping realtime ET news... ')        
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
                    sql2 = "insert into " + tb + "(title,url,kind,record_time) values('{0}','{1}','{2}','{3}')".format(title,complete_url,kind,r_date)
                    self.curr.execute(sql2)

            ### record log
            self.record_log('ET news', 'scraping realtime ET news finish.')        
                
            print('Message : scraping realtime ET news finish.')        
        except Exception as e:
            print("error add_realtime_et_news : " , e)
            
        finally:
            self.__disconnect__()  
        
            
    ### record log        
    def record_log(self,kind,content):
        try:
            self.r_kind = kind
            self.r_content = content
            self.r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime()) 
        
            r_sql = "insert into btn10_log(record_date,kind,content) values('{0}','{1}','{2}')".format(self.r_date,self.r_kind,self.r_content)
            self.curr.execute(r_sql)
        except Exception as e:
            print("error record_log : " , e)    
        
        
    ### add to db
    def add_data_db(self,title,url,kind):
        try:
            self.__connect__()
        
            self.r_date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        
            self.sql = "select title from btn10_news where title='{0}'".format(title)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchone()
        
            if self.res is None:
                self.sql2 = "insert into btn10_news(title,url,kind,record_time) values('{0}','{1}','{2}','{3}')".format(title,self.conn.escape_string(url),kind,self.r_date)                
                self.curr.execute(self.sql2)
        except Exception as e:
            print("error add_data_db : " , e)
            
        finally:
            self.__disconnect__()    
        
