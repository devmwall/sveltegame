from fastapi import FastAPI
from ollama import chat
from ollama import ChatResponse
import config
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    print("Request incoming!");
    response: ChatResponse = chat(model='llama3.2:3b', messages=[
      {
        'role': 'user',
        'content': config.ollamaPrompt,
      },
    ])

   
    print(response['message']['content'])

    # or access fields directly from the response object
    print(response.message.content)
    return {"message": json.loads(response['message']['content'])}

# To run the application:
# Save this script as `main.py` and use the following command:
# uvicorn main:app --reload
# This will start the server on http://127.0.0.1:8000
