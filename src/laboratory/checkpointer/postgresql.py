from typing import Literal

from langchain_core.tools import tool
from langchain_google_vertexai import ChatVertexAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.postgres import PostgresSaver
from src.helpers.load_env import load_env
from psycopg_pool import ConnectionPool

load_env()


@tool
def get_weather(city: Literal["nyc", "sf"]):
    """Use this to get weather information."""
    if city == "nyc":
        return "It might be cloudy in nyc"
    elif city == "sf":
        return "It's always sunny in sf"
    else:
        raise AssertionError("Unknown city")


tools = [get_weather]
model = ChatVertexAI(
  model_name="gemini-1.5-flash-002",
  temperature=0.1,
)

def init_checkpointer():
    pool = ConnectionPool(
        conninfo="postgresql://lukita:lukitadb@localhost:5432/postgres",
        max_size=20,
        kwargs={"autocommit": True}
    )

    checkpointer = PostgresSaver(pool)

    graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "1"}}
    res = graph.invoke({"messages": [("human", "cual es mi nombre?")]}, config)
    print(res)


if __name__ == "__main__":
    checkpointer = init_checkpointer()
