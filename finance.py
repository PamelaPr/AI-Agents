from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools


from dotenv import load_dotenv

load_dotenv()

def build_agent():    
    return Agent(
    tools=[YFinanceTools(),DuckDuckGoTools()],
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Use the given tools when required.Format your response using markdown and use tables to display data where possible."],
    markdown=True,
)
openai_agent = build_agent()


openai_agent.print_response("Share the NVDA stock price and analyst recommendations.")