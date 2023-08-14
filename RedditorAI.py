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

# loading reddit reader from LlamaHub
RedditReader = download_loader('RedditReader')

# allow user to specify what subreddits they want
subredditChoice = input("Please enter the name of the SubReddit you'd like to query: ")
subreddits = [subredditChoice]

searchkeyChoice1 = input("Please enter a keyword to narrow down the search: ")
searchkeyChoice2 = input("Please enter another keyword to narrow down the search: ")
search_keys = [searchkeyChoice1, searchkeyChoice2]

print("Thank you, please wait as we process your request!")

# will need to change accordingly; the higher this number the more accurate the answer will be
# however, the higher the number = more data to embed, which will cost me more via openAI API
post_limit = 15

# loading appropriate subreddit data, and storing it as indexes
loader = RedditReader()
documents = loader.load_data(subreddits=subreddits, search_keys=search_keys, post_limit=post_limit)
index = VectorStoreIndex.from_documents(documents)

# initializing query engine, and user question
query_engine = index.as_query_engine()

print("Please enter your question: ")
userQuestion = input()

#response = query_engine.query("What are some good laptops for engineering?")
response  = query_engine.query(userQuestion)
print(response)