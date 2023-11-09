import os
from langchain import HuggingFacePipeline, PromptTemplate
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from pdf2image import convert_from_path
import torch


DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
PDF_FILE_PATH = "media"


def makeEmbedding():
    loader = PyPDFDirectoryLoader(PDF_FILE_PATH)
    docs = loader.load()
    embeddings = HuggingFaceInstructEmbeddings(
        model_name="hkunlp/instructor-large", model_kwargs={"device": DEVICE}
    )
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
    texts = text_splitter.split_documents(docs)
    db = Chroma.from_documents(texts, embeddings, persist_directory="db")
    return "all pdf's embedding has stored in the chromaDB"