from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

        # Set the value of the input field to "test"
        input_field.send_keys("test")

        # Allow some time for the value to be set (you might need to adjust this)
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
