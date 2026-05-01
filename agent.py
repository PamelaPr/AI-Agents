from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools


from dotenv import load_dotenv

load_dotenv()

def build_agent():    
    return Agent(
    tools=[DuckDuckGoTools()],
    model=OpenAIResponses(id="gpt-5-mini"),
    instructions="You are a helpful and expert travel agent.",
    markdown=True,
)
openai_agent = build_agent()

openai_agent.print_response("My budget is 1 Lakh Rupees ,should I travel to Goa or Phuket.")