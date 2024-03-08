import os
from pathlib import Path

import pandas as pd
from langchain.document_loaders import DataFrameLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_data():
    
    data_folder = Path("data")
    data_path = os.path.join(data_folder, 'data.csv')
    data = pd.read_csv(data_path, header=None, names=['description'])
    data = pd.DataFrame(data)

    return data

def text_chunk():
    data = load_data()
    text_chunks = DataFrameLoader(
        data, page_content_column="description").load_and_split(
        text_splitter=RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=0, length_function=len
            ))
    
    return text_chunks
