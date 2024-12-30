import base64
import httpx

# Function to convert image to base64
def image_to_base64(image_path):
  """
  Convert image to base64 string, supporting both URLs and local files
  Returns the image in base64 format
  """
  try:
    if image_path.startswith(('http://', 'https://')):
      image_data = base64.b64encode(httpx.get(image_path).content).decode("utf-8")
      return f"data:image/jpeg;base64,{image_data}"
    else:
      with open(image_path, 'rb') as image_file:
          base64_data = base64.b64encode(image_file.read()).decode('utf-8')
          return f"data:image/jpeg;base64,{base64_data}"
  except Exception as e:
    print(f"Error processing image: {str(e)}")
    return None