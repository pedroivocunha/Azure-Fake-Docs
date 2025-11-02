import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    container_name = os.getenv("container_name")
    azure_storage_connection_string = os.getenv("azure_storage_connection_string")
    storage_account_name = os.getenv("storage_account_name")
    endpoint = os.getenv("endpoint")
    key = os.getenv("subscription_key")
