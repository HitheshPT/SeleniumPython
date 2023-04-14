from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
class mouseHover:
    def mouse(self):
        driver.get('https://genesis.qa.lrescorp.com/')
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, 'UserName').send_keys('KatalonTestUser')
        driver.find_element(By.ID, 'Password').send_keys('Welcome1!')
        driver.find_element(By.XPATH, '//button[normalize-space()="Login"]').click()
        driver.implicitly_wait(5)
        orders = driver.find_element(By.XPATH, '//span[normalize-space()="Orders"]')
        createNewOrder = driver.find_element(By.XPATH, "//span[normalize-space()='Create New Order']")
        driver.implicitly_wait(5)

        #Mouse Over Orders
        actions = ActionChains(driver)
        driver.implicitly_wait(5)
        actions.move_to_element(orders).move_to_element(createNewOrder).click(createNewOrder).perform()

mH = mouseHover()
mH.mouse()