import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import csv
from datetime import datetime
import sys
import json

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path='driver/chromedriver',chrome_options=chrome_options)

desired_cap = chrome_options.to_capabilities()

def get_watchpage(link, loc, query):
    if link.split('.com//')[1].startswith('watch'):
        print(link)
        driver.get(link)
        sleep(3)
        result_html = driver.page_source
        filename = link.split('?')[1]
        filepath = loc+'/'+query+'/'+filename+'.html'
        with open(filepath, 'w') as result_file:
            result_file.write(result_html)

def main(path):
    #path = f'iowa_zone_a_videos.json'
    loc_folder = path.split('.json')[0]
    os.mkdir(loc_folder)
    with open(path, 'r') as inFile:
        video_links = json.load(inFile)
        for i, link in enumerate(links):
            sleep(7)
            get_watchpage(links, loc_folder)
    driver.close()

if __name__ == "__main__":
    main(sys.argv[1])
