from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time



def main_page(driver):
    form_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Page Scroll']"))
    )
    form_button.click()
    time.sleep(3)

def page_scroll(driver):
    page_height = driver.execute_script("return document.body.scrollHeight")
    scroll_speed = 500
    scroll_iteration=int(page_height/scroll_speed)

    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(3)

    full_name=driver.find_element(By.ID, "name")
    date=driver.find_element(By.ID, "date")

    full_name.send_keys("John Doe")
    date.send_keys("04/14/2026")

def main():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    driver.maximize_window()
    main_page(driver)
    page_scroll(driver)
    driver.quit()

if __name__ == "__main__":
    main()