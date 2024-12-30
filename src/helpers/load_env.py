def load_env():
  import os
  from dotenv import load_dotenv

  load_dotenv(override=True)
  print(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

