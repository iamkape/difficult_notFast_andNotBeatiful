# import requests
# import lxml
# from bs4 import BeautifulSoup
# import chromedriver as chromedriver
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# press Ctrl+Alt+O
# It's for optimize imports


s = Service("/home/unotuno/chromedriver")
driver = webdriver.Chrome(service=s)

# executable_path = '/home/dkysyelyev/Pycharm_Projects/difficult_notFast_andNotBeatiful/chromedriver'
# driver = webdriver.Chrome(executable_path=executable_path)

driver.maximize_window()
chrome_options = Options()
a = []
driver.get(
    'https://www.wildberries.by/catalog/0/search.aspx?sort=popular&search=%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8+nike')  # main link
try:
    f__element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-card__main")))  # w8 while needed class download
    # add "except" for exclude errors
finally:
    info = {}  # create dict for save parsing info
    sneaker = driver.find_elements(By.CLASS_NAME, "product-card__main")  # card's with sneakers
    # can we write it to CSV format not txt? it will be better
    file__parser = open('info.txt', 'w')  # open/create file...

    for sn in sneaker:  # get href sneakers and add in a[]
        a.append(sn.get_attribute('href'))
        print(a)

    for price__link in a:  # get link each sneaker..
        time.sleep(2)  # for more understandable, what is happening on the page
        driver.get(price__link)
        info['Ссылка на товар '] = price__link  # terminal view...
        file__parser.write("Link of sneakers : " + price__link)  # add in file link of each sneakers

        for price in driver.find_elements(By.CLASS_NAME, 'price-block__final-price'):  # price
            info['Цена товара '] = price.text  # terminal view...
            file__parser.write("Price : " + price.text)

        for art in driver.find_elements(By.ID, 'productNmId'):  # articul
            info['Артикул товара '] = art.text  # terminal view...
            file__parser.write("Art. : " + art.text + '\n')
            # print(info)

        print(price__link)
        # in price__link variable we have just link for item, where are the price, article etc?
    file__parser.close()  # close file


# here we need to close the browser

"""response = requests.get(price__link)
soup = BeautifulSoup (response.content,'lxml')
print(response.status_code)
time.sleep(5)
price = soup.find('ins')
print(price)"""
