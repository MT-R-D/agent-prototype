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
def create_repo(name: str):
    """create a repo by name"""
    print(" created a repository ")
    
@tool
def push_repo(name:str,data:str):
    """create new file and push it to repository"""
    print(" created new file ")
# Get the prompt to use - you can modify this!
github_tools = [create_repo,push_repo]
github_prompt = hub.pull("hwchase17/openai-functions-agent")


github_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
github_agent = create_openai_functions_agent(github_llm, github_tools,github_prompt)
github_agent_executor = AgentExecutor(agent=github_agent, tools=github_tools, verbose=True)

@tool
def call_github_agent(request:str):
    """call the github agent to handle a request """
    return github_agent_executor.invoke({"input":request})