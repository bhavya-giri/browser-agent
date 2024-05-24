
# Browser-Agent: Agent Orchestration for Surfing

This project provides a set of tools for orchestrating agents that interact with web browsers using Selenium WebDriver and LlamaIndex. The toolkit includes functions to create a web agent, open URLs, click elements, type text and various other tools.




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`




## Run Locally

Clone the project

```bash
  git clone git@github.com:bhavya-giri/browser-agent.git
```

Go to the project directory

```bash
  cd browser-agent
```
Create and activate virtual environment

```bash
   python -m venv .venv
   source .venv/bin/activate
```
Install dependencies

```bash
  pip install -r requirements.txt
```

Run the main.py

```bash
  python main.py
```


## Scope of Improvement

- Indexing specific product's features with metadata of select element
- Parsing and cleaning page_sourse
    ``` python
    def clean_html() -> str:
    """
    Cleans and returns the HTML DOM structure of the page as a JSON string.

    Returns:
        str: The cleaned HTML DOM structure as a JSON string.
    """
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

    body = driver.find_element(By.TAG_NAME, 'body')
    dom_structure = traverse_element(body)
    return json.dumps(dom_structure, indent=2)
    ```
- OCR for elements
- More tools are always welcomed


## License

This project is licensed under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.


