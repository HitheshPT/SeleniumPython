from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
class loginLRES:
    def login(self):
        driver.get('https://genesis.qa.lrescorp.com/')
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, 'UserName').send_keys('KatalonTestUser')
        driver.find_element(By.ID, 'Password').send_keys('Welcome1!')
        driver.find_element(by=By.XPATH, value='//button[normalize-space()="Login"]').click()
        driver.implicitly_wait(5)
        orders = driver.find_element(by=By.XPATH, value='//span[normalize-space()="Orders"]')
        createNewOrder = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Create New Order']")
        driver.implicitly_wait(5)

        #Mouse Over Orders
        actions = ActionChains(driver)
        driver.implicitly_wait(5)
        actions.move_to_element(orders).move_to_element(createNewOrder).click(createNewOrder).perform()

        #Select clients from the dropdown.
        clientDropDown = driver.find_element(by=By.XPATH, value="//select[@id='OrderItemEdit_ClientID']")
        clientSelect = Select(clientDropDown)
        available_options = clientSelect.options
        for x in available_options:
            if x.text == "DMD_VSA_TC2 (ID #444796)":
                clientSelect.select_by_visible_text("DMD_VSA_TC2 (ID #444796)")
                print("Client is found")
                break
            else:
                print("Client is not found")


login = loginLRES()
login.login()