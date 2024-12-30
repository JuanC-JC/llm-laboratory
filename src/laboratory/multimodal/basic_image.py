from src.helpers.load_env import load_env
from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import HumanMessage
from src.helpers.image_processing import image_to_base64
load_env()

model = ChatVertexAI(
  model_name="gemini-1.5-pro-002",
  temperature=0.1,
)

text_message = {"type": "text", "text": "que ves en esta imagen?"}
media_message = {
    "type": "image_url",
    "image_url": {"url": image_to_base64("/home/juancjc/study/AI/llm-laboratory/files/piri.jpeg")},
}


# for this option, the file must be upload in internet
# media_message = {
#     "type": "media",
#     "file_uri": "gs://dataset_lite/images/images.jpeg",
#     "mime_type": "image/jpeg",
# }

# Get the response content and clean it up
response = model.invoke([HumanMessage(content=[text_message, media_message])])