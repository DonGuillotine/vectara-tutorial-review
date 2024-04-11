import os
import time
import json
import logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import streamlit as st
from streamlit_chat import message
from injest import create_corpus, upload_file, save_to_dir


logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)

st.set_page_config(page_title="Vectara Chat Essentials", page_icon="💬")


st.title("Vectara Chat Essentials 🤖")

st.markdown("""
    Welcome to 'Vectara Chat Essentials: A Developer's Guide to Next-Gen Chatbots' 🌟.
    This tutorial offers a deep dive into building and enhancing chatbots using the innovative Vectara platform,
    equipped with the latest in AI and conversational intelligence. 🧠💬
    Whether you are a beginner or an advanced developer, this guide will take you through all the steps
    from creating your first chatbot to deploying sophisticated AI-driven conversational agents.
    Let's embark on this exciting journey! 🚀
    """)

if st.button("Start Using Now!"):
    st.snow()
    st.write(
        "Great! Let's dive into the world of conversational AI with Vectara Chat. 🎉"
    )

if "corpus_number" not in st.session_state:
    st.session_state["corpus_number"] = None

with st.sidebar:
    st.session_state["vectara_api_key"] = st.text_input("Vectara API Key")
    st.session_state["serper_api_key"]= st.text_input("Serper API Key (for research)")
    vectara_customer_id = st.text_input("Vectara Customer ID")
    corpus_name = st.text_input("Corpus Name (optional)")
    corpus_description = st.text_input("Corpus Description (optional)")
    file = st.file_uploader("Upload a file (optional)", type=["text", "pdf"])

    if st.button("Submit") and file:
        corpus_number, _ = create_corpus(
            st.session_state["vectara_api_key"],
            vectara_customer_id,
            corpus_name,
            corpus_description,
        )

        if corpus_number is not None:
            st.session_state["corpus_number"] = corpus_number
            file_path = save_to_dir(file)
            upload_file(
                st.session_state["vectara_api_key"],
                vectara_customer_id,
                corpus_number,
                file_path,
            )
            st.success("File uploaded successfully!")
        else:
            st.error("Failed to create corpus. Please check your inputs.")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

with st.form("chat_input", clear_on_submit=True):
    user_prompt = st.text_input("Your message:", label_visibility="collapsed")

    if st.form_submit_button("Send"):
        st.session_state.messages.append({"role": "user", "content": user_prompt})