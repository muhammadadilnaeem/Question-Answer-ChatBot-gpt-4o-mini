# Conversational Q&A Chatbot

# Import libraries
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage # importing message types from langchain schem class to create messages in streamlit  
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI 
import os
from dotenv import load_dotenv
load_dotenv()

# Load your API key from an environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI Code
st.set_page_config(page_title="🧠 Simple Q & A Bot 🤖", page_icon=":robot:")
st.markdown("<h1>Conversational Q&A Chatbot 🏁</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask your queries about any topic related to Python or any programming language.</p>", unsafe_allow_html=True)

# Custom CSS for styling
st.markdown(
    """
    <style>
    h1 {
        color: #3498db;
        text-align: center;
    }
    h3 {
        color: #2ecc71;
    }
    .stTextInput>div>div>input {
        font-size: 20px;
        height: 50px; /* Height for larger input box */
        width: 100%;
        padding: 0; /* Remove padding */
        border-radius: 0; /* Remove border radius */
        border: 1px solid #ccc; /* Remove shadow */
        box-shadow: none; /* Remove shadow */
        text-align: center; /* Center the placeholder text */
        transition: all 0.2s ease;
    }
    .stTextInput>div>div>input::placeholder {
        color: #999;
    }
    .stTextInput>div>div>input:focus {
        border-color: #3498db;
        outline: 0;
        box-shadow: none;
    }
    .stButton>button {
        background-color: #e74c3c;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 10px auto;
        cursor: pointer;
        border-radius: 4px;
        display: block;
        transition: background-color 0.3s, color 0.3s;
    }
    .stButton>button:hover {
        background-color: #c0392b;
        color: white;
    }
    /* Dark mode styling */
    body.dark-mode {
        background-color: #333;
        color: #fff;
    }
    body.dark-mode h1 {
        color: #3498db;
    }
    body.dark-mode h3 {
        color: #2ecc71;
    }
    body.dark-mode .stTextInput>div>div>input {
        background-color: #444;
        color: #fff;
        border: 1px solid #555;
    }
    body.dark-mode .stTextInput>div>div>input:focus {
        border-color: #3498db;
        box-shadow: none;
    }
    body.dark-mode .stButton>button {
        background-color: #e74c3c;
        color: #fff;
    }
    body.dark-mode .stButton>button:hover {
        background-color: #c0392b;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Let's create a chat model
chat = ChatOpenAI(
    temperature=0.5, 
    openai_api_key=openai_api_key, 
    model_name="gpt-4o-mini"
)

if "flowmessages" not in st.session_state:
    st.session_state["flowmessages"] = [
        SystemMessage(content="You are a serious helpful assistant."),
    ]

# Define a function to get the response
def get_openai_response(question):
    st.session_state["flowmessages"].append(HumanMessage(content=question))
    answer = chat.invoke(st.session_state["flowmessages"])
    st.session_state["flowmessages"].append(AIMessage(content=answer.content))
    return answer.content

# Input and button for user interaction
input_text = st.text_input("Question", placeholder="Enter Your Question Here 🤔", label_visibility="collapsed", key="input")
submit = st.button("Submit ✅")

# Display the response
if submit:
    response = get_openai_response(input_text)
    st.markdown("<h3 style='color:#2ecc71;'>The Response of gpt-4o-mini is 📝</h3>", unsafe_allow_html=True)
    st.write(response)
