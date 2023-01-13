from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the ChromeOptions class
options = webdriver.ChromeOptions()

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chrome_options=options)

# Navigate to the YouTube homepage
driver.get("https://www.youtube.com/channel/UCqzVqqDAGJTX2Bk_2KOAkag")

# Locate the search bar and enter a query
# search_bar = driver.find_element(By.NAME, "search_query")
# search_bar.send_keys("")

# channel = driver.find_element(By.ID, "endpoint")
# channel.click()
try:
    fullscreen_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.ytp-fullscreen-button.ytp-button"))
    )
    fullscreen_button.click()
    play_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.ytp-play-button.ytp-button"))
    )
    play_button.click()
except Exception as e:
    print(f'Error: {e}')

# Locate the search button and click it
# search_button = driver.find_element(By.ID, "search-icon-legacy")
# search_button.click()

# Close the browser
input("Press Enter to close the browser")
driver.quit()
