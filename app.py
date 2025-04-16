# Initialize Traceloop SDK and LlamaIndex with Azure OpenAI
# This script sets up tracing and testing of the LlamaIndex integration with Azure OpenAI

import os
from traceloop.sdk import Traceloop
from config import AzureOpenAIConfig, LangSmithConfig

# Get LangSmith API key from environment variables for tracing
# Load application settings
az_settings = AzureOpenAIConfig()
langsmith_settings = LangSmithConfig()

# initialize Traceloop with LangSmith endpoint and authentication environment variables
os.environ["TRACELOOP_BASE_URL"] = "https://api.smith.langchain.com/otel"
os.environ["TRACELOOP_HEADERS"] = "x-api-key=" + langsmith_settings.api_key + ",Langsmith-Project=" + langsmith_settings.project

Traceloop.init()


# Initialize Traceloop with LangSmith endpoint and authentication
# - api_endpoint: LangSmith OTEL endpoint for trace collection
# - headers: Authentication and content type headers
# - disable_batch: Send traces immediately without batching
# - app_name: Name of the application for trace identification
# Traceloop.init(api_endpoint="https://api.smith.langchain.com/otel",
#                headers=
#                {
#                 "x-api-key": langsmith_settings.api_key, 
#                 "content-type": "application/protobuf"},
#                disable_batch=False,
#                app_name=langsmith_settings.project,
#                )

# Import required LlamaIndex components
from llama_index.core import VectorStoreIndex, Document
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.core import Settings


# Configure LlamaIndex to use Azure OpenAI for text generation
llm = AzureOpenAI(
            model=az_settings.gpt_4o_model_name,
            engine=az_settings.gpt_4o_deployment_name,
            deployment_name=az_settings.gpt_4o_deployment_name,
            api_key=az_settings.api_key,
            azure_endpoint=az_settings.endpoint,
            api_version=az_settings.api_version,
        )

# Configure LlamaIndex to use Azure OpenAI for embeddings
embed_model = AzureOpenAIEmbedding(
            model=az_settings.embeddings_model,
            deployment_name=az_settings.embeddings_name,
            api_key=az_settings.api_key,
            azure_endpoint=az_settings.embeddings_endpoint,
            api_version=az_settings.embeddings_api_version,
        )

# setting the llm and embed_model to the llm and embed_model
Settings.llm = llm
Settings.embed_model = embed_model

# Test the setup with a sample document and query
try:
    # Create test index with example document
    documents = [Document.example()]
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    
    # Run test query
    response = query_engine.query("What is this document about?")
    print(f"Query Response: {response}")
    
except Exception as e:
    print(f"Error occurred: {str(e)}")