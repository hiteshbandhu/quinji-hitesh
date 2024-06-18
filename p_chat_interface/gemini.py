import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyCnp6NLlx7Lc0gBfpa6wSfr32eWmrl6pug")

prompt = ""

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

def gemini_answer(prompt:str):
    response = chat_session.send_message(prompt)
    return response.text
