from llama_index import GPTVectorStoreIndex, download_loader
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os


load_dotenv()

reddit_client_id = os.environ.get("REDDIT_CLIENT_ID")
reddit_client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
reddit_user_agent = os.environ.get("REDDIT_USER_AGENT")
reddit_username = os.environ.get("REDDIT_USERNAME")
reddit_password = os.environ.get("REDDIT_PASSWORD")


RedditReader = download_loader('RedditReader')

subreddits = ['MachineLearning']
search_keys = ['PyTorch', 'deploy']
post_limit = 10

loader = RedditReader()
documents = loader.load_data(subreddits=subreddits, search_keys=search_keys, post_limit=post_limit)
index = GPTVectorStoreIndex.from_documents(documents)

index.query("What are the pain points of PyTorch users?")
