import time
from typing import List, Dict, Any
from pydantic import BaseModel, Field
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Global WebDriver instance
global_driver = None


# Function to create and initialize the WebDriver
def create_web_agent() -> str:
    """
    Creates and initializes a new Selenium WebDriver instance.

    Returns:
        str: A message indicating that the WebDriver has been created.
    """
    global global_driver
    if global_driver is None:
        global_driver = webdriver.Chrome()  # You can use any WebDriver here, e.g., Chrome, Firefox
    return "Web agent created."

def open_url_tool(url: str) -> str:
    """
    Opens a URL in the global Selenium WebDriver instance.

    Args:
        url (str): The URL to open.

    Returns:
        str: A message indicating that the URL has been opened.
    """
    global global_driver
    if global_driver is None:
        return "Web agent is not initialized."
    global_driver.get(url)
    return "URL opened."

def click_element_tool(by: Any, value: str) -> str:
    """
    Clicks an element in the webpage based on the provided selector.

    Args:
        by (Any): The method used to find the element (e.g., By.ID, By.CLASS_NAME).
        value (str): The value of the attribute used for locating the element.

    Returns:
        str: A message indicating that the element has been clicked.
    """
    global global_driver
    if global_driver is None:
        return "Web agent is not initialized."
    try:
        element = WebDriverWait(global_driver, 10).until(
            EC.element_to_be_clickable((by, value))
        )
        global_driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        return "Element clicked."
    except Exception as e:
        return f"Encountered error: {str(e)}"

def type_text_tool(by: Any, value: str, text: str, delay: float = 0.1) -> str:
    """
    Types text into an input field in the webpage with a natural typing delay.

    Args:
        by (Any): The method used to find the input field (e.g., By.ID, By.NAME).
        value (str): The value of the attribute used for locating the input field.
        text (str): The text to type into the input field.
        delay (float, optional): The delay between typing each character. Defaults to 0.1.

    Returns:
        str: A message indicating that the text has been inputted.
    """
    global global_driver
    if global_driver is None:
        return "Web agent is not initialized."
    try:
        element = WebDriverWait(global_driver, 10).until(
            EC.element_to_be_clickable((by, value))
        )
        global_driver.execute_script("arguments[0].scrollIntoView();", element)
        for char in text:
            element.send_keys(char)
            time.sleep(delay)
        return "Text inputted."
    except Exception as e:
        return f"Encountered error: {str(e)}"

def handle_task_tool(steps: List[Dict[str, Any]]) -> str:
    """
    Handles multi-step tasks in the webpage.

    Args:
        steps (List[Dict[str, Any]]): A list of steps to execute, where each step is a dictionary containing
                                       action, by, value, and text keys.

    Returns:
        str: A message indicating that the task has been handled.
    """
    global global_driver
    if global_driver is None:
        return "Web agent is not initialized."
    for step in steps:
        action = step.get("action")
        by = step.get("by")
        value = step.get("value")
        text = step.get("text", "")
        if action == "click":
            click_element_tool(by, value)
        elif action == "type":
            type_text_tool(by, value, text)
    return "Task handled."

def get_clean_html_tool() -> str:
    """
    Retrieves a clean HTML representation of the current DOM in the webpage.

    Returns:
        str: The clean HTML representation of the DOM.
    """
    global global_driver
    if global_driver is None:
        return "Web agent is not initialized."
    return global_driver.page_source

def close_browser_tool() -> str:
    """
    Closes the Selenium WebDriver instance.

    Returns:
        str: A message indicating that the browser has been closed.
    """
    global global_driver
    if global_driver is not None:
        global_driver.quit()
        global_driver = None
        return "Browser closed."
    return "Web agent is not initialized."