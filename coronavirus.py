import re
import pandas as pd
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html'

driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver.get(url)
wait = WebDriverWait(driver, 10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
dic = get_info(soup)
print(dic)

def get_info(info):
    date = info.find('span', class_="text-red").text
    summary = info.find('div', class_ = "2019coronavirus-summary").find_all('li')
    for i in summary:
        dic = {
            'total': summary[0].text,
            'deaths': summary[1].text,
            'jurisdictions': summary[2].text
        }
    dic['date'] = date
    return dic

wait.until(EC.frame_to_be_available_and_switch_to_it("cdcMaps1"))
wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'h3'))).click()
element = driver.find_element_by_tag_name('h3')
driver.execute_script('return arguments[0].scrollIntoView(true);', element)

for table in driver.find_elements_by_xpath('//[@id="root"]/section/section/div'):
        header = [item.text for item in table.find_elements_by_xpath('//[@id="root"]/section/section/div/div[1]/div[1]')]
        print(header)

for table in driver.find_elements_by_xpath('//[@id="root"]/section/section/div'):
        data = [item.text for item in table.find_elements_by_xpath('//[@id="root"]/section/section/div/div[1]/div[2]')]
        print(data)