import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import pypdf

def build_vector_db():
    docs = []
    
    # 1. Load airline policy PDF safely (with a fallback if the file is empty)
    pdf_path = "./data/airline_policy.pdf"
    if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
        print("Loading airline_policy.pdf...")
        try:
            reader = pypdf.PdfReader(pdf_path)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text and text.strip():
                    docs.append(Document(page_content=text, metadata={"source": "airline_policy.pdf", "page": i+1}))
        except Exception as e:
            print(f"⚠️ Error reading PDF: {e}")
    
    if not docs:
        print("⚠️ airline_policy.pdf is empty. Adding default airline policy text...")
        docs.append(Document(
            page_content="Airline Baggage Policy: Passengers are allowed 1 carry-on bag up to 7kg and 1 checked bag up to 15kg. Cancellation & Refund Policy: Full refund if cancelled 24 hours before departure. No refunds for no-shows.", 
            metadata={"source": "default_airline_policy"}
        ))
    
    # 2. Load flights CSV data
    csv_path = "./data/flights.csv"
    if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
        print("Loading flights.csv...")
        from langchain_community.document_loaders import CSVLoader
        csv_loader = CSVLoader(csv_path)
        docs.extend(csv_loader.load())

    # 3. Split documents into smaller text chunks
    print("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_documents(docs)

    # 4. Initialize lightweight local embeddings
    print("Generating embeddings and saving to ChromaDB...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 5. Store in ChromaDB vector database
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    
    print("✅ Vector database built and persisted successfully in './chroma_db'!")
    return vectorstore

if __name__ == "__main__":
    build_vector_db()