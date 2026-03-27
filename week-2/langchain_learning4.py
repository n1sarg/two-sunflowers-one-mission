import os
import tempfile
import streamlit as st
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.messages import HumanMessage, SystemMessage



load_dotenv()

MODEL = 'claude-opus-4-6'
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'

def load_file(uploaded_file):
    """Save the uploaded file to a temp location and load it as document(s)"""

    extension = os.path.splitext(uploaded_file.name)[1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=extension) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    if extension == '.pdf':
        docs = PyPDFLoader(temp_path).load()
    elif extension == '.txt':
        docs = TextLoader(temp_path, encoding = 'utf-8').load()
    else:
        print('Uploaded file is not pdf or txt file')
    
    os.unlink(temp_path)

    for doc in docs:
        doc.metadata['source_file'] = uploaded_file.name
    
    return docs
    

def chunk_documents(docs):
    """ Split long documents into small overlapping pieces"""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
    text_chunks = text_splitter.split_documents(docs)
    return text_chunks


def build_vector_store(text_chunks):
    """Embeded chunks and store them in ChromaDB for similarity search"""
    embeddings = HuggingFaceEmbeddings(model_name = EMBEDDING_MODEL)
    vector_store = Chroma.from_documents(documents = text_chunks, embedding=embeddings)
    return vector_store


def ask_question(vector_store, user_question):
    """  """
    result = vector_store.similarity_search(query = user_question, k = 10)
    context = "\n\n".join (
        f"[{chunk.metadata.get('source_file', 'unknown')}]\n{chunk.page_content}"

        for chunk in result
    )

    llm = ChatAnthropic(model = MODEL, temperature=0.0)

    messages = [
        SystemMessage(content = "Answer using only the provided context, if the answer is not there, say you dont know, "
                                "mention which file the information came from."),
        HumanMessage(content = f"Context : \n{context} \n Question : {user_question}")
    ]

    response = llm.invoke(messages)

    return response.content




st.set_page_config(page_title = "Document Chatbot", page_icon = ":books:", layout = "wide")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None


st.title("Document Chatbot (RAG)")

with st.sidebar:
    st.subheader("Upload a PDF or TXT file")
    uploaded_files = st.file_uploader("", type = ["pdf", "txt"], accept_multiple_files = True)

    if st.button("Build a Knowledge base", use_container_width = True):
        if uploaded_files:
            with st.spinner("Loading, Chunking and Embedding files..."):
                all_docs = []
                for file in uploaded_files:
                    all_docs.extend(load_file(file))

                chunks = chunk_documents(all_docs)
                vector_store = build_vector_store(chunks)
                st.session_state.vector_store = vector_store
                st.session_state.messages = []
                st.success(f"Successfully loaded {len(uploaded_files)} files, {len(chunks)} chunks and embedded them in the vector store.")
        else:
            st.warning("Upload at least one file first!")

if not os.getenv("ANTHROPIC_API_KEY"):
    st.warning("Please set your ANTHROPIC_API_KEY in the .env file")

for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.write(msg['content'])

if prompt := st.chat_input("Ask me anything about the uploaded documents..."):
    if st.session_state.vector_store is None:
        st.warning("Please build a knowledge base first from the sidebar.")
    else:
        st.session_state.messages.append({"role" : "user", "content" : prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = ask_question(st.session_state.vector_store, prompt)
                st.write(answer)

        st.session_state.messages.append({"role" : "assistant", "content" : answer})
        

















