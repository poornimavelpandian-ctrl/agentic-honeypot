from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Agentic Honeypot API")
@app.get("/")
def root():
    return {"status": "Agentic Honeypot API is running"}

API_KEY = "test123"

class ScamInput(BaseModel):
    message: str

@app.post("/honeypot")
def honeypot(
    data: ScamInput,
    x_api_key: str = Header(...)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    response = {
        "status": "scam_detected",
        "extracted_entities": {
            "upi_ids": ["scammer@upi"],
            "phone_numbers": ["+91XXXXXXXXXX"],
            "phishing_links": ["http://fake-link.com"]
        },
        "persona_response": "I am trying to complete the payment. Please wait."
    }
    return response