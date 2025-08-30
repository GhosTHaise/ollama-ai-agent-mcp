from praisonaiagents import Agent, MCP

search_agent = Agent(
    instructions="""You help book apartments on Airbnb.""",
    llm="ollama/llama3",
    tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
)

search_agent.start("Search fo Apartments in Antananarivo , Madagascar for 2 nights. 28/04/25 - 30/04/25 for 50 euros per night")