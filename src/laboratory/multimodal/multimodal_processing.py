from src.helpers.load_env import load_env
from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
load_env()

model = ChatVertexAI(
  model_name="gemini-1.5-flash-002",
  temperature=0.1,
)


image_url = "https://i.insider.com/5484d9d1eab8ea3017b17e29?width=700&format=jpeg&auto=webp"


# image_message = {
#     "type": "image_url",
#     "image_url": {"url": image_url},
# }

media_message = {
    "type": "media",
    "file_uri": "gs://dataset_lite/images/images.jpeg",
    "mime_type": "image/jpeg",
}

text_message = {
    "type": "text",
    "text": "What is shown in this image?",
}
# message = HumanMessage(content=[text_message, image_message])s


# message = HumanMessage(
#     content=[image_message, "What is shown in this image?"]
# )

message = HumanMessage(
    # content=[media_message, text_message]
    "hola como estas"
)

print(model.invoke([message]))


# # print(message)
# # print(message2)
# x = ("user", [
#     "What is shown in this image?",
#     {
#         "type": "media",
#         "file_uri": "gs://dataset_lite/images/images.jpeg",
#         "mime_type": "image/jpeg"
#     }
# ])