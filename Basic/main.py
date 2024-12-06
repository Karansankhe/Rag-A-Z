#Set Environment Vars and Api Keys
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


#environment configuration
import os
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = os.getenv('LANGCHAIN_ENDPOINT')
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGCHAIN_PROJECT')
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['GROQ_API_KEY'] = os.getenv("GROQQ_API_KEY")


####  Overiview ####

from langchain_community.document_loaders import WebBaseLoader #Extracts data from web pages and transforms it into a document format for use in language model workflows.
from langchain_community.vectorstores import FAISS  #A library for fast nearest-neighbor search on high-dimensional vectors, enabling efficient document retrieval based on semantic similarity.
from langchain_community.vectorstores import StrOutputParser #Used for converting outputs into plain strings, ensuring a structured and human-readable format.
from langchain_core.output_parsers import RunnablePassthrough #Passes data through the pipeline without modifications, useful for chaining tasks where no transformation is needed between steps.
from langchain_groq import ChatGroq #A specialized chat interface for Groq models, allowing interaction with language models for tasks such as answering queries or generating text.
from langchain_community.embeddings import HuggingFaceBgeEmbeddings #Generates dense vector representations of text using Hugging Face's Bidirectional Generative Embedding (BGE) models, essential for semantic search and similarity tasks.

