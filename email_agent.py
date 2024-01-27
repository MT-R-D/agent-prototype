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
def sent_email(text:str,email:str):
    """send an email to a specific email address with the content of text"""
    print("sent email")


# Get the prompt to use - you can modify this!
email_tools = [get_email_address,sent_email]
email_prompt = hub.pull("hwchase17/openai-functions-agent")


email_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
email_agent = create_openai_functions_agent(email_llm, email_tools,email_prompt)
email_agent_executor = AgentExecutor(agent=email_agent, tools=email_tools, verbose=True)

@tool
def call_email_agent(request:str):
    """send a request to the email handling agent"""
    return email_agent_executor.invoke({"input":request})