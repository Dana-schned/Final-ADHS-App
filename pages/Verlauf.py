# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# ------------------------------------------------------------
# Verlauf der Verdünnungsrechner-Daten als Tabelle anzeigen

import streamlit as st
import pandas as pd

st.title("Verlauf der Verdünnungsrechner-Eingaben")

# Zugriff auf die gespeicherten Daten
data_df = st.session_state.get("data_df", pd.DataFrame())

# Prüfen, ob überhaupt Daten vorhanden sind
if data_df.empty:
    st.info("Keine gespeicherten Eingaben vorhanden. Bitte zuerst im Verdünnungsrechner etwas berechnen.")
    st.stop()

# Nur Einträge vom Typ "Verdünnungsrechner" anzeigen
verlauf_df = data_df[data_df["typ"] == "Verdünnungsrechner"]

if verlauf_df.empty:
    st.info("Es wurden noch keine Verdünnungsrechnungen durchgeführt.")
    st.stop()

# Sortieren nach Zeit, neueste oben
verlauf_df = verlauf_df.sort_values("timestamp", ascending=False)

# Tabelle anzeigen
st.dataframe(verlauf_df)
