# SwiftReddit.AI

SwiftReddit.AI lets you learn from reddit quicker! 
For example, let's say I want the opinions of other University of Alberta students on which laptop is best for engineering; Rather than scrolling through countless posts and keeping tally of what people say, wouldn't it be nice to have a quick answer? SwiftReddit.AI gives you precisely that! 

You start by submitting the name of the subreddit you want to query; Building off the earlier example, this would be r/uAlberta. Next, pick 2-3 keywords that will narrow down the posts within that subreddit to what you're looking for; In the engineering laptops example, we'll choose "engineering" and "laptops". Finally, ask SwiftReddit.AI a question, such as "What are some good laptops for engineering?". It will look through the appropriate posts, and give you an answer to your question within seconds, saving you significant time! 

How does SwiftReddit.AI work exactly?
This application works by leveraging the OpenAI GPT-3.5-Model, and a few other python libraries (LlamaIndex and LangChain). We all have heard about how ChatGPT's September 2021 knowledge cut-off, however SwiftReddit.AI takes it one step further and feeds the GPT-3.5-Model information on specific posts in your chosen subreddit. By filtering through subreddit and keywords, we'll have a small list of posts that we think may contain the information we need. We essentially temporarily add these posts to the AI Model's existing knowledge set, which allows us to now ask specific questions with a wider training dataset. The AI model will then be able to give you a specific answer based on the information in the subreddit, making the process of getting reddit information much more efficient. For questions regarding the technical details, please contact Abhro Chowdhury via either LinkedIn at https://www.linkedin.com/in/abhro-chowdhury/, or email at abhrajyo@ualberta.ca.

