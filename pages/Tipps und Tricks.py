# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously

import streamlit as st

st.title("Tipps und Tricks")

st.write("Diese Seite ist eine Unterseite der Startseite.")

import streamlit as st

# Beispiel-Tipps und Tricks
tips = [
    {"title": "Planung und Struktur", "content": "Nutze ein digitales Kalender-Tool, um deine Aufgaben zu organisieren."},
    {"title": "Kurze Pausen machen", "content": "Mache regelmäßig kurze Pausen, um deine Konzentration aufrechtzuerhalten."},
    {"title": "Bewegung", "content": "Regelmäßige Bewegung hilft, die Konzentration zu verbessern."},
    {"title": "Aufgaben in kleine Schritte unterteilen", "content": "Große Aufgaben in kleinere, überschaubare Schritte aufteilen."},
    {"title": "Vermeide Ablenkungen", "content": "Reduziere Ablenkungen, z.B. durch das Abschalten von Benachrichtigungen."}
]

# Initialisiere 'favoriten' in session_state, wenn noch nicht vorhanden
if "favoriten" not in st.session_state:
    st.session_state.favoriten = []

def favorisieren(tip):
    """Fügt einen Tipp zu den Favoriten hinzu, wenn er noch nicht favorisiert wurde."""
    if tip not in st.session_state.favoriten:
        st.session_state.favoriten.append(tip)
        st.success(f"{tip['title']} wurde zu deinen Favoriten hinzugefügt!")
    else:
        st.warning(f"{tip['title']} ist bereits in deinen Favoriten.")

def tipps_und_tricks():
    st.title("ADHS Tipps & Tricks")
    st.write("Hier findest du nützliche Tipps, die dir helfen können, mit ADHS besser umzugehen.")
    
    for tip in tips:
        st.subheader(tip["title"])
        st.write(tip["content"])
        
        # Favorisieren Button
        if st.button(f"Favorisieren: {tip['title']}", key=tip['title']):
            favorisieren(tip)
