from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from dotenv import load_dotenv

load_dotenv()


@tool
def get_email_address(name: str) -> str:
    """get email address given contact name"""
    if name == "mosab":
        return "najeebmosab@gmail.com"
    elif name == "talal":
        return "talal@gmail.com"
    else:
        return "no contact found"


@tool
def sent_email(text: str, email: str):
    """send an email to a specific email address with the content of text"""
    print("sent email")


# Get the prompt to use - you can modify this!
tools = [get_email_address, sent_email]
prompt = hub.pull("hwchase17/openai-functions-agent")
prompt.messages

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.invoke(
    {"input": "I want an email to be sent to mosab, to meet me on sunday,"})
