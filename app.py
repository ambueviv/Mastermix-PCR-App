# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:53:00 2023

@author: vivie
"""

import streamlit as st
import pandas as pd

# Titel und Beschreibung anzeigen
st.title('PCR Step-by-Step Anleitung')
st.markdown('Dieses Programm führt Sie Schritt für Schritt durch den praktischen Ablauf einer PCR. Haben Sie einen Schritt ausgeführt, bestätigen Sie den Task mit einem Haken. Danach wird der nächste Schritt freigeschaltet.')

# Verlauf der abgeschlossenen Versuche speichern
completed_runs = []

# Funktion zur Berechnung der Ergebnisse
def calculate(x):
    # Berechnungen mit x durchführen
    result1 = x * 5
    result2 = x * 1
    result3 = x * 2
    result4 = x * 2
    result5 = x * 1
    result6 = x * 4
    result7 = x * 1 
    result8 = (max(x * 50 - (result1 + result2 + result3 + result4 + result5 + result6 + result7), 0))
    
    return result1, result2, result3, result4, result5, result6, result7, result8

# Neue Funktion zur Überprüfung des Fortschritts
def check_progress(step_num, checked):
    """
    Diese Funktion überprüft, ob der vorherige Schritt abgeschlossen wurde.
    Wenn ja, wird der aktuelle Schritt freigeschaltet.
    """
    if checked:
        next_step = step_num + 1
        st.write("Schritt", next_step, "ist jetzt freigeschaltet.")
    else:
        st.write("Bitte zuerst den vorherigen Schritt abschließen.")

# Neue Funktion zur Anzeige des Verlaufs der abgeschlossenen Versuche
def show_completed_runs():
    """
    Diese Funktion zeigt den Verlauf der abgeschlossenen Versuche an.
    """
    if len(completed_runs) == 0:
        st.write("Es wurden noch keine Versuche abgeschlossen.")
    else:
        st.write("Verlauf der abgeschlossenen Versuche:")
        for i, results in enumerate(completed_runs):
            st.write("Versuch", i+1, "für", len(results), "Proben:", results)

# Seitenlayout mit Streamlit
page = st.sidebar.radio("Seite auswählen:", ("Anleitung", "Letzter abgeschlossener Versuch"))

if page == "Anleitung":
    # Anleitung für das Beschriften der Testtubes anzeigen
    st.markdown("Für deine PCR brauchst du für jede Probe ein eigenes Test-Tube. Stelle für jede deiner Proben ein Test-Tube bereit und beschrifte sie entsprechend.")
    # Schritt 1: PCR Puffer pipettieren
    x = st.number_input("Anzahl Proben:", min_value=1, max_value=100, value=1)
    results = calculate(x)
    checkbox1 = st.checkbox("Schritt 1: PCR Puffer pipettieren")
    st.write("Für deine Anzahl Proben werden insgesamt", results[0], "Mikroliter PCR Puffer benötigt. Davon pipettierst du je 5 Mikroliter in jedes Testtube.")
    if checkbox1:
        # Schritt 2: dNTP pipettieren
        checkbox2 = st.checkbox("Schritt 2: dNTP pipettieren")
        st.write("Für deine Anzahl Proben werden insgesamt", results[1], "Mikroliter dNTP benötigt. Davon pipettierst du je 1 Mikroliter in jedes Testtube.")
        if checkbox2:
            # Schritt 3: Vorwärtsprimer pipettieren
            checkbox3 = st.checkbox("Schritt 3: Vorwärtsprimer pipettieren")
            st.write("Für deine Anzahl Proben werden insgesamt", results[2], "Mikroliter Vorwärtsprimer benötigt. Davon pipettierst du je 2 Mikroliter in jedes Testtube.")
            if checkbox3:
                # Schritt 4: Rückwärtsprimer pipettieren
                checkbox4 = st.checkbox("Schritt 4: Rückwärtsprimer pipettieren")
                st.write("Für deine Anzahl Proben werden insgesamt", results[3], "Mikroliter Rückwärtsprimer benötigt. Davon pipettierst du je 2 Mikroliter in jedes Testtube.")
                if checkbox4:
                    # Schritt 5: Template hinzufügen
                    checkbox5 = st.checkbox("Schritt 5: Template hinzufügen")
                    st.write("Für deine Anzahl Proben werden insgesamt", results[4], "Mikroliter Template benötigt. Davon pipettierst du je 1 Mikroliter in jedes Testtube.")
                    if checkbox5:
                        # Schritt 6: Taq Polymerase hinzufügen
                        checkbox6 = st.checkbox("Schritt 6: Taq Polymerase hinzufügen")
                        st.write("Für deine Anzahl Proben werden insgesamt", results[5], "Mikroliter Taq Polymerase benötigt. Davon pipettierst du je 4 Mikroliter in jedes Testtube.")
                        if checkbox6:
                            # Schritt 7: Wasser hinzufügen
                            checkbox7 = st.checkbox("Schritt 7: Wasser hinzufügen")
                            st.write("Für deine Anzahl Proben werden insgesamt", results[6], "Mikroliter Wasser benötigt. Davon pipettierst du je 1 Mikroliter in jedes Testtube.")
                            if checkbox7:
                                # Schritt 8: PCR durchführen
                                checkbox8 = st.checkbox("Schritt 8: PCR durchführen")
                                st.write("Deine PCR ist nun bereit für den nächsten Schritt.")
                                if checkbox8:
                                    save_data(completed_runs)
                                    st.write("Du hast die PCR für", x, "Proben erfolgreich durchgeführt.")

def load_data():
    with open('completed_runs.json', 'r') as f:
        data = json.load(f)
    return data

if page == "Letzter abgeschlossener Versuch":
    data = load_data()
    if data:
        st.write("Letzter abgeschlossener Versuch:")
        st.write(pd.DataFrame(data[-1], columns=["PCR Puffer", "dNTP", "Vorwärtsprimer", "Rückwärtsprimer", "Template", "Taq Polymerase", "Wasser", "Restvolumen"]))
    else:
        st.write("Es wurden noch keine Versuche abgeschlossen.")
