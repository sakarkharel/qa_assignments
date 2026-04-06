from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time



def main_page(driver):
    form_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Dropdown']"))
    )
    form_button.click()
    time.sleep(3)

def dropdown(driver):
    dropdown=driver.find_element(By.ID, "dropdownMenuButton")
    dropdown.click()

    select_buttons = driver.find_element(By.XPATH, "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][normalize-space()='Buttons']")
    select_buttons.click()
    time.sleep(5)

def main():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    driver.maximize_window()
    main_page(driver)
    dropdown(driver)
    driver.quit()

if __name__ == "__main__":
    main()