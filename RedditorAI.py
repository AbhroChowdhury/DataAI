from llama_index import GPTVectorStoreIndex, download_loader
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory

RedditReader = download_loader('RedditReader')

subreddits = ['MachineLearning']
search_keys = ['PyTorch', 'deploy']
post_limit = 10

loader = RedditReader()
documents = loader.load_data(subreddits=subreddits, search_keys=search_keys, post_limit=post_limit)
index = GPTVectorStoreIndex.from_documents(documents)

tools = [
    Tool(
        name="Reddit Index",
        func=lambda q: index.query(q),
        description=f"Useful when you want to read relevant posts and top-level comments in subreddits.",
    ),
]
llm = OpenAI(temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history")
agent_chain = initialize_agent(
    tools, llm, agent="zero-shot-react-description", memory=memory
)

output = agent_chain.run(input="What are the pain points of PyTorch users?")
print(output)