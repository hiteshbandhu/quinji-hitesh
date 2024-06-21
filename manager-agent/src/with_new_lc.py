from langchain_openai import ChatOpenAI
from os import getenv
from dotenv import load_dotenv
# Load the .env file
load_dotenv()
# Verify the environment variable is loaded
api_key = getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not found")

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=api_key)

from langchain import hub
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load, chunk and index the contents of the blog.
loader = PyPDFLoader("./Lecture09a.pdf")

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

question = "hi ! How are you ?"

while question != "exit":
    question = str(input("Type Your Query: \n\n"))
    output = rag_chain.invoke(question)
    print("\n-" + output + "\n******")

