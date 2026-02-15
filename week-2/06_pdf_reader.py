"""
📄 Exercise 06 — PDF Reader: Chat with Your Documents!
=======================================================

Goals:
------
- Learn to extract text from PDF files using Python
- Send document content to an LLM for analysis
- Build a "Chat with your PDF" mini-app
- Understand why this is one of the most useful AI skills in the real world!

Why this matters:
-----------------
"Chat with your documents" is THE killer feature of modern AI apps.
Imagine: upload a 50-page report and ask "What are the key risks?" — 
the AI reads it all and gives you a summary in seconds.

Install:
--------
pip install PyMuPDF   (this installs as 'fitz' — yes the name is confusing!)

How PDF Reading Works:
----------------------
PDFs are weird. They're not like text files — they're more like images with
text placed at specific coordinates. Libraries like PyMuPDF figure out how
to extract that text for us.

Flow: PDF file → PyMuPDF extracts text → Send text to LLM → Get answer!

Instructions:
-------------
PART 1 — Read a PDF:
  1. Use PyMuPDF (import fitz) to open and extract text from a PDF
  2. Print the text content and page count

PART 2 — Summarize a PDF:
  1. Send the extracted text to Claude
  2. Ask it to summarize the key points
  3. Display the summary with Rich

PART 3 — Q&A with your PDF:
  1. Load the PDF text once
  2. Let the user ask questions about it in a loop
  3. Send the PDF content + question to Claude each time
  4. This is your first "RAG-lite" (Retrieval Augmented Generation) app!

For testing:
-----------
You can use ANY PDF you have! Try with:
- A recipe PDF → ask "What ingredients do I need?"
- A resume → ask "What are this person's key skills?"
- A research paper → ask "Explain the main findings in simple terms"

If you don't have a PDF handy, the script will create a sample one for you.

Tips:
-----
- fitz.open("file.pdf") opens the PDF
- For each page: page.get_text() extracts the text
- Send the text as context in the system prompt or user message
- Keep the prompt clear: "Based on the following document, answer..."
"""

import os
from dotenv import load_dotenv

load_dotenv()


# ============ HELPER: Create a Sample PDF for Testing ============
# Run this once if you don't have a PDF to test with!

def create_sample_pdf(filename="sample_data/sample_document.pdf"):
    """Creates a sample PDF for testing. You only need to run this once."""
    try:
        from fpdf import FPDF
    except ImportError:
        print("Run: pip install fpdf2")
        return

    os.makedirs("sample_data", exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, text="The Amazing World of Penguins", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(10)
    pdf.set_font("Helvetica", size=11)

    content = [
        "Chapter 1: Introduction to Penguins",
        "",
        "Penguins are fascinating flightless birds that live primarily in the Southern Hemisphere. "
        "Despite their inability to fly, they are excellent swimmers, with some species reaching "
        "speeds of up to 22 miles per hour underwater. There are 18 known species of penguins, "
        "ranging from the tiny Little Blue Penguin (just 13 inches tall) to the majestic Emperor "
        "Penguin (up to 4 feet tall).",
        "",
        "Chapter 2: Emperor Penguins",
        "",
        "Emperor Penguins are the largest of all penguin species. They can dive to depths of "
        "1,800 feet and hold their breath for up to 20 minutes. During the harsh Antarctic winter, "
        "male Emperor Penguins incubate their eggs by balancing them on their feet, covered by a "
        "flap of skin called a brood pouch. They huddle together in groups of up to 5,000 to "
        "conserve warmth, rotating positions so everyone gets a turn in the warm center.",
        "",
        "Chapter 3: Penguin Diet",
        "",
        "Penguins primarily eat fish, squid, and krill. An adult Emperor Penguin can eat up to "
        "6 kg of food per day during peak feeding times. They have specialized spines on their "
        "tongues and the roof of their mouths to grip slippery prey. Different species have "
        "different dietary preferences depending on their habitat and size.",
        "",
        "Chapter 4: Conservation Status",
        "",
        "Several penguin species are threatened by climate change, overfishing, and habitat "
        "destruction. The African Penguin population has declined by about 70% since 2001. "
        "Conservation efforts include marine protected areas, breeding programs, and reducing "
        "bycatch in fishing operations. Supporting sustainable fishing practices is one of the "
        "most impactful ways to help penguin populations recover.",
    ]

    for line in content:
        if line.startswith("Chapter"):
            pdf.set_font("Helvetica", "B", 13)
            pdf.cell(0, 10, text=line, new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("Helvetica", size=11)
        elif line == "":
            pdf.ln(5)
        else:
            pdf.multi_cell(0, 6, text=line)

    pdf.output(filename)
    print(f"✅ Sample PDF created: {filename}")


# Uncomment the line below to create the sample PDF:
# create_sample_pdf()


# ============ PART 1: Read a PDF ============

# TODO: Import fitz (PyMuPDF)
# import fitz

# TODO: Open the PDF
# doc = fitz.open("sample_data/sample_document.pdf")

# TODO: Extract text from all pages
# full_text = ""
# for page_num in range(len(doc)):
#     page = doc[page_num]
#     full_text += page.get_text()

# TODO: Print some info
# print(f"📄 Pages: {len(doc)}")
# print(f"📝 Characters: {len(full_text)}")
# print(f"📖 Preview (first 500 chars):\n{full_text[:500]}")



# ============ PART 2: Summarize the PDF ============

# TODO: Import anthropic and set up client
# import anthropic
# client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# TODO: Send the PDF text to Claude for summarization
# message = client.messages.create(
#     model="claude-sonnet-4-5-20250929",
#     max_tokens=1024,
#     system="You are a helpful document analyst. Be concise and clear.",
#     messages=[{
#         "role": "user",
#         "content": f"Please summarize the key points of this document:\n\n{full_text}"
#     }]
# )
# print(message.content[0].text)



# ============ PART 3: Interactive Q&A with Your PDF ============

# TODO: Build a loop where the user can ask questions about the PDF
# The trick: include the PDF text in EVERY message as context!
#
# while True:
#     question = input("\n❓ Ask about the document (or 'quit'): ")
#     if question.lower() in ['quit', 'exit', 'q']:
#         break
#
#     message = client.messages.create(
#         model="claude-sonnet-4-5-20250929",
#         max_tokens=512,
#         system=f"You are a helpful assistant. Answer questions based ONLY on "
#                f"this document:\n\n{full_text}\n\n"
#                f"If the answer isn't in the document, say so.",
#         messages=[{"role": "user", "content": question}]
#     )
#     print(f"\n💬 {message.content[0].text}")


"""
🧪 Expected Output:

📄 Pages: 1
📝 Characters: 1847
📖 Preview: The Amazing World of Penguins...

📝 Summary:
This document covers four aspects of penguins:
1. There are 18 species ranging from 13 inches to 4 feet tall
2. Emperor Penguins can dive to 1,800 feet...
3. Penguins eat fish, squid, and krill...
4. Several species are threatened; African Penguin population down 70%...

❓ Ask: How deep can Emperor Penguins dive?
💬 Emperor Penguins can dive to depths of 1,800 feet and hold their breath
   for up to 20 minutes.

❓ Ask: What do penguins eat?
💬 Penguins primarily eat fish, squid, and krill...

❓ Ask: What's the weather like today?
💬 I can't answer that — the document only covers penguin biology and conservation.
"""
