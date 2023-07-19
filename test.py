#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20221229
# Update   : 20230307
# Function : test scraping

import requests , re , pymysql , time , urllib3
from bs4 import BeautifulSoup

########################################################################################################
#
# test
#
########################################################################################################
class test():
    
    def scraping2(self):

        url     = requests.get("https://www.ettoday.net/news/news-list-2023-3-27-0.htm")
        soup    = BeautifulSoup(url.text , "html.parser")
        content = soup.findAll("a")

        for val in content:
            title = val.get("title")
            href = val.get("href")
            
            if str(title) != 'None':
                title = title.strip()
                print(str(title))
        
    
    def scraping(self):
        try:
            val        = {'user':'root','pwd':'111111'}
            user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
            headers    = {'User-Agent':user_agent}
            url        = "https://www.google.com.tw/search?source=hp&ei=a4pfXb7UBY_60gTMqovABA&q=旺宏&oq=旺宏&gs_l=psy-ab.3..35i39i285j35i39j0i131l2j0l6.838.2853..3388...0.0..0.157.478.8j1......0....1..gws-wiz.....10..35i39i19.UJhMaRRLYaE&ved=0ahUKEwj-teKusZjkAhUPvZQKHUzVAkgQ4dUDCAU&uact=5"
            
            r       = requests.post(url , data=val , headers=headers)    
            soup    = BeautifulSoup(r.text , 'html.parser')
            content = soup.findAll('a')
            
            for data in content:
                content = data.get_text().strip()
                href = data.get('href')
                print(content)
                print(href)
            
        except Exception as e:
            print("< Error > scraping : " , str(e))

########################################################################################################
#
# start
#
########################################################################################################
if __name__ == "__main__":
    run = test()
    run.scraping2()
    
        
                
                
                
        
    