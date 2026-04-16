import streamlit as st
import time

# 1. Seiten-Konfiguration
st.set_page_config(page_title="63811 - Einführung in die Imperative Programmierung", page_icon="🎓")

if 'step' not in st.session_state:
    st.session_state.step = 1

# --- DIE FAKE-UNI UI (Wird nur am Anfang angezeigt) ---
if st.session_state.step <= 4:
    st.title("63811 - Einführung in die Imperative Programmierung")
    st.subheader("Kapitel 4: Primitive Datentypen")
    st.caption("Matrikelnummer: q1250507 | Studienjahr:Sommersemester 2026 | Sitzung läuft ab in: 14:59")
    st.divider()

# --- DIE ECHTE UI (Nach dem System-Neustart) ---
if st.session_state.step >= 5:
    st.title("Das Ultimative 'Herde'-Quiz 🕵️‍♀️✨")
    st.write("🎧 **Okay, der langweilige Teil ist vorbei. Klick auf Play für die richtige Stimmung!**")
    try:
        st.audio("song.mp3")
    except FileNotFoundError:
        st.warning("⚠️ Bitte lege eine Datei namens 'song.mp3' in denselben Ordner!")
    st.divider()

# ==========================================
# TEIL 1: DIE LANGWEILIGEN INFORMATIK-FRAGEN
# ==========================================

# --- FRAGE 1 ---
if st.session_state.step == 1:
    st.subheader(
        "Frage 1: Wie hoch ist die durchschnittliche Zeitkomplexität für eine Suchoperation in einer Hash-Tabelle?")
    q1_answer = st.radio("Wählen Sie die korrekte Big-O-Notation:",
                         ["O(n)", "O(log n)", "O(1)", "O(n²)"], index=None)

    if st.button("Antwort einreichen"):
        if q1_answer == "O(1)":
            st.success("System: Korrekt. Fortfahren...")
            time.sleep(1.5)
            st.session_state.step = 2
            st.rerun()
        elif q1_answer == None:
            st.warning("Systemwarnung: Sie müssen eine Antwort auswählen.")
        else:
            st.error("System: Falsch. Bitte erneut versuchen.")

# --- FRAGE 2 ---
elif st.session_state.step == 2:
    st.subheader(
        "Frage 2: Was ist der primäre Zweck eines 'Foreign Key' (Fremdschlüssel) in einer relationalen Datenbank?")
    q2_answer = st.radio("Wählen Sie die zutreffende Aussage:",
                         ["Daten verschlüsseln",
                          "Eine Verbindung zwischen Daten in zwei Tabellen herstellen",
                          "Die Datenbankgeschwindigkeit verdoppeln",
                          "Speicherplatz freigeben"], index=None)

    if st.button("Antwort einreichen"):
        if q2_answer == "Eine Verbindung zwischen Daten in zwei Tabellen herstellen":
            st.success("System: Korrekt. Fortfahren...")
            time.sleep(1.5)
            st.session_state.step = 3
            st.rerun()
        elif q2_answer == None:
            st.warning("Systemwarnung: Sie müssen eine Antwort auswählen.")
        else:
            st.error("System: Falsch. Bitte erneut versuchen.")

# --- FRAGE 3 ---
elif st.session_state.step == 3:
    st.subheader("Frage 3: Welcher dieser HTTP-Statuscodes steht für 'Not Found' (Nicht gefunden)?")
    q3_answer = st.radio("Wählen Sie den korrekten Code:",
                         ["200", "404", "500", "301"], index=None)

    if st.button("Antwort einreichen"):
        if q3_answer == "404":
            st.success("System: Korrekt. Vorbereitung auf die letzte Modulfrage...")
            time.sleep(1.5)
            st.session_state.step = 4
            st.rerun()
        elif q3_answer == None:
            st.warning("Systemwarnung: Sie müssen eine Antwort auswählen.")
        else:
            st.error("System: Falsch. Bitte erneut versuchen.")

