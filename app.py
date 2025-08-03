from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
import os
import google.api_core.exceptions

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

embeddings = download_hugging_face_embeddings()
index_name = "medical-chatbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})
chatModel = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=GEMINI_API_KEY)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    return render_template('chat.html')

@retry(
    stop=stop_after_attempt(3),  # Retry up to 3 times
    wait=wait_fixed(25),  # Wait 25 seconds between retries (slightly more than 23s)
    retry=retry_if_exception_type(google.api_core.exceptions.ResourceExhausted)  # Retry on quota errors
)
def invoke_rag_chain(msg):
    return rag_chain.invoke({"input": msg})

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    print(f"User: {msg}")
    response = rag_chain.invoke({"input": msg})
    print("Response:", response["answer"])
    return jsonify({"answer": response["answer"]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)