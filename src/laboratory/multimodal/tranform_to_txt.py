from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import HumanMessage
from src.helpers.load_env import load_env
load_env()

def transform_to_txt(image_path: str):

  model = ChatVertexAI(
    model_name="gemini-1.5-flash-002", temperature=0, max_retries=2
  )

  text_message = {
    "type": "text",
    "text": """Please extract all text from this document and format it in a clean, structured way:
1. Maintain the original language of the document ( dont translate it )
2. Preserve the hierarchical structure (titles, subtitles, body text)
3. Keep text blocks together logically
4. Remove any redundant or repeated text
5. Maintain proper spacing and line breaks
6. Ignore decorative elements or non-textual content
7. Present the text in a clear, readable format

Format the output as continuous text, with clear paragraph breaks where appropriate."""
  }

  media_message = {
    "type": "media",
    "file_uri": image_path, # gs bucket file
    "mime_type": "application/pdf"
  }

  response = model.invoke([HumanMessage(content=[text_message, media_message])])

  return response.content

if __name__ == "__main__":

  print(transform_to_txt("gs://bewe-lite-docsearch-test/capitanBarbas_id/capitan_barbas.pdf"))
