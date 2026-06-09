import json
from pathlib import Path
from pypdf import PdfReader

chunk_size = 250 #words
chunk_overlap = 40 #words

DOCUMENTS_DIR = Path("/Users/manish/gitspace/AIRoadmap/documents")
DATA_DIR = Path("/Users/manish/gitspace/AIRoadmap/week2/data")
CHUNKS_FILE = DATA_DIR / "chunks.json"

chunk_output = {
    "chunk_id": "ecommerce_usecases.md::chunk_1",
    "source": "ecommerce_usecases.md",
    "text": "WebEngage helps ecommerce brands..."
  }

def split_text_into_word_chunks(filename, page, text) -> list[dict]: 
    chunks = []
    # Split the text into individual words by whitespace
    words = text.split()
    
    # Loop through the list of words, skipping ahead by the chunk size
    for i in range(0, len(words), chunk_size-chunk_overlap):
        # Slice the list to get the current chunk of words
        chunk_words = words[i : i + chunk_size]
        
        # Rejoin the chunked words into a readable sentence
        chunk_text = " ".join(chunk_words)
        chunk_obj = dict()
        chunk_obj['chunk_id'] = f"{filename} :: {page} :: {i}"
        chunk_obj['source'] = filename
        chunk_obj['text'] = chunk_text
        chunks.append(chunk_obj)
    return chunks    

def read_pdf(dir_path):
    all_chunks = []
    
    # Find all files ending in .pdf (case-insensitive)
    pdf_files = list(dir_path.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in this directory.")
        return

    for file_path in pdf_files:
        # Initialize the PDF reader object
        reader = PdfReader(file_path)
        print(file_path.name)
        
        # Print total number of pages
        print(f"Total Pages: {len(reader.pages)}")
        print("-" * 30)
        
        # Iterate through each page and extract text
        for index, page in enumerate(reader.pages):
            text = page.extract_text()
            chunks = split_text_into_word_chunks(file_path.name, index, text)
            if(len(chunks) > 0) :
                all_chunks.extend(chunks)
    
    CHUNKS_FILE.write_text(
        json.dumps(all_chunks, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"Saved {len(chunks)} chunks to {CHUNKS_FILE}")

# Run the function with your PDF filename
read_pdf(DOCUMENTS_DIR)