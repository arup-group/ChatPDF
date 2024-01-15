from langchain.vectorstores.chroma import Chroma
from langchain.chat_models import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv


def make_chain():
    model = ChatOpenAI(
        model_name="gpt-3.5-turbo-16k", # you can use any model
        temperature="0",
        # verbose=True 
    )
    embedding = OpenAIEmbeddings()

    vector_store = Chroma(
        collection_name="AASHTO", # has to match the collection name used in ingest.py
        embedding_function=embedding,
        persist_directory="files/data/AASHTO",  # has to match the persist directory used in ingest.py
    )

    return ConversationalRetrievalChain.from_llm(
        model,
        retriever=vector_store.as_retriever(),
        return_source_documents=True,
        #verbose=True,
    )
if __name__ == "__main__":
    load_dotenv()

    chain = make_chain()
    chat_history = []

    while True:
        print()
        question = input("Question: ")
        
        # Check if the input is 'end' to terminate the conversation
        if question.lower() == "end":
            print("Ending conversation.")
            break
        

        # Generate answer
        response = chain({"question": question, "chat_history": chat_history})

        # Retrieve answer
        answer = response["answer"]
        source = response["source_documents"]
        chat_history.append(HumanMessage(content=question))
        chat_history.append(AIMessage(content=answer))

        # Display answer
        print(f"Answer: {answer}")
        print("\n\nSources:\n")
        for document in source:
            print(f"Page: {document.metadata['page_number']}")
            print(f"Text chunk: {document.page_content[:160]}...\n")

       
        