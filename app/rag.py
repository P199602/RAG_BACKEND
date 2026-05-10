from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_chroma import Chroma

import os


CHROMA_DB_DIR = "app/chroma_db"


# Multilingual embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)


def save_pdf_to_db(pdf_path, filename):

    print("Loading PDF...")

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    print("PDF Loaded")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = text_splitter.split_documents(documents)

    print("Chunks Created:", len(docs))

    # add metadata
    for doc in docs:

        doc.metadata["source"] = filename

    print("Creating Embeddings...")

    vectorstore = Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embeddings,
        collection_name="pdf_collection"
    )

    vectorstore.add_documents(docs)

    print("Embeddings Stored Successfully")

    return "PDF Stored Successfully"



def search_pdf(question):

    vectorstore = Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embeddings,
        collection_name="pdf_collection"
    )

    docs = vectorstore.similarity_search(
        question,
        k=5
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context



def delete_pdf_from_db(filename):

    vectorstore = Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embeddings,
        collection_name="pdf_collection"
    )

    vectorstore.delete(
        where={
            "source": filename
        }
    )

    return "PDF Deleted"