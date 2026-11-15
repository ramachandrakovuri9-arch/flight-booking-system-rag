import os
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def run_chatbot():
    print("\n🤖 Initializing AI Flight & Policy Assistant...")
    
    # Check if vector DB exists
    if not os.path.exists("./chroma_db"):
        print("❌ Vector database not found! Please run python rag.py first.")
        return

    # Load embeddings and existing vector store
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    
    print("\n✈️ AI Assistant is ready! Ask me anything about flights or airline policies.")
    print("Type 'exit' or 'quit' to return to the main menu.\n")
    
    while True:
        query = input("You: ").strip()
        if query.lower() in ["exit", "quit", "back"]:
            print("Exiting AI Assistant. Returning to main menu...")
            break
        
        if not query:
            continue
            
        # Retrieve relevant context from ChromaDB
        docs = vectorstore.similarity_search(query, k=3)
        
        print("\n🤖 AI Assistant:")
        if docs:
            print(f"Based on our flight records and policies:")
            for i, doc in enumerate(docs, 1):
                source = doc.metadata.get("source", "Unknown")
                print(f"\n[Source {i} - {source}]:")
                print(doc.page_content.strip())
        else:
            print("I couldn't find any specific information related to your query.")
        print("-" * 50)

if __name__ == "__main__":
    run_chatbot()