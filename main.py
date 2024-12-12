# ---------------------------------------------------
VERSION = "12.12.2024"
# Author: M. Weber
# ---------------------------------------------------
# ---------------------------------------------------

from datetime import datetime
import streamlit as st
import ask_llm
import ask_doc
import scrape_web
import prompts

# Define Constants ---------------------------------------------------
HEUTE = str(datetime.now().date())
AUSGABE_SPRACHE = ["DEU", "ENG", "FRA"]
LLM = "gpt4o" # ONLINE: gpt4o, gpt4omini, llama3 | LOCAL: llama3, mistral
LOCAL = False

# Main -----------------------------------------------------------------
def main() -> None:

    # Initialize screen sections -------------------------------------------
    st.set_page_config(page_title='ContentBuddy', layout='wide')
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
    st.write(f"Version: {VERSION} M. Weber | Status: POC | LLM: {LLM} | Lokal: {LOCAL}")
    
    # Initialize Session State -----------------------------------------
    if 'init' not in st.session_state:
        st.session_state.init: bool = True
        st.session_state.eingabe: str = ""
        st.session_state.ausgabe: str = ""
        # st.session_state.schlagworte: str = ""
        st.session_state.search_status: bool = False
        st.session_state.system_prompt: str = prompts.SYSTEM_PROMPT
        st.session_state.format_prompt: str = ""
        st.session_state.zielformat: str = ""
        st.session_state.ausgabe_sprache_idx: int = 0

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
            # st.session_state.search_status = False

        # Reset Button ------------------------------------------------------
        if st.button("Reset"):
            st.session_state.eingabe = ""
            st.session_state.ausgabe = ""
            st.session_state.schlagworte = ""
            # st.session_state.search_status = False
            st.rerun()
   
    # Define Parameter Form ----------------------------------------------
    with container_mid:
        if st.button("Fachartikel"):
            st.session_state.zielformat = "Fachartikel"
            st.session_state.format_prompt = prompts.FACHARTIKEL
            st.session_state.search_status = True
        if st.button("Blogbeitrag"):
            st.session_state.zielformat = "Blogbeitrag"
            st.session_state.format_prompt = prompts.BLOGBEITRAG
            st.session_state.search_status = True
        if st.button("Social Media Post"):
            st.session_state.zielformat = "Social Media Post"
            st.session_state.format_prompt = prompts.SOCIAL_MEDIA_POST
            st.session_state.search_status = True
        if st.button("Schlagworte"):
            st.session_state.zielformat = "Schlagworte"
            st.session_state.format_prompt = prompts.SCHLAGWORTE
            st.session_state.search_status = True
        if st.button("Pressemitteilung"):
            st.session_state.zielformat = "Pressemitteilung"
            st.session_state.format_prompt = prompts.PRESSEMITTEILUNG
            st.session_state.search_status = True

        sprache = AUSGABE_SPRACHE[st.session_state.ausgabe_sprache_idx]
        index = st.session_state.ausgabe_sprache_idx
        
        ausgabe_sprache_neu = st.radio(f"Ausgabe-Sprache ({sprache})", AUSGABE_SPRACHE, index=index)
        if ausgabe_sprache_neu != sprache:
            st.session_state.ausgabe_sprache_idx = AUSGABE_SPRACHE.index(ausgabe_sprache_neu)
            st.rerun()

    # Execute Search & Display Ausgabe -------------------------------------------
    if st.session_state.search_status and st.session_state.eingabe:
        prompt = f"#{AUSGABE_SPRACHE[st.session_state.ausgabe_sprache_idx]}\n\n {st.session_state.format_prompt}"
        llm_handler = ask_llm.LLMHandler(llm=LLM, local=LOCAL)
        st.session_state.ausgabe = llm_handler.ask_llm(
            temperature=0.2,
            question=prompt,
            # history=st.session_state.history,
            systemPrompt=st.session_state.system_prompt,
            # web_results_str=st.session_state.web_results,
            source_doc_str=st.session_state.eingabe,
            )
        with container_right:
            st.write(st.session_state.ausgabe)
        st.session_state.zielformat = ""
        st.session_state.search_status = False

if __name__ == "__main__":
    main()
