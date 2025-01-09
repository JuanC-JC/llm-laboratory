from datetime import datetime
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent


def check_weather(location: str, at_time: datetime | None = None) -> str:
    '''Return the weather forecast for the specified location.'''
    return f"It's always sunny in {location}"

tools = [check_weather]
model = ChatOpenAI(model="gpt-4o")
graph = create_react_agent(model, tools=tools)
inputs = {"messages": [("user", "what is the weather in sf")]}
for s in graph.stream(inputs, stream_mode="values"):
    message = s["messages"][-1]
    if isinstance(message, tuple):
        print(message)
    else:
        message.pretty_print()
('user', 'what is the weather in sf')


# ================================== Ai Message ==================================
# Tool Calls:
# check_weather (call_LUzFvKJRuaWQPeXvBOzwhQOu)
# Call ID: call_LUzFvKJRuaWQPeXvBOzwhQOu
# Args:
#     location: San Francisco
# ================================= Tool Message =================================
# Name: check_weather
# It's always sunny in San Francisco
# ================================== Ai Message ==================================
# The weather in San Francisco is sunny.