# --- FRAGE 4: DER GLITCH (Kaffee-Frage) ---
elif st.session_state.step == 4:
    st.subheader(
        "Frage 4: Welche der folgenden Methoden ist bei der Fehlersuche (Debugging) in einer komplexen Anwendung am effizientesten?")
    q4_answer = st.radio("Wählen Sie den besten Ansatz:",
                         ["Logdateien analysieren",
                          "Unit-Tests schreiben",
                          "Den Laptop zuklappen und mit mir kuscheln",
                          "Den Code komplett löschen"], index=None)

    # Hier bauen wir den extrem prominenten Systemfehler ein
    glitch_container = st.empty()

    if glitch_container.button("Antwort einreichen"):
        if q4_answer == "Den Laptop zuklappen und mit mir kuscheln":
            # Der dramatische Glitch-Effekt
            glitch_container.error("🚨 KRITISCHER FEHLER: UNBEKANNTER PARAMETER ERKANNT 🚨")
            time.sleep(4)
            glitch_container.warning("⚠️ SYSTEM-ÜBERLASTUNG... BRECHE PRÜFUNG AB...")
            time.sleep(4)
            glitch_container.info("🔄 INITIALLISIERE NEUES PROTOKOLL: 'Echte Fragen' werden geladen...")
            time.sleep(4)
            st.balloons()  # Ein kleiner Konfetti-Schock zum Übergang
            st.session_state.step = 5
            st.rerun()
        elif q4_answer == None:
            st.warning("Systemwarnung: Sie müssen eine Antwort auswählen.")
        else:
            st.error("System: Falsch. Diese Methode ist ineffizient. Suchen Sie nach einer besseren Lösung.")


# ==========================================
# TEIL 2: DIE 5 PERSÖNLICHEN FRAGEN
# (Passe die Texte und Antworten hier für euch an!)
# ==========================================

# --- PERSÖNLICHE FRAGE 1 ---
elif st.session_state.step == 5:
    st.subheader("Frage 1: Was ist das? 🔴")
    q5_answer = st.radio("Sei ehrlich...", ["Ein roter Kreis ⭕", "Das offizielle Baybell Emoji 🔴", "Ein roter Ball 🏀","Keine Ahnung ❓"], index=None)

    if st.button("Bestätigen"):
        if q5_answer == "Das offizielle Babybel Emoji 🔴":
            st.success("Richtig. Das weiß doch jeder. 🏆")
            time.sleep(4);
            st.session_state.step = 6;
            st.rerun()
        else:
            st.error("Versuch es nochmal. 😘")

# --- PERSÖNLICHE FRAGE 2 ---
elif st.session_state.step == 6:
    st.subheader("Frage 2: Was war das allererste Gericht, das ich für dich gekocht habe? 🍝")
    q6_answer = st.radio("Erinnerst du dich?", ["Pizza 🍕", "Nudeln mit Soße 🍝", "Hänchencurry mit Ananas 🍍", "Ich kann gar nicht kochen 👨‍🍳"],
                         index=None)

    if st.button("Bestätigen"):
        if q6_answer == "Hänchencurry mit Ananas 🍍":  # Tausche dies mit eurer echten Antwort aus!
            st.success("Korrekt! Fünf Sterne für den Koch. ⭐")
            time.sleep(4);
            st.session_state.step = 7;
            st.rerun()
        else:
            st.error("Wow. Einfach wow. Falsch! 😂")

# --- PERSÖNLICHE FRAGE 3 ---
elif st.session_state.step == 7:
    st.subheader("Frage 3: Wo haben wir uns das erste Mal geküsst? 😘")
    q7_answer = st.radio("Überlege mal:",
                         ["Im Kino 🎥", "Wir haben uns noch nie geküsst, wir leben ja enthaltsam bis zur Ehe ⛪", "In den Weinbergen von Hochheim 🍇", "Im Park 🏞️"],
                         index=None)

    if st.button("Bestätigen"):
        if q7_answer == "In den Weinbergen von Hochheim 🍇":  # Tausche dies mit eurer echten Antwort aus!
            st.success("Ich wusste es! Das war seeeeeehr schön. 🥰")
            time.sleep(4);
            st.session_state.step = 8;
            st.rerun()
        else:
            st.error("Netter Versuch, aber wir beide wissen, dass das nicht die volle Wahrheit ist!")

