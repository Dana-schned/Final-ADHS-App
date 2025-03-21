import streamlit as st
from utils.data_manager import DataManager

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

        result = f"Konzentrierte Mende in ml (C1): {C1}\nKonzentration der Lösung in % (V1): {V1}\nGewünschte Konzentration in % (C2): {C2}\nMenge der konzentrierten Lösung in ml (V2): {V2}"
        result += f"\nBerechnetes Volumen (V2): {V2}L"

        st.download_button(
            label= "Ergebnisse herunterladen (txt)",
            data=result,
            file_name="Verdünnungsrechner.txt",
            mime="text/plain")
    else:
        st.write("Bitte geben Sie gültige Werte ein.")


