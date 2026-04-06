from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time



def main_page(driver):
    form_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Key and Mouse Press']"))
    )
    form_button.click()
    time.sleep(3)

def keyboard_mouse(driver):
    full_name=driver.find_element(By.ID, "name")
    button = driver.find_element(By.ID, "button")

    full_name.send_keys("John Doe")
    button.click()

def main():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    driver.maximize_window()
    main_page(driver)
    keyboard_mouse(driver)
    driver.quit()

if __name__ == "__main__":
    main()