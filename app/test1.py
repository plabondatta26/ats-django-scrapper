from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import json
# from .data_handler import data_formatter, location_engineering
from datetime import datetime
from multiprocessing import Process, Queue, Pool, Manager
import time
import json
import html_to_json

def zillow_scrapper(link):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    html_data = None

    driver.get(link)
    parent_of_data = driver.find_element_by_class_name('hdp__sc-1gqth4d-0')
    html_data = parent_of_data.get_attribute('innerHTML')
    output_json = html_to_json.convert(html_data)
    location = output_json["h1"][0]["_values"][0] + output_json["h1"][0]["_values"][1]
    driver.close()

url = 'https://www.zillow.com/homes/24634-N-36th-Avenue,-Glendale,-AZ-85310_rb/7932419_zpid/'
zillow_scrapper(url)