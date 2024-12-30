from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# To run the application:
# Save this script as `main.py` and use the following command:
# uvicorn main:app --reload
# This will start the server on http://127.0.0.1:8000
