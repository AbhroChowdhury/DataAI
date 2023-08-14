from llama_index import VectorStoreIndex, download_loader
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os
import json
import openai

# load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# read the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# reddit credentials
reddit_client_id = os.environ.get("REDDIT_CLIENT_ID")
reddit_client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
reddit_user_agent = os.environ.get("REDDIT_USER_AGENT")
reddit_username = os.environ.get("REDDIT_USERNAME")
reddit_password = os.environ.get("REDDIT_PASSWORD")


RedditReader = download_loader('RedditReader')

subreddits = ['uAlberta']
search_keys = ['engineering', 'laptop']
post_limit = 20

loader = RedditReader()
documents = loader.load_data(subreddits=subreddits, search_keys=search_keys, post_limit=post_limit)
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("What are some good laptops for engineering?")
print(response)