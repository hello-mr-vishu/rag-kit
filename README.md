# RAG Application

This project is a Retrieval-Augmented Generation (RAG) based medical chatbot. It uses a large language model to answer questions about medical topics based on a provided medical text. The chatbot is built with Flask and uses Pinecone for vector storage and retrieval.

## Features

-   **Medical Question Answering:** Ask the chatbot any medical question, and it will provide answers based on the knowledge from the provided medical book.
-   **Web Interface:** A simple and intuitive web interface to interact with the chatbot.
-   **RAG Pipeline:** Implements a RAG pipeline using LangChain, which includes:
    -   Loading and splitting a medical PDF document.
    -   Generating embeddings for the text chunks.
    -   Storing and retrieving text chunks from a Pinecone vector store.
    -   Generating answers using a large language model.

## Technologies Used

-   **Backend:** Flask
-   **Frontend:** HTML, CSS, JavaScript, Bootstrap
-   **LLM Orchestration:** LangChain
-   **Vector Store:** Pinecone
-   **Embeddings:** Hugging Face Sentence Transformers (`all-MiniLM-L6-v2`)
-   **LLM:** Google Gemini

<img src="documents/chatbot1.png" alt="Chatbot_screenshot" width="800" height="600">


## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/hello-mr-vishu/rag-kit.git
    cd your-repository-name
    ```

2.  **Create a virtual environment and install dependencies:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**

    Create a `.env` file in the root directory and add the following:

    ```
    PINECONE_API_KEY="YOUR_PINECONE_API_KEY"
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```

4.  **Store the index:**

    Run the `store_index.py` script to process the PDF, create embeddings, and store them in Pinecone:

    ```bash
    python store_index.py
    ```

## Usage

1.  **Run the Flask application:**

    ```bash
    python app.py
    ```

2.  **Open your web browser and go to:**

    ```
    http://127.0.0.1:8080
    ```

3.  **Start chatting with the medical chatbot!**

<img src="documents/Deployed.png" alt="Chatbot_screenshot" width="800" height="600">

## Project Structure

```
.
├── app.py              # Flask application
├── data
│   └── Medical_book.pdf # Medical document
├── requirements.txt    # Python dependencies
├── setup.py            # Setup script
├── src
│   ├── helper.py       # Helper functions for data processing
│   └── prompt.py       # System prompt for the LLM
├── static
│   └── style.css       # CSS for the web interface
├── store_index.py      # Script to create and store the vector index
└── templates
    └── chat.html       # HTML template for the chat interface
```


# AWS-CICD-Deployment-with-Github-Actions
<img src="documents/GitHub - Runners.png" alt="Chatbot_screenshot" width="800" height="600">

## 1. Login to AWS console.
<img src="documents/ECR.png" alt="ECR.png" width="800" height="600">

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws

<img src="documents/Instance details _ EC2 .png" alt="Instance details _ EC2 .png" width="800" height="600">

	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	6. AmazonEC2ContainerRegistryFullAccess

	7. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot

<img src="documents/SimpleDockerService _ CodePipeline.png" alt="Chatbot_screenshot" width="800" height="600">
<img src="documents/CICD pipeline.png" alt="Chatbot_screenshot" width="800" height="600">
	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO
   - PINECONE_API_KEY
   - OPENAI_API_KEY


<img src="documents/GitHub - Add Actions secret.png" alt="Chatbot_screenshot" width="800" height="600">

<img src="documents/Deploy1.png" alt="Deploy1.png" width="800" height="600">