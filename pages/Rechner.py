# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously

import streamlit as st
from utils.data_manager import DataManager
from datetime import datetime

st.title("Verdünnungsrechner")

with st.form(key='dilution_form'):
    C1 = st.number_input("Konzentrierte Menge in ml", min_value=0.0)
    V1 = st.number_input("Konzentration der Lösung in %", min_value=0.0, max_value=100.0)
    C2 = st.number_input("Gewünschte Konzentration in %", min_value=0.0, max_value=100.0)
    submit_button = st.form_submit_button(label='Berechnen')

if submit_button:
    st.write(f"Debug: C1={C1}, V1={V1}, C2={C2}")

    if C1 > 0 and C2 > 0:
        V2 = (C1 * V1) / C2
        st.write(f"Sie müssen {V2} ml der konzentrierten Lösung hinzufügen, um die gewünschte Konzentration zu erhalten.")

        result = (
            f"Konzentrierte Menge in ml (C1): {C1}\n"
            f"Konzentration der Lösung in % (V1): {V1}\n"
            f"Gewünschte Konzentration in % (C2): {C2}\n"
            f"Berechnetes Volumen (V2): {V2} ml"
        )

        # Dynamischer Dateiname mit Datum & Uhrzeit
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"Verdünnungsrechner_Ergebnis_{timestamp}.txt"

        # SWITCHdrive-Handler
        dm = DataManager(fs_protocol="webdav", fs_root_folder="Final ADHS App")
        handler = dm._get_data_handler()

        # 🟡 Neue Eingabe in Session-Tabelle hinzufügen
        new_record = {
            "timestamp": datetime.now(),
            "typ": "Verdünnungsrechner",
            "C1": C1,
            "V1": V1,
            "C2": C2,
            "V2": V2
        }
        dm.append_record("data_df", new_record)

        # Versuch, Ergebnisdatei zu speichern
        try:
            handler.save(filename, result)
            st.success("✅ Ergebnis wurde auf SWITCHdrive gespeichert.")
        except Exception as e:
            st.error("❌ Fehler beim Speichern auf SWITCHdrive:")
            st.exception(e)

        # Download-Button
        st.download_button(
            label="Ergebnisse herunterladen (txt)",
            data=result,
            file_name="Verdünnungsrechner.txt",
            mime="text/plain"
        )

    else:
        st.write("Bitte geben Sie gültige Werte ein.")
