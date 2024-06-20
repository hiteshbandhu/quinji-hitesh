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