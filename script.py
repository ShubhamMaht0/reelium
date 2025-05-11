from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import requests
import time

def generate_script(topic):
    prompt = (
        f"Write a short and engaging Instagram Reel script about 5 fascinating and unknown facts "
        f"related to {topic}. Include:\n"
        f"- Ensure the tone is fun and energetic.\n"
        f"- A catchy introduction to grab attention.\n"
        f"- Five clearly listed facts.\n"
        f"- A conclusion with a call-to-action, like 'Follow for more!'\n"
    )
    
    # Initialize WebDriver
    driver = webdriver.Chrome()

    url = "https://copilot.microsoft.com/chats/kEZnknsciYLkA1tw2qEsX"

    # Open the page in the browser
    driver.get(url)
    time.sleep(10)
    # Locate the text input area for the script
    script_input = driver.find_element(By.XPATH, '//*[@id="userInput"]')  # Update with the actual XPath
    script_input.send_keys(prompt)
    time.sleep(15)

     # Wait for the page to load
    driver.implicitly_wait(10)
    response = requests.get(url)
    soup = BeautifulSoup(driver.page_source,'html.parser')

    # Extract trending topics
    script = soup.find('div',class_="space-y-3 break-words").text
    clean_script = re.sub(r'[^\x00-\x7F]+', '', script)
    return clean_script




