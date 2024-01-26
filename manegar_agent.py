from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from dotenv import load_dotenv
from coding_tool import call_coding_agent
from email_agent import call_email_agent
from github_agent import call_github_agent
load_dotenv()

manegar_tools = [call_email_agent,call_coding_agent,call_github_agent]
manegar_prompt = hub.pull("hwchase17/openai-functions-agent")


manegar_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
manegar_agent = create_openai_functions_agent(manegar_llm, manegar_tools,manegar_prompt)
manegar_agent_executor = AgentExecutor(agent=manegar_agent, tools=manegar_tools, verbose=True)

response = manegar_agent_executor.invoke({"input":"send email to mosab hi mosab how are you"})
print(response)