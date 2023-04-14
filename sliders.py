from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.chrome(ChromeDriverManager.install())

class sliders:
    def slider(self):
        driver.get('https://www.snapdeal.com/products/mens-footwear-sports-shoes?sort=plrty')
