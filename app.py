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