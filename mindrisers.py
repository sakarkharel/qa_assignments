from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time


def main_page(driver):
    form_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/contact-us']"))
    )
    form_button.click()

def form_fill(driver):
    name = driver.find_element(by=By.NAME, value = "name")
    name.send_keys("ankit")

    email = driver.find_element(by=By.NAME, value = "email")
    email.send_keys("hello@gmail.com")

    phone = driver.find_element(by=By.NAME, value = "mobile_no")
    phone.send_keys("9800020202")

    subject = driver.find_element(by=By.NAME, value = "subject")
    subject.send_keys("Class Timing")
    
    queries = driver.find_element(by=By.NAME, value = "message")
    queries.send_keys("I hope this message finds you well."
                   "Would it be possible to get information on the schedule for the upcoming QA classes?"
                    " I would greatly appreciate any details you could share at your earliest convenience. Thank you!")
    time.sleep(4)



def main():
    driver = webdriver.Chrome()
    driver.get("https://www.mindrisers.com.np/")
    driver.maximize_window()
    main_page(driver)
    form_fill(driver)
    driver.quit()


if __name__ == "__main__":
    main()