from llama_index.core.tools import FunctionTool
from tools import functions

open_url_tool = FunctionTool.from_defaults(fn=functions.open_url_tool)
click_element_tool = FunctionTool.from_defaults(fn=functions.click_element_tool)
type_text_tool = FunctionTool.from_defaults(fn=functions.type_text_tool)
handle_task_tool = FunctionTool.from_defaults(fn=functions.handle_task_tool)
get_clean_html_tool = FunctionTool.from_defaults(fn=functions.get_clean_html_tool)
close_browser_tool = FunctionTool.from_defaults(fn=functions.close_browser_tool)