import os
from functools import lru_cache

from langchain_openai import OpenAIEmbeddings, AzureOpenAIEmbeddings

@lru_cache(maxsize=4)
def get_openai_embedding(azure: bool = False):
    if azure:
        return AzureOpenAIEmbeddings(
            azure_deployment=os.environ["EMBEDDING_DEPLOYMENT"],
            azure_endpoint=os.environ["AZURE_ENDPOINT"],
            chunk_size=1,
        )
    return OpenAIEmbeddings()