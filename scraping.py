#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20221229
# Update   : 20221229
# Function : scraping

import logging , time
from control.scraping_dao import link_db

#################################################################################################################################################################
#
# main
#
#################################################################################################################################################################
def main():
    
    ########
    # log
    ########
    log_format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%H:%M:%S")
    
    try:
        print('--------------------------------------------------------------------------------------------------------------------')
        
        ############
        # link_db
        ############
        catch = link_db()
    
        ############
        # 工商時報
        ############
        ### realtime
        #index = "https://ctee.com.tw/livenews"
        #catch.add_commercial_times_news(index)

        ###################
        # 卡提諾論壇 時事版
        ###################
        ### all
        index = "https://ck101.tw/forum-3590-1.html"
        catch.add_ck101_news(index)
        ### page 2
        index2 = "https://ck101.tw/forum-3590-2.html"
        catch.add_ck101_news(index2)
        ### page 3
        index3 = "https://ck101.tw/forum-3590-3.html"
        catch.add_ck101_news(index3)
        ### page 4
        index4 = "https://ck101.tw/forum-3590-4.html"
        catch.add_ck101_news(index4)
        ### page 5
        index5 = "https://ck101.tw/forum-3590-5.html"
        catch.add_ck101_news(index5)
        ### page 6
        index6 = "https://ck101.tw/forum-3590-6.html"
        catch.add_ck101_news(index6)
        ### page 7
        index7 = "https://ck101.tw/forum-3590-7.html"
        catch.add_ck101_news(index7)
        ### page 8
        index8 = "https://ck101.tw/forum-3590-8.html"
        catch.add_ck101_news(index8)
        ### page 9
        index9 = "https://ck101.tw/forum-3590-9.html"
        catch.add_ck101_news(index9)
        ### page 10
        index10 = "https://ck101.tw/forum-3590-10.html"
        catch.add_ck101_news(index10)

        ###############
        # duck comic
        ###############
        ### all
        index  = "https://777tv.app/vod/show/id/30.html"
        catch.add_duck_comic(index)
        ### page 2
        index2 = "https://777tv.app/vod/show/id/30/page/2.html"
        catch.add_duck_comic(index2)
        ### page 3
        index3 = "https://777tv.app/vod/show/id/30/page/3.html"
        catch.add_duck_comic(index3)
        ### page 4
        index4 = "https://777tv.app/vod/show/id/30/page/4.html"
        catch.add_duck_comic(index4)
        ### page 5
        index5 = "https://777tv.app/vod/show/id/30/page/5.html"
        catch.add_duck_comic(index5)
        ### page 6
        index6 = "https://777tv.app/vod/show/id/30/page/6.html"
        catch.add_duck_comic(index6)
        ### page 7
        index7 = "https://777tv.app/vod/show/id/30/page/7.html"
        catch.add_duck_comic(index7)
        
        ##################
        # duck teleplay
        ##################
        index = "https://777tv.app/vod/type/id/2.html"
        catch.add_duck_teleplay(index)

        #############
        # udn news
        #############
        udn_url = "https://udn.com/news/breaknews/1"
        catch.add_udn_news(udn_url)
        
        ##############
        # duck film   
        ##############     
        index = "http://www.149mov.com"
        catch.add_duck_film(index)
    
        ##############
        # tech news
        ##############
        url = "https://technews.tw/" 
        catch.add_tech_news(url)

        #####################
        # ET realtime news   
        #####################
        kind = "realtime"    
        tb2  = "scraping_news"
        url  = "https://www.ettoday.net/news/news-list.htm"    
        catch.add_realtime_et_news(url,tb2,kind)

        ###############
        # PCDIY news   
        ###############
        kind = "pcdiy"    
        tb2  = "scraping_news"
        url  = "http://www.pcdiy.com.tw/"    
        catch.add_pcdiy_news(url,tb2,kind)

        print('--------------------------------------------------------------------------------------------------------------------')
        
    except Exception as e:
        logging.info("catch scraping error ! : " + str(e))  
    finally:
        pass  

#################################################################################################################################################################
#
# start
#
#################################################################################################################################################################
if __name__ == '__main__':
    
    while True:
        main()
        time.sleep(300)
        

        
    

    
        




