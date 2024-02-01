from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from dotenv import load_dotenv


from coding_tool import call_coding_agent
from email_agent import call_email_agent
from github_agent import call_github_agent

load_dotenv()

manager_tools = [call_email_agent, call_coding_agent, call_github_agent]
manager_prompt = hub.pull("hwchase17/openai-functions-agent")

manager_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
manager_agent = create_openai_functions_agent(
    manager_llm, manager_tools, manager_prompt)
manager_agent_executor = AgentExecutor(
    agent=manager_agent, tools=manager_tools, verbose=True)

response = manager_agent_executor.invoke(
    {"input": "send a happy birthday email to mosab"})
print(response)
