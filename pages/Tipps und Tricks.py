# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously

import streamlit as st

st.title("Tipps und Tricks")

st.write("Diese Seite ist eine Unterseite der Startseite.")
