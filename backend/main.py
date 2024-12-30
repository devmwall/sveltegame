from fastapi import FastAPI
from ollama import chat
from ollama import ChatResponse

app = FastAPI()

@app.get("/")
def read_root():
    response: ChatResponse = chat(model='tinyllama', messages=[
      {
        'role': 'user',
        'content': 'Why is the sky blue?',
      },
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)
    return {"message": response.message.content}

# To run the application:
# Save this script as `main.py` and use the following command:
# uvicorn main:app --reload
# This will start the server on http://127.0.0.1:8000
