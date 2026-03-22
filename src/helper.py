from pinecone import Pinecone
from pinecone import ServerlessSpec

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings


from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from typing import List
from langchain.schema import Document

from dotenv import load_dotenv
import os
load_dotenv()



def load_pdf_files(data_path):
    loader = DirectoryLoader(
        data_path,
        glob = "*.pdf",
        loader_cls = PyPDFLoader
    )

    documents = loader.load()

    return documents

def filter_to_minimal_docs(docs: List[Document])-> List[Document]:
    """
    given a list of document objects, returns a new list of document objects,
    containing only 'source' and 'page content'
    """
    minimal_docs : List[Document] = []
    
    for doc in docs:
        src = doc.metadata.get('source')
        minimal_docs.append(
            Document(
            page_content = doc.page_content,
            metadata = {"source":src} # follow the structure of "extracted_data"
            )
        )
    return minimal_docs

def text_split(minimal_docs):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 20,
        length_function = len
    )
    texts_chunck = text_splitter.split_documents(minimal_docs)

    return texts_chunck

def download_embeddings():
    """
    Download and return the Huggingface embedding model
    """
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name = model_name
        # model_kwargs = {"device": "cuda" if torch.cuda.is_available() else "cpu"}
    )

    return embeddings
