from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import requests

def create_video_with_text(script,video_file):

    # Path to your WebDriver and Chrome profile
    driver_path = "C:/Users/shubh/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
    chrome_profile = "C:/Users/shubh/AppData/Local/Google/Chrome/User Data"

    # Set Chrome options
    options = Options()
    options.add_argument(f"user-data-dir={chrome_profile}")
    service = Service(driver_path)

    # Launch browser with the profile
    driver = webdriver.Chrome(service=service, options=options)


    # Open Veed.io AI Reel Generator
    driver.get("https://www.veed.io/")
    #driver.maximize_window()
    # Wait for the page to load 
    time.sleep(15)


    text_to_video = driver.find_element(By.XPATH,'//*[@id="root"]/main/section/div[2]/article/div/div[1]/div[3]/div/div/div[6]/div/p[1]')
    text_to_video.click()
    time.sleep(5)

    # Locate the text input area for the script
    script_input = driver.find_element(By.XPATH, '//*[@id="prompt-step-form"]/div/div[2]/textarea')  # Update with the actual XPath
    script_input.send_keys(script)
    time.sleep(5)

    # Submit the script to generate the video
    generate_button = driver.find_element(By.XPATH, '//*[@id="prompt-step-form"]/div/div[2]/button')  # Update with the actual XPath
    generate_button.click()
    time.sleep(5)

    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[1]/div/header/div[2]/button')  # Update with the actual XPath
    continue_button.click()
    time.sleep(5)

    continue2_button = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[1]/div/header/div[2]/button')  # Update with the actual XPath
    continue2_button.click()

    # Wait for the video to process
    time.sleep(250)  # Adjust this based on processing time


    done_button = driver.find_element(By.XPATH, '//*[contains(text(),"Done")]')  # Update with the actual XPath
    done_button.click()
    time.sleep(5)

    # Locate the download button and click
    export_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[4]/div/button[2]')  # Update with the actual XPath
    export_button.click()
    time.sleep(80)

    edit_name = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Edit Video Name']")
    edit_name.click()
    time.sleep(5)

    driver.implicitly_wait(10)
    name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='@rename-video-modal/input-area']")
    time.sleep(5)
    name_input.send_keys(Keys.CONTROL + 'a')
    name_input.send_keys(Keys.BACKSPACE) 
    name_input.send_keys(video_file)
    time.sleep(3)
    name_input.send_keys(Keys.ENTER)
    time.sleep(5)


    download_button = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div/div[3]/div/div[3]/div/button')
    download_button.click()
    time.sleep(5)

    mp4_download_button = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/button[1]')
    mp4_download_button.click()
    time.sleep(30)

    
    driver.quit()



