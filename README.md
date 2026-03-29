# 🏥  Health-care-AI-assistant

 
A RAG-based (Retrieval-Augmented Generation) medical question-answering chatbot built with LangChain, Pinecone, OpenAI, and Flask. The chatbot retrieves relevant context from a medical knowledge base stored in Pinecone and uses GPT-4o to generate concise, accurate answers.
CICD has also been implemented using Github Action. 

![Home page](./images/Screenshot%202026-03-29%20155006.png)


# Libraries Used:
```
    1. langchain==0.3.26
    2. flask==3.1.1
    3. sentence-transformers==4.1.0
    4. pypdf== 5.6.1
    5.python-dotenv==1.1.0
    6. langchain-pinecone==0.2.8
    7.langchain-openai==0.3.24
    8. langchain-community==0.3.26
    9. sentence-transformers
```

# Project's structure

 
```
medical-chatbot/
├── src/
│   ├── __init__.py
│   ├── helper.py          # PDF loading, text splitting, and embedding utilities
│   └── prompt.py          # System prompt definition
├── templates/
│   └── chat.html          # Frontend chat UI
├── static/
│   └── style.css          # Chat UI styling
├── notebook/
│   └── trigger.ipynb      # Experimentation notebook
├── app.py                 # Flask application entry point
├── store_index.py         # Script to embed docs and store in Pinecone
├── template.py            # Project scaffolding script
├── setup.py               # Package setup
├── requirements.txt       # Python dependencies
└── .env                   # Environment variables (not committed)
```



# Deployment Steps:
```
update ec2 machine :
        sudo apt-get update
        sudo apt-get upgrade

Install docker on the machine:
        curl -fsSL https://get.docker.com -o get-docker.sh
        sudo sh get-docker.sh
        sudo usermod -aG docker ubuntu
        newgrp docker

Add all the command form github-> setting-> Action -> runner -> new runner
```


# Secret Keys:

```
AWS_ACCESS_KEY_ID :
AWS_SECRET_ACCESS_KEY :
AWS_DEFAULT_REGION :
ECR_REPOSITORY:
OPENAI_API_KEY:
PINECONE_API_KEY:

```