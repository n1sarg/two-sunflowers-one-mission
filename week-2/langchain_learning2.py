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

""""
What Does This Code Do?
It loads a movie script from the internet, gives it
to an AI, and lets you ask questions about it in a chat.
That's it. You type a question, the AI reads the script and answers you.
Like having a friend who has perfect memory of every line in the film.


Remember the conversation:
The chatbot keeps a list of every message,your and the AI's.
Each time you ask a new question, it sends the ENTIRE conversation
history back to the AI. This means the AI remembers what you talked
about earlier.
Without this, every question would be like talking to someone with
amnesia, they would forget your previous questions instantly.

SystemMessage -> Instructions we give the AI -> A job description, what it is and what it is not allowed to do.
HumanMessage -> The user's question -> The question the user is asking.
AIMessage -> The AI's response -> The answer the AI is giving.

ChatHistory -> The list of all the messages, your and the AI's.

while True creates an infinite loop, the chatbot keeps running
forever until you tell it to stop.

input("You: ") Shows "You: " and waits for you to type
.strip() — Removes any extra spaces from the start/end

If you type "exit" (in any case), stop the chatbot.
.lower() converts to lowercase so "EXIT", "Exit", "exit" all work.
break exits the while True loop.

"""


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

