from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time



def main_page(driver):
    form_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Switch Window']"))
    )
    form_button.click()
    time.sleep(3)

def open_new_tab(driver):
    new_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='new-tab-button']"))
    )
    new_tab.click()
    time.sleep(3)



# Alert chai visible vako chaina 

def open_alert(driver):
    new_alert = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='alert-button']"))
    )
    new_alert.click()
    time.sleep(7)

def main():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    driver.maximize_window()
    main_page(driver)
    open_new_tab(driver)
    driver.quit()

if __name__ == "__main__":
    main()