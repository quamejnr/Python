import os
from dotenv import load_dotenv


# Initialize dotenv
load_dotenv()

# reading environment variables
django = os.environ.get("DJANGO")
python = os.environ.get("PYTHON")

# printing out
print(django)
print(python)
