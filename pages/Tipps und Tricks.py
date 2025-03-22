# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously

import streamlit as st

# Initialisierung der Favoriten im session_state als Dictionary (Schlüssel = Thema, Wert = Favorit-Status)
if "favoriten" not in st.session_state:
    st.session_state.favoriten = {
        "Struktur": False,
        "Zeitmanagement": False,
        "Priorisierung": False,
        "Organisation": False,
        "Routinen": False
    }

# Funktion zum Hinzufügen von Themen zu den Favoriten
def toggle_favorites(topic):
    # Toggle des Favoritenstatus (True/False)
    if st.session_state.favoriten.get(topic):
        st.session_state.favoriten[topic] = False
        st.success(f"{topic} wurde aus deinen Favoriten entfernt.")
    else:
        st.session_state.favoriten[topic] = True
        st.success(f"{topic} wurde zu deinen Favoriten hinzugefügt.")

# Navigationsleiste für Seiten
page = st.selectbox("Wähle eine Seite", ["Tipps und Tricks", "Favoriten"])

# Seite 1: Tipps und Tricks
if page == "Tipps und Tricks":
    st.write("Der Alltag mit AD(H)S kann herausfordernd sein. Hier sind einige Tipps und Tricks, die Ihnen helfen können:")

    st.write("### 1. Struktur")
    st.write("Erstelle dir klar strukturierte Tagesabläufe und Wochenpläne. So behältst du den Überblick und kannst dich besser organisieren. Fokussiere dich auf das Wesentliche und unterteile deine Aufgaben in kleine Schritte.")
    if st.button("Favorisieren: Struktur"):
        toggle_favorites("Struktur")

    st.write("### 2. Zeitmanagement")
    st.write("Lerne, wie du deine Zeit besser einteilen kannst, um effizienter zu arbeiten. Verwende Techniken wie die Pomodoro-Methode oder setze dir klare Deadlines.")
    if st.button("Favorisieren: Zeitmanagement"):
        toggle_favorites("Zeitmanagement")

    st.write("### 3. Priorisierung")
    st.write("Setze dir Prioritäten, damit du wichtige Aufgaben zuerst erledigst und dich nicht von unwichtigen Dingen ablenken lässt.")
    if st.button("Favorisieren: Priorisierung"):
        toggle_favorites("Priorisierung")

    st.write("### 4. Organisation")
    st.write("Verwende To-Do-Listen und andere Hilfsmittel, um deine Aufgaben zu organisieren und nichts zu vergessen.")
    if st.button("Favorisieren: Organisation"):
        toggle_favorites("Organisation")

    st.write("### 5. Routinen")
    st.write("Entwickle feste Routinen, um deinen Tag vorhersehbar zu gestalten und deine Energie besser zu nutzen.")
    if st.button("Favorisieren: Routinen"):
        toggle_favorites("Routinen")

    # Link zu den Favoriten
    st.markdown("[Zu deinen Favoriten](?page=favoriten)")
