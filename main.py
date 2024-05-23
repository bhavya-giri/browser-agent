from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import FunctionCallingAgentWorker
from config import config
from tools.tools import *

create_web_agent_tool()

llm = OpenAI(model='gpt-4o',api_key=config.OPENAI_API_KEY)

agent_worker = FunctionCallingAgentWorker.from_tools(
    [
        open_url_tool, click_element_tool,
        type_text_tool, handle_task_tool, get_clean_html_tool,
        close_browser_tool
    ],
    llm=llm,
    verbose=True,
    allow_parallel_tool_calls=True,
)
agent = agent_worker.as_agent()

if __name__ == "__main__":
    response = agent.chat(f"open url, 'https://www.google.com'")
    print(response)
