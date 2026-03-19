import pypdf
from pypdf import PdfReader
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


path = r"/Users/nisruch/Downloads/00_course_roadmap.md.pdf"
# reader = PdfReader(path)
# pdf_text = ""
# for page in reader.pages:
#    pdf_text = pdf_text + page.extract_text()



# user_question = input('Please ask a question reagarding the pdf document: ')


# user_prompt = f"""
# Please provide the answer based on the following document text :
# {pdf_text}

# User question: {user_question}

# """


# message = client.messages.create(
#         model="claude-sonnet-4-5",
#         temperature=0,
#         max_tokens=5000,
#         system=f"You are helpful assistant that provides the answers to the user's question based on the given document's context.",
#         messages=[
#             {
#                 "role": "user",
#                 "content": user_prompt,
#             }
#         ],
#     )

# text = message.content[0].text

# print("\nMODEL OUTPUT:")
# print(text)




# from langchain_anthropic import ChatAnthropic

# llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0.1)
# response = llm.invoke("Write a paragraph about a PupPup as best dog in the world.")
# print(response.content)





from langchain_community.document_loaders import PyPDFLoader
from langchain_anthropic import ChatAnthropic


#Step 1 : Loading the document
path = r"/Users/nisruch/Downloads/00_course_roadmap.md.pdf"
file_path = path
loader = PyPDFLoader(file_path)
docs = loader.load()

#Step 2 : Creating the LLM object
llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0.1)

#Step 3 : Creating the user question
user_question = "Write a summary of the document for a 10 year old child."

#Step 4 : Creating the user prompt
user_prompt = f""""
Please provide the answer based on the following document text :
{docs}

User question: {user_question}

"""

#Step 5 : Ingesting the user prompt which has all the instructions and context into the llm to generate the response
response = llm.invoke(user_prompt)
print(response.content)


#Exercise : Write a function to generate the response using llm and langchain, it should take the user question, path, model, temperature