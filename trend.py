import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def get_google_trends():

    driver_path = "C:/Users/shubh/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
    service = Service(driver_path)

    # Set up the Selenium WebDriver
    driver = webdriver.Chrome(service=service)

    url = "https://trends.google.com/trends/trendingsearches/daily"

    # Open the page in the browser
    driver.get(url)
    # Wait for the page to load
    driver.implicitly_wait(10)
    response = requests.get(url)
    soup = BeautifulSoup(driver.page_source,'html.parser')

    # Extract trending topics
    trends = soup.find_all('div',class_="mZ3RIc")
    trending_topics = [trend.text.strip() for trend in trends[:1]] # Top 1 trends
    return trending_topics
