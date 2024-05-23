import time
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
import json

# Global WebDriver instance
global_driver: Optional[WebDriver] = None



def create_web_agent() -> str:
    """
    Creates and initializes a new Selenium WebDriver instance.

    Returns:
        str: A message indicating that the WebDriver has been created.
    """
    global global_driver
    if global_driver is None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        global_driver = webdriver.Chrome(options=options)  
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
    try:
        global_driver.get(url)
        return "URL opened."
    except WebDriverException as e:
        return f"Error opening URL: {str(e)}"

def click_element_tool(by: str, value: str) -> bool:
    """
    Attempts to click an element on the page given its locating strategy and value.

    Args:
        by (str): The locating strategy to use (e.g., By.ID, By.NAME).
        value (str): The value of the attribute to locate the element.

    Returns:
        bool: True if the element was found and clicked, False otherwise.
    """
    global global_driver
    if global_driver is None:
        print("Web agent is not initialized.")
        return False

    print(f"Attempting to click element with {by} = {value}")
    try:
        # Use WebDriverWait to wait until the element is clickable
        element = WebDriverWait(global_driver, 10).until(
            EC.element_to_be_clickable((By.__dict__[by.upper()], value))
        )
        element.click()
        print("Element clicked.")
        return True
    except NoSuchElementException:
        print(f"Element not found: {by} = {value}")
        return False
    except TimeoutException:
        print(f"Timeout waiting for element to be clickable: {by} = {value}")
        return False
    except WebDriverException as e:
        print(f"Error clicking element: {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False
    
def press_enter_tool(by: str, value: str) -> bool:
    """
    Simulates pressing the Enter key on an element identified by the specified locating strategy and value.

    Args:
        by (str): The locating strategy to use (e.g., By.ID, By.NAME).
        value (str): The value of the attribute to locate the element.

    Returns:
        bool: True if the element was found and Enter was pressed, False otherwise.
    """
    global global_driver
    if global_driver is None:
        print("Web agent is not initialized.")
        return False

    print(f"Attempting to press Enter on element with {by} = {value}")
    try:
        # Use WebDriverWait to wait until the element is present and interactable
        element = WebDriverWait(global_driver, 10).until(
            EC.presence_of_element_located((By.__dict__[by.upper()], value))
        )
        element.send_keys(Keys.RETURN)
        print("Enter key pressed.")
        return True
    except NoSuchElementException:
        print(f"Element not found: {by} = {value}")
        return False
    except TimeoutException:
        print(f"Timeout waiting for element to be interactable: {by} = {value}")
        return False
    except WebDriverException as e:
        print(f"Error pressing Enter on element: {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False

def press_tab_tool(by: str, value: str) -> bool:
    """
    Simulates pressing the Tab key on an element identified by the specified locating strategy and value.

    Args:
        by (str): The locating strategy to use (e.g., By.ID, By.NAME).
        value (str): The value of the attribute to locate the element.

    Returns:
        bool: True if the element was found and Tab was pressed, False otherwise.
    """
    global global_driver
    if global_driver is None:
        print("Web agent is not initialized.")
        return False

    print(f"Attempting to press Tab on element with {by} = {value}")
    try:
        # Use WebDriverWait to wait until the element is present and interactable
        element = WebDriverWait(global_driver, 10).until(
            EC.presence_of_element_located((By.__dict__[by.upper()], value))
        )
        element.send_keys(Keys.TAB)
        print("Tab key pressed.")
        return True
    except NoSuchElementException:
        print(f"Element not found: {by} = {value}")
        return False
    except TimeoutException:
        print(f"Timeout waiting for element to be interactable: {by} = {value}")
        return False
    except WebDriverException as e:
        print(f"Error pressing Tab on element: {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False

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
    except NoSuchElementException:
        return f"Element not found: {by}, {value}"
    except TimeoutException:
        return f"Timeout waiting for element: {by}, {value}"
    except WebDriverException as e:
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

def wait_for_page_load(timeout: int = 10) -> str:
    """
    Waits for the page to fully load.

    Args:
        timeout (int): The maximum time to wait for the page to load, in seconds. Default is 10 seconds.

    Returns:
        str: A message indicating whether the page has fully loaded.
    """
    global global_driver
    if global_driver is None:
        return "Web agent is not initialized."

    try:
        WebDriverWait(global_driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        return "Page loaded."
    except TimeoutException:
        return "Failed to load the page within the given time."
    

def get_clean_html_tool() -> str:
    """
    Cleans and returns the HTML DOM structure of the page as a JSON string.

    Returns:
        str:  The cleaned HTML DOM structure as a JSON string.
    """
    load_status = wait_for_page_load()
    if load_status != "Page loaded.":
        return load_status

    global global_driver
    if global_driver is None:
        return "Web agent is not initialized."
    
    def clean_text(text: str) -> str:
        return ' '.join(text.split())

    def get_readable_attributes(element: webdriver.remote.webelement.WebElement) -> Dict[str, str]:
        readable_attributes = [
            'id', 'class', 'title', 'alt', 'href', 'placeholder', 'label',
            'value', 'caption', 'summary', 'aria-label', 'aria-describedby',
            'datetime', 'download', 'selected', 'checked', 'type'
        ]
        attributes = {}
        for attr in readable_attributes:
            if element.get_attribute(attr):
                attributes[attr] = element.get_attribute(attr)
        return attributes
    
    def traverse_element(element: webdriver.remote.webelement.WebElement) -> Dict[str, Any]:
        node_name = element.tag_name.lower()
        node_value = clean_text(element.get_attribute('innerText')) if element.text else None
        attributes = get_readable_attributes(element)
        children = [traverse_element(child) for child in element.find_elements(By.XPATH, './*')]
        return {
            'nodeName': node_name,
            'nodeValue': node_value,
            'attributes': attributes,
            'children': children
        }
    try:
        dom_structure = traverse_element(global_driver.find_element(By.TAG_NAME, 'body'))
        return json.dumps(dom_structure, indent=2)
    except WebDriverException as e:
        return f"Error retrieving page source: {str(e)}"

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