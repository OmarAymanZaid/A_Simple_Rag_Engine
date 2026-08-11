# RAG Engine

A simple **Retrieval-Augmented Generation (RAG) engine** built with **LangChain** and **FastAPI**.

The project is intentionally general-purpose rather than being tied to a specific domain. Its primary goal is to build practical experience designing and implementing the infrastructure behind RAG applications, while following a structured and repeatable development workflow.

## 🎯 Project Objective

The main objective of this project is to reinforce the skills required to build RAG systems from the ground up.

Rather than focusing on a specialized application, the project provides a reusable foundation where different document collections can be loaded, indexed, retrieved, and used to generate context-aware responses.

The project is also being developed using **The Routine Method** — a structured development approach designed to make implementation predictable and repeatable while keeping architectural decisions under the developer's control.

## 🏗️ Architecture

The RAG pipeline follows the general flow:

```text
                ┌─────────────────┐
                │     Documents   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Document Loading│
                │ & Processing    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Text Splitting  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Embeddings    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    ChromaDB     │
                │  Vector Store   │
                └────────┬────────┘
                         │
              User Query │
                         ▼
                ┌─────────────────┐
                │    Retrieval    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Google Gemini   │
                │      LLM        │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     Response    │
                └─────────────────┘
```

## 🛠️ Technology Stack

* **Python** — Core programming language
* **FastAPI** — Backend API framework
* **LangChain** — RAG and LLM application framework
* **Google Gemini** — LLM for response generation and embeddings
* **ChromaDB** — Vector store for document embeddings
* **Pydantic / Pydantic Settings** — Data validation and configuration
* **Uvicorn** — ASGI server
* **Git & GitHub** — Version control

## 🔄 RAG Pipeline

The system is built around the standard RAG workflow:

1. **Load** documents into the system.
2. **Split** documents into smaller chunks.
3. **Embed** the chunks into vector representations.
4. **Store** the vectors in ChromaDB.
5. **Receive** a user query.
6. **Embed and retrieve** the most relevant document chunks.
7. **Construct** a context-aware prompt.
8. **Generate** an answer using Google Gemini.
9. **Return** the generated response through the API.

## 🚀 Project Scope

The project is intentionally kept simple.

It is not designed around a specific business domain or dataset. Instead, the document collection can be replaced depending on what is being tested or learned.

This makes the project useful for experimenting with different:

* Documents
* Chunking strategies
* Embedding configurations
* Retrieval strategies
* Prompt structures
* LLM configurations
* RAG pipeline designs

## 📁 Project Structure

The project follows a modular backend architecture based on a repeatable development routine.

```text
.
├── src/
│   ├── helpers/
│   ├── utils/
│   ├── assets/
│   ├── routes/
│   ├── models/
│   ├── controllers/
│   └── ...
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

The exact structure may evolve as additional RAG components are implemented.

## ⚙️ Configuration

Configuration is managed through environment variables.

Create a `.env` file based on `.env.example` and provide the required Google API credentials and application configuration.

```env
GOOGLE_API_KEY="your-api-key"

# Application configuration
APP_NAME="RAG Engine"
ENVIRONMENT="local"
LOG_LEVEL="INFO"
```

> Never commit API keys or other secrets to the repository.

## ▶️ Running the Project

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env` from `.env.example` and add the required configuration.

### 5. Run the API

```bash
uvicorn src.main:app --reload
```

The API will then be available locally through the configured server address.

## 🧪 Testing

The project will include testing for the different components of the RAG pipeline and API as they are implemented.

The development workflow follows a simple cycle:

```text
Design
   ↓
Implement
   ↓
Test
   ↓
Document
```

## 🧠 Development Method

This project is developed using **The Routine Method**.

The method aims to make implementation increasingly predictable by standardizing recurring development tasks into reusable routines.

The developer focuses primarily on:

* Requirements
* Architecture
* Component design
* Integration decisions
* Domain-specific logic
* Validation of the generated implementation

Implementation details are organized into repeatable subroutines so that common patterns become consistent and easier to reproduce.

## 📌 Learning Goals

Through this project, the main areas of practice are:

* Building RAG pipelines with LangChain
* Working with document loaders and text splitters
* Generating and storing embeddings
* Working with vector databases
* Implementing similarity-based retrieval
* Connecting an LLM to retrieved context
* Designing RAG prompts
* Building RAG APIs with FastAPI
* Structuring an AI backend into reusable components
* Managing external AI services through configuration
* Testing and documenting API components
* Developing RAG infrastructure using a repeatable implementation routine

## 🔮 Future Improvements

Potential extensions include:

* Multiple document formats
* Metadata-aware retrieval
* Different chunking strategies
* Configurable retrieval parameters
* Conversation history
* Reranking
* Streaming responses
* Retrieval evaluation
* RAG pipeline evaluation metrics
* Additional LLM or embedding providers

These extensions are not required for the initial version and can be introduced as the underlying RAG infrastructure develops.

## 📄 License

This project is licensed under the terms specified in the `LICENSE` file.
