from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

load_dotenv()

app = Flask(__name__)

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

embedding = download_embeddings()
index_name = "medical-chatbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name = index_name,
    embedding = embedding
)

chatModel = ChatOpenAI(
    model = "gpt-4o"
)

retriver = docsearch.as_retriever(
    search_type = "similarity",
    search_kwargs = {"k":3})

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriver, question_answer_chain)


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods = ["GET","POST"])
def chat():
    msg = request.form['msg']
    input = msg
    print("User Input: ", input)    
    responser = rag_chain.invoke({"input": input})
    print("Response: ", responser["answer"])
    return str(responser["answer"])




if __name__ == '__main__':
    app.run(host = "0.0.0.0", port  = 8080,debug=True)