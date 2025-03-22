import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Final ADHS App")  # switch drive 

st.title("Meine erste Streamlit App")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Dana Schnekenburger (schned06@students.zhaw.ch)
- Katarina Djuric (djurikat@students.zhaw.ch)   

Unsere App unterstützt Menschen mit AD(H)S dabei, ihren Alltag strukturierter zu gestalten. Sie bietet einen Wochenplaner, To-Do-Listen und hilfreiche Tipps für eine bessere Organisation. Gleichzeitig hilft sie auch Angehörigen und Freunden, AD(H)S besser zu verstehen, iindem sie praktische Ratschläge und Einblicke vermittelt.
"""

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

# Seiten definieren
pages = {
   "Home": "Willkommen bei der AD(H)S App!",
   "Rechner": "Hier ist der Rechner.",
   "Wochenplaner": "Hier ist der Wochenplaner.",
   "To-Do-Listen": "Hier sind die To-Do-Listen.",
   "Tipps": "Hier sind hilfreiche Tipps."
}
# Aktuelle Seite aus Query-Parametern holen
query_params = st.query_params
if "page" in query_params:
   st.session_state.current_page = query_params["page"] if isinstance(query_params["page"], str) else query_params["page"][0]
else:
   if "current_page" not in st.session_state:
       st.session_state.current_page = "Home"
# Navigationstitel
st.title("Navigation")
# Buttons für Seiten erstellen
for page in pages.keys():
   if st.button(page):
       # Query-Parameter aktualisieren
       st.query_params = {"page": page}
       st.session_state.current_page = page
# Inhalt der aktuellen Seite anzeigen
st.subheader(st.session_state.current_page)
st.write(pages[st.session_state.current_page])


