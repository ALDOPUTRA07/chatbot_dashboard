from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain import HuggingFacePipeline
from langchain.chains import RetrievalQA
from sentence_transformers import SentenceTransformer
import pandas as pd


from model.config.config import modelPath, model_kwargs, encode_kwargs
from model.processing.data_manager import text_chunk
from model.processing.pipeline_qa import pipeline


def embedding():
    embeddings = HuggingFaceEmbeddings(
            model_name=modelPath,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
    
    return embeddings


def model(question):
    text_chunks = text_chunk()
    embeddings =embedding()

    db = FAISS.from_documents(text_chunks, embeddings)
    
    pipe = pipeline()
    
    retriever = db.as_retriever(search_kwargs={"k": 1})
    docs = retriever.get_relevant_documents(question)

    answer = pipe({
        'context': docs[0],
        'question': question})

    return answer