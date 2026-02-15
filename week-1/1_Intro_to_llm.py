"""
Warm-up mini-project — "Magic 8-Ball AI Oracle" 
This is your very first LLM interaction. The user asks a question, the LLM responds as a dramatic
fortune teller. It teaches API key loading, the client pattern, and basic response parsing.

Pre-requisites:
- We need to have api key for to use the LLM, we have stored it in the .env file, since we don't want to hardcode it in the code as best practice.


Few information about the parameters:

- model: The model name that we are using to generate the response.

- max_tokens: The maximum number of tokens that the model can generate, one token is approximately 4 characters.

- system: System prompts set the persona. The system prompt that we are using to guide the model's overall behavior, it is optional, 
          but if you provide it, the model will behave in this way only.


- temperature : The temperature is a parameter that controls the randomness of the model's output, 
                0 is the most deterministic, 1 is the most random. It is optional, but if you provide it, its optional though but recommended.

- messages: The messages are the messages that we are sending to the model, it is a list of dictionaries, 
            each dictionary contains a role and a content.

- role: The role of the message, it can be "user" or "assistant".

- content: The content of the message, it is the message that we are sending to the model, it can be a string or a list of strings.

- response: The response is the response that the model generates, it is a string.

- response.content[0].text: The text is the text that the model generates, it is a string.


The code syntax is, it will stay same for all the prompts, we will only change the parameters.

message = client.messages.create(
model=,
max_tokens=,
temperature=,
system=,
messages=[{"role": "user", "content": "User Prompt Here"}]
)

The general structure of the code is:
1. Load the API key from the .env file.
2. Create a client object.
3. Ask the user a question.
4. Generate the response using the client object.
5. Print the response.


To test the code for each part, you can run the code for each part separately, by commenting the code of other parts.

"""

# ============  PART - 1 Now lets use multiple prompts at once ============



import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")) 

question = input("🔮 Ask the oracle anything: ")

message = client.messages.create(
model="claude-sonnet-4-5-20250929",
max_tokens=256,
temperature=0.5,
system="You are a mystical oracle. Give dramatic, mysterious one-sentence answers.",
messages=[{"role": "user", "content": question}]
)
print(f"🔮 Claude speaks: {message.content[0].text}")



# ============ PART - 2 Now lets use multiple prompts at once ============


prompts = [
    "Write a paragraph about a PupPup as best dog in the world.",
    "You are a Pulitzer-winning novelist. Write a literary paragraph about a lonely robot. Use sensory details and internal monologue.",
    "Write a paragraph about a robot named Bolt-7 who lives in an abandoned factory. Style: whimsical, bittersweet. Include a reference to the movie 'Bolt'.",
]

panels = []
for i, prompt in enumerate(prompts):
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=256,
        system="You are a mystical oracle. Give dramatic, mysterious one-sentence answers.",
        messages=[{"role": "user", "content": prompt}]
    )
    print(f"Prompt {i+1}: {message.content[0].text}")





# ============ PART - 3 Now lets print the responses in better way ============
import anthropic
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns

load_dotenv()
console = Console()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")) 

prompts = [
"Write a paragraph about PupPup, as best dog in the world.",
"You are a Pulitzer-winning novelist. Write a literary paragraph about a lonely robot. Use sensory details and internal monologue.",
"Write a paragraph about a robot named Bolt-7 who lives in an abandoned factory. Style: whimsical, bittersweet.",
]

panels = []
for i, prompt in enumerate(prompts):
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=256,
        system="You are a mystical oracle. Give dramatic, mysterious one-sentence answers.",
        messages=[{"role": "user", "content": prompt}]
    )
    panels.append(Panel(message.content[0].text, title=f"Prompt {i+1}"))


console.print(Columns(panels, equal=True))