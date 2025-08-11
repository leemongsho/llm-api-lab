import os
import google.generativeai as genai 
"""Make sure to run the following 2 commands in your terminal:
pip install -q -U google-genai
pip install google-generativeai
Also make sure your python is at least v3.9 or above
"""

# This is the correct way to configure your API key.
# It automatically picks up the GEMINI_API_KEY environment variable.
genai.configure(api_key=os.environ["YOUR_API_KEY"]) #Insert your environment Gemini API Key

# You then directly create an instance of the model you want to use.
model = genai.GenerativeModel('gemini-2.5-flash')

# User prompt
user_prompt = "Describe in 100 words or less the key features of gemini-2.5-flash"

# You can now use the model instance to generate content.
response = model.generate_content(user_prompt)
print(response.text)