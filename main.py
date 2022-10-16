import requests
import lxml
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


s = Service("/home/unotuno/chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
chrome_options = Options()
a = []
driver.get('https://www.wildberries.by/catalog/0/search.aspx?sort=popular&search=%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8+nike')
time.sleep(5)
info={}
sneaker = driver.find_elements(By.CLASS_NAME, "product-card__main")
file__parser = open('info.txt','w')
for sn in sneaker:
    a.append(sn.get_attribute('href'))


for price__link in a:
    driver.get(price__link)
    info['Ссылка на товар '] = price__link
    file__parser.write("Link of sneakers : "+price__link)
   # time.sleep(6)
    for price in driver.find_elements(By.CLASS_NAME,'price-block__final-price'):
        info['Цена товара '] = price.text
        file__parser.write("Price : " + price.text)
    for art in driver.find_elements(By.ID,'productNmId'):
       info['Артикул товара '] = art.text
       file__parser.write("Art. : " + art.text + '\n')
       print(info)
file__parser.close()


"""response = requests.get(price__link)
    soup = BeautifulSoup (response.content,'lxml')
    print(response.status_code)
    time.sleep(5)
    price = soup.find('ins')
    print(price)"""
















