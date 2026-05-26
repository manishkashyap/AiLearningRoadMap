from fastapi import FastAPI
from TextToJsonExtractor import TextToJsonExtractor

app = FastAPI()
extractor = TextToJsonExtractor()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/lead/extract")
def read_item(q: str | None = None):
    return extractor.extract(q)