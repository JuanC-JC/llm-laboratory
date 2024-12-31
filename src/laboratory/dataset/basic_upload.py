from src.helpers.load_env import load_env
from langsmith import Client

load_env()


client = Client()
dataset_id = "2a1cb04d-5572-45f0-a440-9cfbeb3e1e8a"

example_inputs = [
  ("What is the capital of France?", "Paris"),
  ("What is the capital of Germany?", "Berlin"),
  ("What is the capital of Italy?", "Rome"),
  ("What is the capital of Spain?", "Madrid"),
  ("What is the capital of Portugal?", "Lisbon"),
]


for input, output in example_inputs:
  client.create_example(
    dataset_id=dataset_id,
    inputs={"question": input},
    outputs={"answer": output},
    metadata={"source": "test"},
  )
