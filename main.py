from llama_index.llms.openai import OpenAI
from llama_index.core.agent import FunctionCallingAgentWorker
from config import config
from tools.tools import *
from tools.functions import create_web_agent

create_web_agent()

llm = OpenAI(model='gpt-4o',api_key=config.OPENAI_API_KEY)

agent_worker = FunctionCallingAgentWorker.from_tools(
    [
        open_url_tool, press_enter_tool,press_tab_tool,click_element_tool,
        type_text_tool, handle_task_tool, get_clean_html_tool,
        close_browser_tool
    ],
    llm=llm,
    verbose=True,
    max_function_calls=10,
    allow_parallel_tool_calls=True,
    system_prompt='''You are an interaction agent. You help users with their requests. \
                    You can take a websites DOM and understand what action to take next. The available \
                    actions are "click" and "type". For links and buttons, return click and for inputs, return type.'''
)
agent = agent_worker.as_agent()

if __name__ == "__main__":
    response = agent.chat(f"search on google for lex fridman and andrej karpathy podcast, open the youtube link")
    print(response)
