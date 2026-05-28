from fastapi import FastAPI
from pydantic import BaseModel, Field

try:
    from .LeadExtractionApplication import LeadExtractionApplication
except ImportError:
    from LeadExtractionApplication import LeadExtractionApplication


class LeadExtractionRequest(BaseModel):
    raw_lead_text: str = Field(min_length=1)


app = FastAPI()
lead_extraction_application = LeadExtractionApplication()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/lead/extract")
def extract_lead(request: LeadExtractionRequest):
    result = lead_extraction_application.extract_structured_data(
        request.raw_lead_text,
    )
    return result.model_dump()
