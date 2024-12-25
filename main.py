from datetime import datetime
import streamlit as st
import ask_llm
import ask_doc
import scrape_web
import prompts

import os
from dotenv import load_dotenv
load_dotenv()

# Define Constants ---------------------------------------------------
VERSION = "25.12.2024"
HEUTE = str(datetime.now().date())
AUSGABE_SPRACHE = ["DEU", "ENG", "FRA"]
LLMS = ["gemini", "gpt4o", "gpt4omini", "llama"]
# LLM = "gemini" # ONLINE: gemini, gpt4o, gpt4omini, llama | LOCAL: llama, mistral
OUTPUT_FORMATS = ["text", "json"]
LOCAL = False

# Functions -------------------------------------------------------------
@st.dialog("Code Eingabe")
def login_code_dialog() -> None:
    code = st.text_input(label="Code", type="password")
    if st.button("Enter"):
        stored_code = os.environ.get('CODE')
        if stored_code is None:
            st.error("Umgebungsvariable CODE ist nicht gesetzt.")
        elif code == stored_code:
            st.success("Code is correct.")
            st.session_state.code = True
            st.rerun()
        else:
            st.error("Code is not correct.")

# Main -----------------------------------------------------------------
def main() -> None:
    st.set_page_config(page_title='ContentBuddy', layout='wide')

    # Initialize Session State -----------------------------------------
    if 'init' not in st.session_state:
        st.session_state.init: bool = True
        st.session_state.code: bool = False
        st.session_state.eingabe: str = ""
        st.session_state.ausgabe: str = ""
        st.session_state.model_idx: int = 0
        st.session_state.output_format_idx: int = 0
        st.session_state.search_status: bool = False
        st.session_state.system_prompt: str = prompts.get_system_prompt()
        st.session_state.format_prompt: str = ""
        st.session_state.ausgabe_sprache_idx: int = 0

    # Authentication ---------------------------------------------------
    if st.session_state.code == False:
        login_code_dialog()

    # Initialize screen sections -------------------------------------------
    st.subheader("ContentBuddy")

    col_left, col_mid, col_right = st.columns([4, 1, 4])

    container_left = col_left.container(border=True, height=800)
    container_mid = col_mid.container(border=True, height=800)
    container_right = col_right.container(border=True, height=800)

    with container_left:
        st.subheader("EINGABE")
    with container_mid:
        st.subheader("FORMAT")
    with container_right:
        st.subheader("AUSGABE")

    # with footer:
    st.write(f"Version: {VERSION} M. Weber | Status: POC | LLM: {LLMS[st.session_state.model_idx]} | Lokal: {LOCAL}")
    
    # Define Input Form ----------------------------------------------
    with container_left:

        # File Upload ---------------------------------------------------------
        with st.expander("Datei Upload", expanded=False):
            file_data = st.file_uploader(label="Datei Upload", type=["pdf", "xlsx"])
            if file_data:
                file_type = str(file_data.name)[-3:]
                if file_type == "pdf":
                    st.session_state.eingabe = ask_doc.read_pdf_streamlit(file_data)
                elif file_type == "lsx":
                    st.session_state.eingabe = ask_doc.read_excel_streamlit(file_data)
            else:
                st.session_state.eingabe = ""
                st.error("Keine Datei geladen.")

        # URL Upload ------------------------------------------------------
        with st.expander("Webseite Upload", expanded=False):
            url = st.text_input(label="Upload Web page:")
            if url:
                st.session_state.eingabe = scrape_web.scrape_web(url)
                st.success("Webseite geladen.")
            else:
                st.error("Keine Webseite geladen.")

        # Text Area ---------------------------------------------------------
        value_text = st.session_state.eingabe
        eingabe_text = st.text_area(label="Was sind die Quelltexte?", value=value_text, height=500)
        if eingabe_text != value_text:
            st.session_state.eingabe = eingabe_text

        # Reset Button ------------------------------------------------------
        if st.button("Reset"):
            st.session_state.eingabe = ""
            st.session_state.ausgabe = ""
            st.session_state.schlagworte = ""
            st.rerun()

    # Define Parameter Form ----------------------------------------------
    with container_mid:

        # Choose Prompt -----------------------------------------------------
        for item in prompts.get_prompt_names():
            if st.button(item):
                st.session_state.format_prompt = prompts.get_prompt_by_name(item)
                st.session_state.search_status = True

        # Choose LLM & Language & Output Format ---------------------------------------------
        ausgabe_sprache_neu = st.radio("Ausgabe-Sprache", AUSGABE_SPRACHE, index=st.session_state.ausgabe_sprache_idx)
        if ausgabe_sprache_neu != AUSGABE_SPRACHE[st.session_state.ausgabe_sprache_idx]:
            st.session_state.ausgabe_sprache_idx = AUSGABE_SPRACHE.index(ausgabe_sprache_neu)
            st.rerun()

        model_neu = st.radio("Modell", LLMS, index=st.session_state.model_idx)
        if model_neu != LLMS[st.session_state.model_idx]:
            st.session_state.model_idx = LLMS.index(model_neu)
            st.rerun()

        output_neu = st.radio("Output", OUTPUT_FORMATS, index=st.session_state.output_format_idx)
        if output_neu != OUTPUT_FORMATS[st.session_state.output_format_idx]:
            st.session_state.output_format_idx = OUTPUT_FORMATS.index(output_neu)
            st.rerun()

    # Execute Search & Display Ausgabe -------------------------------------------
    if st.session_state.search_status and st.session_state.eingabe:
        prompt = f"#{AUSGABE_SPRACHE[st.session_state.ausgabe_sprache_idx]}\n\n {st.session_state.format_prompt}"
        llm_handler = ask_llm.LLMHandler(llm=LLMS[st.session_state.model_idx], local=LOCAL)
        
        st.session_state.ausgabe = llm_handler.ask_llm(
            temperature=0.2,
            question=prompt,
            # history=st.session_state.history,
            system_prompt=st.session_state.system_prompt,
            # web_results_str=st.session_state.web_results,
            source_doc_str=st.session_state.eingabe,
            )
        
        with container_right:
            if OUTPUT_FORMATS[st.session_state.output_format_idx] == "json":
                st.json(st.session_state.ausgabe)
            else:
                st.write(st.session_state.ausgabe)
        
        st.session_state.search_status = False

if __name__ == "__main__":
    main()
