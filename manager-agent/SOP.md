### This is a bigger project which consists of using agents and RAG systems, for making a manager-type-agent
#### This sop would be updated regulary with specific information added in specific places
---
### 1. Setting up the file structure

- the main code is in the ```src/``` folder
- ```documents/``` contains the docs for RAG system
- helpers.py function has code we use often - like calling ```gpt4 api``` etc.
- ```.env``` file has all the environment variables
- the name of the files and folders complement the work they do, for eg: the ```without_lc``` file means the code is implementation without langchain etc.
---

#### 1.1 helpers.py file

- it only has code for calling the gpt-4 api for now
- imports the openai library, initialise the client and feed it the api key, using the getenv() function, which gets environment variables from the .env file automatically using the name
- then, we return the output of the function, which is the reponse