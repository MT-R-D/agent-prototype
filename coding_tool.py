from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.tools import BaseTool, StructuredTool, tool
from dotenv import load_dotenv

load_dotenv()

prompt_template = PromptTemplate.from_template(
    """Write code in {language} that fulfills the following requirements:
{messages}
-------------------------------
{request}

**Additional notes:**

- {additional_notes}
- Ensure the code is well-formatted, readable, and follows best practices for {language}.
- Prioritize clarity and efficiency in the generated code.
- If any ambiguities or uncertainties arise, provide multiple alternative solutions or ask for clarification.
    """
)
model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt_template | model | output_parser


@tool
def call_coding_agent(language:str,request:str,additional_notes:str):
    """call the coding agent to generate code from a request"""
    return chain.invoke({"language":language,"request":request,"additional_notes":additional_notes})