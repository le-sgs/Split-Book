from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def scrape_train_data(boarding_station, destination_station):
    # Use a try-except block to handle exceptions
    try:
        # No need to specify the geckodriver_path when the path to geckodriver is in the system's PATH
        driver = webdriver.Firefox()

        # Navigate to the IRCTC website
        driver.get("https://www.irctc.co.in/online-charts/")

        # Find the input field by its name
        input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "react-select-4-input")))
        input_field.send_keys("12081")
        input_field.send_keys(Keys.RETURN)
        time.sleep(2)

        # Replace with the actual locator for your date picker input
        date_picker = driver.find_element(By.XPATH, "//input[@type='text' and @readonly]")
        driver.execute_script("arguments[0].value = '26-11-23';", date_picker)
        time.sleep(1)


        input_field2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "react-select-5-input")))
        input_field2.send_keys("CLT")
        input_field2.send_keys(Keys.RETURN)
        time.sleep(2)


        # Use XPath to find the element by its text content
        xpath_expression = "//button[text()='GET TRAIN CHART']"
        get_train_chart_button = driver.find_element(By.XPATH, xpath_expression)

        # Perform a click on the element
        get_train_chart_button.click()
        time.sleep(2)


        # Print the value of the input field (optional, for verification)
        print("Input Field Value:", input_field.get_attribute("value"))

    except Exception as e:
        # Handle exceptions, you might want to log the exception details
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the browser window, this will be executed regardless of whether an exception occurred
        if 'driver' in locals():
            driver.quit()

# Example usage
scrape_train_data("BoardingStation", "DestinationStation")
