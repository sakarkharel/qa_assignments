from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time


def main_page(driver):
    form_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Autocomplete']"))
    )
    form_button.click()


def form(driver):
    address = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "autocomplete"))
    )
    address.send_keys("Bhaktapur")

    street_address = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "street_number"))
    )
    street_address.send_keys("9123")

    street_address2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "route"))
    )
    street_address2.send_keys("madan bhandari marga")

    city = driver.find_element(By.ID, "locality")
    city.send_keys("Gatthaghar")

    state = driver.find_element(By.ID, "administrative_area_level_1")
    state.send_keys("Bagmati")

    zipcode = driver.find_element(By.ID, "postal_code")
    zipcode.send_keys("162519")

    country = driver.find_element(By.ID, "country")
    country.send_keys("Bagmati")

    time.sleep(7)



def main():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    driver.maximize_window()
    main_page(driver)
    form(driver)
    driver.quit()


if __name__ == "__main__":
    main()