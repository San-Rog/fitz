import streamlit as st
import zipfile
import io
import calendar

def compress_files(uploaded_files):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for uploaded_file in uploaded_files:
            zip_file.writestr(uploaded_file.name, uploaded_file.read())
    zip_buffer.seek(0)
    return zip_buffer

st.title("Compactador de Arquivos Streamlit")
uploaded_files = st.file_uploader('Selecionar arquivos PDF', type=['pdf'], accept_multiple_files=True)
if uploaded_files:
    if st.button("Compactar"):
        try:
            zip_file = compress_files(uploaded_files)
            st.download_button(
                label="Baixar arquivo ZIP",
                data=zip_file,
                file_name="compactado.zip",
                mime="application/zip"
            )
        except Exception as e:
            st.error(f"Erro ao compactar os arquivos: {e}")
text_calendar = calendar.TextCalendar()
st.write(text_calendar.pryear(2024))
