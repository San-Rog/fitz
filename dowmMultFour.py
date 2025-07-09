import streamlit as st
import zipfile
import io
import calendar
from datetime import date, timedelta

def gerar_calendario_intervalo(data_inicio, data_fim):
    data_atual = data_inicio
    while data_atual <= data_fim:
        ano = data_atual.year
        mes = data_atual.month
        strMonthYear = f'{calendar.month_name[mes]} de {ano}: {calendar.monthrange(ano, mes)[1]} dias'
        st.write(strMonthYear)
        # Avança para o próximo mês
        if mes == 12:
            ano += 1
            mes = 1
        else:
            mes += 1
            data_atual = date(ano, mes, 1)
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
#st.write(list(calendar.month_name))
#st.write(calendar.calendar(2018))
#st.write(calendar.month(2025, 7))

# Exemplo de uso
data_inicial = date(2024, 1, 1)
data_final = date(2024, 3, 31)
gerar_calendario_intervalo(data_inicial, data_final)

