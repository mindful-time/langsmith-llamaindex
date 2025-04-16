from pydantic_settings import BaseSettings, SettingsConfigDict

class AzureOpenAIConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="AZURE_OPENAI_", extra="ignore")
    api_key: str
    endpoint: str
    api_version: str
    gpt_4o_deployment_name: str
    gpt_4o_mini_deployment_name: str
    gpt_4o_model_name: str
    gpt_4o_mini_model_name: str

    embeddings_model: str
    embeddings_name: str
    embeddings_endpoint: str
    embeddings_api_version: str

class LangSmithConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="LANGCHAIN_", extra="ignore")
    api_key: str
    api_url: str
    project: str
    tracing_v2: str
    
