from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time


def main_page(driver):
    form_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Modal']"))
    )
    form_button.click()
    time.sleep(5)

def form(driver):
    modal_button = driver.find_element(By.XPATH, "//button[@id='modal-button']")
    modal_button.click()

    time.sleep(5)

    ok_button = driver.find_element(By.ID, "ok-button")
    ok_button.click()


    time.sleep(5)



def main():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    driver.maximize_window()
    main_page(driver)
    form(driver)
    driver.quit()


if __name__ == "__main__":
    main()