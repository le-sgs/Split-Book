from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def scrape_train_data(train_number, boarding_station_code, journey_date):
    try:
        # No need to specify the geckodriver_path when the path to geckodriver is in the system's PATH
        driver = webdriver.Firefox()

        # Navigate to the IRCTC website
        driver.get("https://www.irctc.co.in/online-charts/")

        # Fill in the train number
        input_train_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "react-select-4-input")))
        input_train_number.send_keys(train_number)
        input_train_number.send_keys(Keys.RETURN)
        time.sleep(2)

        # Fill in the journey date
        input_date_picker = driver.find_element(By.XPATH, "//input[@type='text' and @readonly]")
        driver.execute_script(f"arguments[0].value = '{journey_date}';", input_date_picker)
        time.sleep(1)

        # Fill in the boarding station
        input_boarding_station = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "react-select-5-input")))
        input_boarding_station.send_keys(boarding_station_code)
        input_boarding_station.send_keys(Keys.RETURN)
        time.sleep(2)

        # Click the "Get Train Chart" button
        element_text = "Get Train Chart"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{element_text}']"))).click()

    except Exception as e:
        # Handle exceptions, you might want to log the exception details
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the browser window, this will be executed regardless of whether an exception occurred
        if 'driver' in locals():
            driver.quit()

# Example usage
scrape_train_data("12081", "CLT", "26-12-2023")
