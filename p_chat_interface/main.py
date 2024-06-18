from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gemini import gemini_answer

app = FastAPI()

# Allow CORS for your frontend (e.g., localhost:5500)
origins = [
    "http://127.0.0.1:5500",  # Adjust the port if your frontend is served on a different port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/gemini/{prompt}")
def read_root(prompt:str):
    return gemini_answer(prompt)