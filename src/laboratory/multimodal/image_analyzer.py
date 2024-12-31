from src.helpers.load_env import load_env
from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import HumanMessage
from src.helpers.image_processing import image_to_base64
from pydantic import BaseModel, Field
from langsmith import traceable


class Response(BaseModel):
    description: str = Field(description="Description of the image content")

# @traceable(
#   name="analyze_image_content",
#   inputs=["image_path", "structured_response"],
#   outputs=["description"],
# )
def analyze_image_content(
    image_path: str, structured_response: bool = False
) -> str | Response:

    model = ChatVertexAI(
        model_name="gemini-1.5-flash-002", temperature=0.1, max_retries=2
    )

    if structured_response:
        model = model.with_structured_output(Response)

    text_message = {"type": "text", "text": "what do you see in this image?"}
    media_message = {
        "type": "image_url",
        "image_url": {"url": image_to_base64(image_path)},
    }

    # for this option, the file must be upload in internet
    # media_message = {
    #     "type": "media",
    #     "file_uri": "gs://dataset_lite/images/images.jpeg",
    #     "mime_type": "image/jpeg",
    # }

    # Get the response content and clean it up
    response = model.invoke([HumanMessage(content=[text_message, media_message])])
    data = response if structured_response else response.content

    # Add debug information
    print(f"Response type: {type(data)}")
    if structured_response:
        print(f"Response fields: {data.model_dump()}")  # Convert to dict if needed
    return data


# @traceable(
#   name="analyze_image_content_callback",
#   inputs=["inputs", "attachments"],
#   outputs=["image_analysis"],
# )
def analyze_image_content_callback(inputs: dict, attachments: dict) -> dict:
    image_path = attachments["file_1"]["presigned_url"]
    image_analysis = analyze_image_content(image_path, structured_response=True)
    return image_analysis.model_dump()


if __name__ == "__main__":
    # load_env()
    image_analysis = analyze_image_content(
        "/home/juancjc/study/AI/llm-laboratory/files/images/piri.jpeg",
        structured_response=True,
    )
    print(image_analysis)
