import random
import streamlit as st

# Liste der Teilnehmer
teilnehmer = ["Rabea", "Vincent", "Lita", "Nik", "Anna", "Yannick"]

# Funktion zum Aufteilen der Teilnehmer in Gruppen
def gruppen_einteilung(teilnehmer_liste, restriktionen):
    # Zufällige Anordnung der Teilnehmer
    random.shuffle(teilnehmer_liste)
    gruppen = {"Vorspeise": [], "Hauptspeise": [], "Nachspeise": []}
    # Einteilung der Teilnehmer in Gruppen
    for i, teilnehmer in enumerate(teilnehmer_liste):
        gruppen_name = list(gruppen.keys())[i % 3]
        # Überprüfung der Restriktionen
        while restriktionen.get(teilnehmer) and any([r in gruppen[gruppen_name] for r in restriktionen[teilnehmer]]):
            random.shuffle(teilnehmer_liste)
            gruppen_name = list(gruppen.keys())[i % 3]
        # Hinzufügen des Teilnehmers zur Gruppe
        gruppen[gruppen_name].append(teilnehmer)
    return gruppen

# Benutzeroberfläche mit Streamlit erstellen
st.title("Teilnehmer Auslosung")

# Checkbox zur Aktivierung der Restriktionen
restriktionen_aktiviert = st.checkbox("Restriktionen aktivieren")

# Anzeige der Teilnehmer
st.header("Teilnehmer")
st.write(", ".join(teilnehmer))

# Button zur Auslosung der Gruppen
if st.button("Auslosung starten"):
    restriktionen = {}
    # Festlegen der Restriktionen, falls aktiviert
    if restriktionen_aktiviert:
        restriktionen = {
            "Rabea": ["Vincent"],
            "Vincent": ["Rabea"],
            "Lita": ["Nik"],
            "Nik": ["Lita"],
            "Anna": ["Yannick"],
            "Yannick": ["Anna"]
        }
    # Auslosung der Gruppen
    gruppen = gruppen_einteilung(teilnehmer, restriktionen)
    # Anzeige der Gruppen
    st.header("Gruppen")
    for gruppen_name, teilnehmer_liste in gruppen.items():
        st.subheader(gruppen_name)
        st.write(", ".join(teilnehmer_liste))
