from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


def main_page(driver):
    form_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='File Upload']"))
    )
    form_button.click()
    time.sleep(3)


def file_upload(driver):
    file_pick = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "file-upload-field"))
    )
    file_pick.send_keys("/home/sakar/Music/tech_projects/qa_automation_formy/orangecat.jpg")
    time.sleep(3)

def reset(driver):
    reset = driver.find_element(*(By.XPATH,"//button[normalize-space()='Reset']"))
    reset.click()
    time.sleep(2)

def main():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    driver.maximize_window()
    main_page(driver)
    file_upload(driver)
    reset(driver)
    driver.quit()


if __name__ == "__main__":
    main()