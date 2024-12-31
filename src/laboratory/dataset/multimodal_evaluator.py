from langchain_google_vertexai import ChatVertexAI
from pydantic import BaseModel, Field
from src.helpers.load_env import load_env
from langsmith import Client
from src.laboratory.multimodal.image_analyzer import analyze_image_content_callback
from langchain_core.messages import SystemMessage, HumanMessage

load_env()
client = Client()

def any_evaluator(outputs: dict, attachments: dict, reference_outputs: dict) -> dict:
  return {"key": "correct", "score": 0.4}


def image_content_evaluator(outputs: dict, attachments: dict, reference_outputs: dict) -> dict:
  print("\n\noutputs", outputs)
  print("\n\nattachments", attachments)
  print("\n\nreference_outputs", reference_outputs)
  instructions = """
  Does the description of the following image match the content of the image?
  Please carefuly review the image and the description to determine if the descriptios is valid.
  """

  class Response(BaseModel):
    is_valid: bool = Field(
        description="Whether the description matches the image content"
    )

  system_message = SystemMessage(content=instructions)
  text_message = {"type": "text", "text": outputs["description"]}
  image_url = attachments["file_1"]["presigned_url"]
  media_message = {
      "type": "image_url",
      # "image_url": {"url": image_to_base64(attachments["image"])}, # could be a base64 image or a file_uri
      "image_url": {"url": image_url},
  }

  messages = [system_message, HumanMessage(content=[text_message, media_message])]

  model = ChatVertexAI(
    model_name="gemini-1.5-flash-002",
    temperature=0.1,
  )

  model_json_output = model.with_structured_output(Response)

  response = model_json_output.invoke(messages)
  return [
    {"key": "validation", "score": 1 if response.is_valid else 0},
    {"key": "test", "score": 0.7}
  ]


def evaluate_dataset(dataset_id: str):

  # Note: Flow execution:
  # 1. First calls target_function with inputs and attachments ( params of target_function)
  # 2. target_function response is saved as outputs and passed to evaluator along with attachments and reference_outputs

  client.evaluate(
    analyze_image_content_callback,
    data=dataset_id,
    evaluators=[image_content_evaluator, any_evaluator],
    experiment_prefix="multimodal_evaluation"
  )




if __name__ == "__main__":
  dataset_id = "3657e79f-6755-4481-a748-b77c5f2af575"
  evaluate_dataset(dataset_id)
