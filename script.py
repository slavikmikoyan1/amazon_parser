# -*- coding: utf-8 -*-
import sys
import os
import re
import threading
import urllib
sys.path.append(r'C:\Users\smikoyan\Python')
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

""" vars """
thread_main        = None

""" for users """

#************************** Set yours!! **************************
my_webdriver_path  = "C:\WebDrivers\V2.37\chromedriver.exe"

#******************************* setup *******************************
my_product = "Jabra"
my_sort =  "price-asc-rank"
#my_sort = "price-desc-rank"
url = "https://www.amazon.com/s?k="+my_product+"&s="+my_sort+"&ds=v1%3A%2BzXylj1RSF1e83Iiq8qzxyC6eyiuZ1tLA7O8z%2Bmx0YU&crid=NAH7EYSO4OLM&qid=1658487582&sprefix=jabra%2Caps%2C403&ref=sr_st_price-asc-rank"


""" classes """
class Parser():
    
    def __init__ (self):
        
        self.thread_main    = threading.Thread(target=self.main)

     
    def init_browser(self):
        chromedriver_path = my_webdriver_path
        os.environ["webdriver.chrome.driver"] = chromedriver_path
        
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--allow-running-insecure-content")    # trying to get passed
        #chrome_options.add_argument("--ignore-certificate-errors")         # the self-signed certs
        #chrome_options.add_argument("--ignore-urlfetcher-cert-requests")   
        #chrome_options.add_argument("--disable-gpu")                       
        chrome_options.add_argument("--window-size=1200x2900") 
        
        driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options) 
        return driver 
    
   
    
    def parse_page(self):
        self.driver = self.init_browser()        
        loaded_page_is_ok=False
        
        while( not loaded_page_is_ok ):    
            
            self.driver.get(url)  
                  
            body_element = self.driver.find_element(By.CLASS_NAME, "s-asin")
            print(body_element.text)
            loaded_page_is_ok = True
        
        
    
    def main(self):
       
        self.parse_page()
        

""" functions """
def main_prog():
   
   my_parser = Parser() 
   my_parser.thread_main.start()    
   my_parser.thread_main.join()

""" actions """
main_prog()