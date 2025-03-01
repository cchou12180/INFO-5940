import streamlit as st
from openai import OpenAI
from os import environ
import PyPDF2
import io

# Title Section
st.title("📝 File Q&A with OpenAI")

# File Upload Section - Support for .txt and .pdf Files
uploaded_files = st.file_uploader("Upload one or more documents", type=("txt", "pdf"), accept_multiple_files=True)

question = st.chat_input(
    "Ask something about the documents",
    disabled=not uploaded_files,
)

# Maintain session history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Ask something about the documents."}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Function to extract text from uploaded documents
def extract_text(file):
    if file.type == "text/plain":  # Handling .txt files
        return file.read().decode("utf-8")
    elif file.type == "application/pdf":  # Handling .pdf files
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
        text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        return text
    return ""

# Process uploaded files
if question and uploaded_files:
    file_contents = "".join([extract_text(file) for file in uploaded_files])
    
    client = OpenAI(api_key=environ['OPENAI_API_KEY'])
    
    # Append the user's question to the session messages
    st.session_state.messages.append({"role": "user", "content": question})
    st.chat_message("user").write(question)
    
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="openai.gpt-4o",  # Ensure using a valid OpenAI model
            messages=[
                {"role": "system", "content": f"Here's the content of the uploaded documents:\n\n{file_contents}"},
                *st.session_state.messages
            ],
            stream=True
        )
        response = st.write_stream(stream)
    
    # Append the assistant's response to the session messages
    st.session_state.messages.append({"role": "assistant", "content": response})




