###################### Web Scraping using LangChain #################



from langchain_community.document_loaders import WebBaseLoader
from langchain_anthropic import ChatAnthropic

loader = WebBaseLoader(["https://www.bbc.co.uk/news/articles/cvg33nwy9llo", "https://www.bbc.co.uk/news/articles/c62z5yl2l1lo"])
docs = loader.load()

llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0.1)

user_question = "Write a summary of both articles for a 10 year old child and is there any overlap in the articles?"


user_prompt = f""""
Please provide the answer based on the following document text :
{docs}

User question: {user_question}

Please provide the answer into ennglish and french both.

"""

response = llm.invoke(user_prompt)
print(response.content)



############## Chatbot using LangChain #################


from langchain_community.document_loaders import WebBaseLoader
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatAnthropic(model="claude-opus-4-6", temperature=0)

loader = WebBaseLoader("http://www.script-o-rama.com/movie_scripts/a2/stardust-script-transcript.html")
docs = loader.load()


system_prompt = f""""

Role : You are very helpful assistant chatbot that answers the questions based on the given stardust movie script.

This is the movie script : {docs}

Clear Instructions for the output :
- If the answer is not present in the script, say "I don't know" or "I am not sure", dont make up the answer.
- Please provide the answer in the plain text format, dont use any markdown or html tags.

"""

system_message = SystemMessage(content=system_prompt)

chat_history = [system_message]

print("The chatbot is ready to answer the questions based on the given stardust movie script.")

print("Type 'exit' to end the conversation.")

while True:
    user_question = input("You: ").strip()

    if user_question.lower() == "exit": 
        break
    else:
        chat_history.append(HumanMessage(content = user_question))

        response = llm.invoke(chat_history)

        chat_history.append(AIMessage(content = response.content))

        print("AI Model Response : ", response.content)

