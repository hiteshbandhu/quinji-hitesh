from helpers import get_llm_response
from pypdf import PdfReader 

#read the pdf save it
reader = PdfReader('Lecture04.pdf') 

docs = []

for page in reader.pages:
    docs.append(str(page.extract_text()) + "\n\n")

# docs = str(book[:50]) ## use this if the book is too long for example

## specifying the prompt and variables
QUESTION = str(input("What is your question : \n\n"))


PROMPT = f"""    

You are a useful researcher. You need to answer the question using the documents given below.

- Question  : {QUESTION}

- Documents : {docs}

"""

print(get_llm_response(PROMPT))