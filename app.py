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