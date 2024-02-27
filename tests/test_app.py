from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.edge.options import Options

@pytest.fixture
def driver():
    # Initialize streamlit in background
    process = subprocess.Popen(["streamlit", "run", "source/app.py"])
    options = Options()
    options.headless = True  # Headless mode False -> Browser remains closed
    driver = webdriver.Edge(options=options)

    # Initialize the WebDriver using GeckoDriver
    driver.set_page_load_timeout(5)
    yield driver

    # Close WebDriver and Streamlit
    driver.quit()
    process.kill()

def test_app_opens(driver):
    '''
    Test if page opens
    '''
    driver.get("http://localhost:8501")
    sleep(2)

def test_check_title(driver):
    '''
    Test if page title is correct
    '''
    driver.get("http://localhost:8501")
    sleep(2)
    page_title = driver.title

    expected_title = "Excel Schema Validator"
    assert page_title == expected_title

