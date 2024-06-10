import os
from src.exception import CustomException
from src.logger import logging
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


GPT_MODEL = os.environ.get("GPT_MODEL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
GPT_VISION_MODEL = os.environ.get("GPT_VISION_MODEL")


# LLAMA_CLOUD_API = os.environ.get("llama_cloud_api")
# COHERE_API_KEY = os.environ.get("cohere_api_key")
# KDB_AI_API_KEY = os.environ.get("KDB_AI_API_KEY")
# KDB_ENDPOINT = "https://cloud.kdb.ai/instance/g6ezq28nnv"