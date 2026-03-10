# import anthropic
# import os
# from dotenv import load_dotenv

# load_dotenv()
# client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")) 


# def ai_calling(input_text):
#     message = client.messages.create(
#     model="claude-sonnet-4-5-20250929",
#     max_tokens=256,
#     temperature=0.5,
#     system="You are a mystical oracle. Give dramatic, mysterious one-sentence answers.",
#     messages=[{"role": "user", "content": input_text}]
#     )
#     return message.content[0].text


# print(ai_calling('Tell me a dog joke!'))









# prompts = [
#     "Write a paragraph about a PupPup as best dog in the world.",
#     "You are a Pulitzer-winning novelist. Write a literary paragraph about a lonely robot. Use sensory details and internal monologue.",
#     "Write a paragraph about a robot named Bolt-7 who lives in an abandoned factory. Style: whimsical, bittersweet. Include a reference to the movie 'Bolt'.",
# ]


# def story_writing(prompts):
#     panels = []
#     for i, prompt in enumerate(prompts):
#         message = client.messages.create(
#             model="claude-sonnet-4-5-20250929",
#             max_tokens=256,
#             system="You are a mystical oracle. Give dramatic, mysterious one-sentence answers.",
#             messages=[{"role": "user", "content": prompt}]
#         )

#     return print(f"Prompt {i+1}: {message.content[0].text}")

# print(story_writing(prompts))
     


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


def story_telling(prompts):
    panels = []
    for i, prompt in enumerate(prompts):
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=256,
            system="You are a mystical oracle. Give dramatic, mysterious one-sentence answers.",
            messages=[{"role": "user", "content": prompt}]
        )
    return panels.append(Panel(message.content[0].text, title=f"Prompt {i+1}"))
    
console.print(Columns(panels, equal=True))

print(story_telling(prompts))






