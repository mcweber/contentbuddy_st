import pandas as pd
import pypdf
import io

def read_pdf_file(file_path: str = "") -> str:
    pdf_file = open(file_path, 'rb')
    pdf_reader = pypdf.PdfReader(pdf_file)
    pdf_text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_text += page.extract_text()
    return pdf_text

def read_pdf_streamlit(file_data: io.BytesIO) -> str:
    pdf_reader = pypdf.PdfReader(file_data)
    pdf_text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_text += page.extract_text()
    return pdf_text

def read_excel_file(file_path: str = "") -> str:
    df = pd.read_excel(file_path)
    df_json = df.to_json(orient='records')
    return df_json

def read_excel_streamlit(file_data: io.BytesIO) -> str:
    df = pd.read_excel(file_data)
    df_json = df.to_json(orient='records')
    return df_json