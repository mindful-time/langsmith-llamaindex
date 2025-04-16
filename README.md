# LangSmith LlamaIndex Integration

This project demonstrates the integration of LlamaIndex with Azure OpenAI and LangSmith for tracing and monitoring AI applications.

## Overview

The project sets up a simple LlamaIndex application that:
- Uses Azure OpenAI for text generation and embeddings
- Integrates with LangSmith for tracing and monitoring
- Demonstrates basic document indexing and querying capabilities

## Prerequisites

- Python 3.11
- Azure OpenAI service with:
  - GPT-4 deployment
  - Embeddings model deployment
- LangSmith account and API key
- uv (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd langsmith-llamaindex
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies using uv:
```bash
# Install uv using the recommended script if you haven't already:
# On macOS and Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
# On Windows (PowerShell):
# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Verify uv installation
uv --version

# Install project dependencies
uv pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root with the following variables:
```
# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
AZURE_OPENAI_API_VERSION=your_api_version
AZURE_OPENAI_GPT4o_MODEL=your_gpt4_model_name
AZURE_OPENAI_GPT4o_DEPLOYMENT=your_gpt4_deployment_name
AZURE_OPENAI_EMBEDDINGS_MODEL=your_embeddings_model_name
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT=your_embeddings_deployment_name
AZURE_OPENAI_EMBEDDINGS_ENDPOINT=your_embeddings_endpoint
AZURE_OPENAI_EMBEDDINGS_API_VERSION=your_embeddings_api_version

# LangSmith Configuration
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=your_project_name
```

## Usage

Run the main application:
```bash
python app.py
```

The application will:
1. Initialize the Traceloop SDK with LangSmith configuration
2. Set up LlamaIndex with Azure OpenAI
3. Create a test index with an example document
4. Run a sample query and print the response

## Project Structure

- `app.py`: Main application file containing the LlamaIndex and LangSmith integration
- `config.py`: Configuration management using Pydantic
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (not tracked in git)

## Dependencies

- llama-index >= 0.9.0
- traceloop >= 0.0.1
- pydantic >= 2.0.0
- pydantic-settings >= 2.0.0
- python-dotenv >= 1.0.0

