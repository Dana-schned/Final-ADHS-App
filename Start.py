import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
# DataManager initialisieren
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Final ADHS App")
st.title("Meine erste Streamlit App")
# Entwicklerinfo
"""
Diese App wurde von folgenden Personen entwickelt:
- Dana Schnekenburger (schned06@students.zhaw.ch)
- Katarina Djuric (djurikat@students.zhaw.ch)   
...
"""
# Daten laden
data_manager.load_app_data(
   session_state_key='data_df',
   file_name='data.csv',
   initial_value=pd.DataFrame(),
   parse_dates=['timestamp']
)
# Navigation
pages = {
  "Home": "Willkommen bei der AD(H)S App!",
  "Rechner": "Hier ist der Rechner.",
  "Wochenplaner": "Hier ist der Wochenplaner.",
  "To-Do-Listen": "Hier sind die To-Do-Listen.",
  "Tipps": "Hier sind hilfreiche Tipps."
}
query_params = st.query_params
if "page" in query_params:
   st.session_state.current_page = query_params["page"] if isinstance(query_params["page"], str) else query_params["page"][0]
else:
   if "current_page" not in st.session_state:
       st.session_state.current_page = "Home"
st.title("Navigation")
for page in pages.keys():
   if st.button(page):
       st.query_params = {"page": page}
       st.session_state.current_page = page
st.subheader(st.session_state.current_page)
st.write(pages[st.session_state.current_page])
# Beispiel-Button zum Speichern
if st.button("Speichern"):
   data_manager.save_all_data()
   st.success("Daten wurden gespeichert!")