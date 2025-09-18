from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("a2d92bf0f31b7ec9763b0e55bb3a9f91")  # ✅ Correct usage

@app.get("/")
def read_root():
    return {"message": "Hello from MediMap backend!"}

@app.post("/process")
async def process_transcript(request: Request):
    data = await request.json()
    transcript = data.get("transcript", "I need a dermatologist next Friday in New Haven")

    prompt = f"""
    Extract the medical specialty, date, and location from this request:
    "{transcript}"

    Respond in JSON format like:
    {{
      "specialty": "...",
      "date": "...",
      "location": "..."
    }}
    """
 
 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts structured data from user requests."},
            {"role": "user", "content": prompt}
        ]
    )

    reply = response.choices[0].message.content
    print("OpenAI response:", reply)
    return {"response": reply}