# --- PERSÖNLICHE FRAGE 4 ---
elif st.session_state.step == 8:
    st.subheader("Frage 4: Wohin sind wir bei unserem ersten richtigen Date gegangen? 🗺️")
    q8_answer = st.radio("Denk gut nach...", ["Ins Kino 🎥", "Kaffee trinken ☕", "Spazieren im Park 🏞", "Tanzen 💃"],
                         index=None)

    if st.button("Bestätigen"):
        if q8_answer == "Tanzen 💃":  # Tausche dies mit eurer echten Antwort aus!
            st.success("Ganz genau. Der beste Tag überhaupt. ❤️")
            time.sleep(4);
            st.session_state.step = 9;
            st.rerun()
        else:
            st.error("Schlechte Antwort! Überleg nochmal.")

# --- PERSÖNLICHE FRAGE 5 ---
elif st.session_state.step == 9:
    st.subheader("Frage 5: Checkst du? 🙋‍♀️")
    q9_answer = st.radio("und?",
                         ["Häää ❓", "Ich checke 😎", "✂️", "Nein tu ich nicht ☠️"], index=None)

    if st.button("Bestätigen"):
        if q9_answer == "Ich checke 😎":  # Tausche dies mit eurer echten Antwort aus!
            st.success("Ich checke auch 😉")
            time.sleep(4);
            st.session_state.step = 10;
            st.rerun()
        else:
            st.error("Das glaubst du doch selbst nicht!")

# --- PERSÖNLICHE FRAGE 6 ---
elif st.session_state.step == 10:
    st.subheader("Frage 6: Schauen wir mal was wird. 🕰️")
    q9_answer = st.radio("und?",
                         ["Was wird. 🥸", "Was wird. Wir freuen uns. 🤩", "Wird was. 🤨", "Wir freuen uns. Was wird 🤓"], index=None)

    if st.button("Bestätigen"):
        if q9_answer == "Was wird. Wir freuen uns. 🤩":  # Tausche dies mit eurer echten Antwort aus!
            st.success("Ich freue mich auch 😉")
            time.sleep(4);
            st.session_state.step = 11;
            st.rerun()
        else:
            st.error("Das glaubst du doch selbst nicht!")


# ==========================================
# TEIL 3: DAS DRAMATISCHE FINALE (Schritt für Schritt)
# ==========================================

elif st.session_state.step == 11:
    st.subheader("Auswertung der Ergebnisse... 📊")
    st.divider()

    # Einen neuen State für die Klicks im Finale erstellen
    if "finale_step" not in st.session_state:
        st.session_state.finale_step = 1

    # Schritt 1
    if st.session_state.finale_step >= 1:
        st.markdown("#### Es sieht so aus, als hättest du bestanden...")

    if st.session_state.finale_step == 1:
        if st.button("Weiter ➡️", key="btn1"):
            st.session_state.finale_step = 2
            st.rerun()

    # Schritt 2
    if st.session_state.finale_step >= 2:
        st.markdown("#### ...aber du musst noch *eine letzte* Frage beantworten.")
        st.markdown("#### Diese Frage wird alles entscheiden.")

    if st.session_state.finale_step == 2:
        if st.button("Weiter ➡️", key="btn2"):
            st.session_state.finale_step = 3
            st.rerun()

    # Schritt 3
    if st.session_state.finale_step >= 3:
        st.markdown(
            "#### Eigentlich sollte es eine einfache Frage sein, aber pass auf, dass du richtig antwortest, sonst fällst du durch den Test.")

    if st.session_state.finale_step == 3:
        # Ein bisschen Abstand für die Dramatik
        st.write("")
        if st.button("Zeig mir die letzte Frage 🫣", use_container_width=True, key="btn3"):
            st.session_state.finale_step = 4
            st.rerun()

    # Schritt 4: Die große Frage
    if st.session_state.finale_step == 4:
        st.divider()
        st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Willst du meine Freundin sein? ♥️</h1>",
                    unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Ja! 🥰", use_container_width=True):
                st.balloons()
                st.success("Test zu 100% bestanden. Ich liebe dich! 🎉❤️")

        with col2:
            if st.button("Nein 💀", use_container_width=True):
                st.error("Kritischer Systemfehler: Diese Antwort ist ungültig. Bitte drücke den anderen Button. 🤖")
