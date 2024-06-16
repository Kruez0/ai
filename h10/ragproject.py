import os
from langchain import hub

from langchain_core.messages import AIMessage, HumanMessage 
from langchain.agents import initialize_agent, AgentType, AgentExecutor, create_tool_calling_agent
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.tools.tavily_search import TavilySearchResults

os.environ["TAVILY_API_KEY"] = "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"
tools = [TavilySearchResults(max_results=1)]

llm = ChatGroq(
    temperature=1,
    groq_api_key="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",
    model_name="mixtral-8x7b-32768"
)


sys_prompt = """
You run in a loop of Thought, Action, Observation.
At the end of the loop you output an Answer.
Use Thought to describe your thoughts about the question you have been asked.
Use Action to run one of the actions available to you.
Observation will be the result of running those actions.

Example1:

Question: What is the capital of Australia?
Thought: I can look up Australia on Google.
Action: call_google: Australia

You will be called again with this:

Observation: Australia is a country. The capital is Canberra.

You then output:

Answer: The capital of Australia is Canberra.
""".strip()

prompt = ChatPromptTemplate.from_messages([
    ("system", sys_prompt),
    ("human", "{input}"),  
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.invoke({"input": "What is the most delicious food in Kinmen?"})
