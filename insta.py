import os
from time import sleep
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def upload_video_to_insta(topic, video_file):

    url ="https://www.instagram.com/"

    # Path to your WebDriver and Chrome profile
    driver_path = "C:/Users/shubh/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
    chrome_profile = "C:/Users/shubh/AppData/Local/Google/Chrome/User Data"

    # Set Chrome options
    options = Options()
    options.add_argument(f"user-data-dir={chrome_profile}")
    service = Service(driver_path)

    # Launch browser with the profile
    driver = webdriver.Chrome(service=service, options=options)

    #open instagram url
    driver.get(url)
    #maximize the chrome window
    driver.maximize_window()
    sleep(7)
  
    driver.find_element(By.XPATH,'//*[@name="username"]').send_keys("reelium_007")
    sleep(3)
    driver.find_element(By.XPATH,'//*[@name="password"]').send_keys("reelium@1234")
    sleep(5)
    driver.find_element(By.XPATH,'//*[contains(text(), "Log in")]').click()
    sleep(5)

    try:
        driver.find_element(By.XPATH,'//*[contains(text(),"Not now")]').click()
    except Exception as err:
        print(err)
    

    driver.find_element(By.XPATH,'//*[contains(text(),"Create")]').click()

    # Wait for the file upload dialog to open
    sleep(10)
    
    try:
        driver.find_element(By.XPATH,'//*[contains(text(),"Select from computer")]').click()
    except Exception as err:
        print(err)
    sleep(6)

    # Simulate typing the file path
    file_path = f"C:\\Users\\shubh\\Downloads\\{video_file}-VEED.mp4"
    pyautogui.write(file_path)
    sleep(5)
    # Simulate pressing "Enter" to select the file
    pyautogui.press("enter")
    sleep(10)

    svg_element = driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Select crop']")
    svg_element.click()
    sleep(7)
    driver.find_element(By.XPATH,'//*[contains(text(),"9:16")]').click()
    sleep(5)
    driver.find_element(By.XPATH,'//*[contains(text(),"Next")]').click()
    sleep(6)
    driver.find_element(By.XPATH,'//*[contains(text(),"Next")]').click()
    sleep(5)
    share_button = driver.find_element(By.XPATH, '//div[contains(@class, "x1i10hfl") and text()="Share"]')
    share_button.click()

    sleep(150)
    driver.quit()
