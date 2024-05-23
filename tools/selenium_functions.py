import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Initialize Selenium WebDriver
def create_web_agent():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver

# Open URL
def open_url(driver, url):
    driver.get(url)
    time.sleep(3)

# Click element based on selector
def click_element(driver, by, value):
    element = driver.find_element(by, value)
    element.click()
    time.sleep(2)

# Type text into input field with a natural delay
def type_text(driver, by, value, text, delay=0.1):
    input_field = driver.find_element(by, value)
    input_field.clear()
    for char in text:
        input_field.send_keys(char)
        time.sleep(delay)

# Handle multi-step tasks
def handle_task(driver, steps):
    for step in steps:
        action = step.get("action")
        by = step.get("by")
        value = step.get("value")
        text = step.get("text", "")
        if action == "click":
            click_element(driver, by, value)
        elif action == "type":
            type_text(driver, by, value, text)

# Clean HTML representation of the DOM
def get_clean_html(driver):
    return driver.execute_script("return document.documentElement.outerHTML;")

# Close browser
def close_browser(driver):
    driver.quit()


if __name__ == "__main__":
    # Create web agent
    print("Creating web agent...")
    driver = create_web_agent()
    print("Web agent created successfully!")
    open_url(driver, "https://www.google.com/")
    
   