### This is a bigger project which consists of using agents and RAG systems, for making a manager-type-agent
#### This sop would be updated regulary with specific information added in specific places
---
### 1. Setting up the file structure

- the main code is in the ```src/``` folder
- ```documents/``` contains the docs for RAG system
- helpers.py function has code we use often - like calling ```gpt4 api``` etc.
- ```.env``` file has all the environment variables
- the name of the files and folders complement the work they do, for eg: the ```without_lc``` file means the code is implementation without langchain etc.

**TO SETUP FOR THE FIRST TIME, Make a virtual environment using ```python -m venv env```, activate it using ```cd env/bin/activate``` and then, do ```pip install -r requirements.txt``` to install all the dependencies **
---


#### 1.1 helpers.py file

- it only has code for calling the gpt-4 api for now
- imports the openai library, initialise the client and feed it the api key, using the getenv() function, which gets environment variables from the .env file automatically using the name
- then, we return the output of the function, which is the reponse

```python
from os import getenv
from openai import OpenAI

client = OpenAI(api_key=getenv("OPENAI_API_KEY"))

def get_llm_response(prompt:str):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    )

    return completion.choices[0].message.content

```


#### 1.2  without_lc file

- here is the code to parse the pdf file, get first 50 pages and get a reponse based on them
```python
from helpers import get_llm_response
from pypdf import PdfReader 

#read the pdf save it
reader = PdfReader('superintelligence.pdf') 

book = []

for page in reader.pages:
    book.append(str(page.extract_text()) + "\n\n")

docs = str(book[:50])


## specifying the prompt and variables
QUESTION = "What is this book about, who wrote it and tell me something about the initial content ?"

PROMPT = f"""    

You are a useful researcher. You need to answer the question using the documents given below.

- Question  : {QUESTION}

- Documents : {docs}

"""

print(get_llm_response(PROMPT))

```

*here is the response* : <br>
The book "Superintelligence: Paths, Dangers, Strategies" is a detailed exploration of the potential future impacts of superintelligent machines. It was written by Nick Bostrom, who is the Director of the Future of Humanity Institute and a Professor at the University of Oxford.

The initial content of the book starts with a fable called "The Unfinished Fable of the Sparrows," which serves as a metaphor for the potential risks of pursuing the creation of a highly intelligent machine without adequate planning for its control. This fable sets the stage for the discussion on the complexities and dangers associated with the development of superintelligence.

Following the fable, the preface delves into the nature of human intelligence, its evolutionary advantages, and the prospect that machine intelligence could surpass human intelligence. Bostrom argues that a machine superintelligence could become very powerful and that controlling it would be crucial but challenging. He stresses that creating a superintelligence might be humanity's last and most important challenge because once it exists, it could fundamentally alter our control over our own fate.

The table of contents of the book indicates a comprehensive exploration of various aspects related to superintelligence, such as pathways to developing it, forms it might take, the dynamics of an intelligence explosion, strategic advantages, cognitive superpowers, existential risks, control problems, and potential societal impacts.

The first chapter of the book provides an overview of the historical developments and current capabilities of artificial intelligence, laying the groundwork for understanding the trajectory towards superintelligence and highlighting the importance of preparing for both its opportunities and risks.

#### 1.3 with_lc file

- using langchain, loading logic is easy and also, we can just send the required context to the llm, hence saving is clutter and tokens

![rag](https://docs.llamaindex.ai/en/stable/_static/getting_started/basic_rag.png)

- using langchain to implement the loader, get the file and save it in a local vector db, get the relevant context and send it to the llm

- this whole set of steps is called RAG, it helps in saving tokens and only sending the relevant context to the llm to answer the question

- here is the code implementation

```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

 # Load document using PyPDFLoader document loader

path = ""

loader = PyPDFLoader(f"{path}.pdf")
documents = loader.load()
    # Split document in chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")
docs = text_splitter.split_documents(documents=documents)

embeddings = OpenAIEmbeddings()
    # Create vectors
vectorstore = FAISS.from_documents(docs, embeddings)
    # Persist the vectors locally on disk
vectorstore.save_local("faiss_index_constitution")


def query_pdf(query):
    # Load from local storage
    persisted_vectorstore = FAISS.load_local("faiss_index_constitution", embeddings, allow_dangerous_deserialization=True)

    # Use RetrievalQA chain for orchestration
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=persisted_vectorstore.as_retriever())
    result = qa.run(query)
    print(result)


def main():
    query = input("Type in your query: \n")
    while query != "exit":
        query_pdf(query)
        query = input("Type in your query: \n")


if __name__ == "__main__":
    main()
```

- make sure before running the file, you are inside the ```src/``` folder in the terminal, then only it can parse the pdf from the path
- ignore all the warnings in the terminal, and run the file after specifying the path to your documents
- when type in your query appears, give your query