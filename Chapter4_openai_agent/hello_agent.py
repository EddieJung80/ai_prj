import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

from agents import Agent, Runner

hello_agent = Agent(name="Assistant", model="gpt-5-mini", 
              instructions="You are a helpful assistant. your mission is to say 'Hello, World!'."
              )

result = Runner.run_sync(hello_agent, "Say hello in french & Japanese.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.