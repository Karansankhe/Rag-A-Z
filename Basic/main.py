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

import bs4 #used for extracting information fropm web pages (before passing to the WebBaseLoader)
from langchain import hub #A framework for building applications powered by language models (LLMs), focusing on modularity and the combination of components such as document loaders, text splitters, embeddings, and vector stores.
from langchain_text_splitters import RecursiveCharacterTextSplitter #Breaks down long texts into smaller chunks based on recursive rules (e.g., by paragraph, sentence, or character count).
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores import StrOutputParser
from langchain_core.output_parsers import RunnablePassthrough 
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
