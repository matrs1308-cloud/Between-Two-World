import streamlit as st
import pandas as pd
from pathlib import Path
st.set_page_config(
   page_title="Between Two Worlds",
   page_icon="🌌",
   layout="wide"
)
# DISEÑO

st.markdown("""
<style>
.stApp {
   background-color: #0B132B;
   color: white;
}
.card {
   background-color: #1C2541;
   border: 1px solid #3A506B;
   border-radius: 12px;
   padding: 20px;
   margin-bottom: 15px;
}
h1, h2, h3 {
   color: white !important;
}
</style>
""", unsafe_allow_html=True)
# PORTADA
st.markdown("### AN EXPEDITION BY MATÍAS & ZAZA")
st.title("BETWEEN TWO WORLDS")
st.write("Two worlds. One universe of discoveries.")
st.divider()
# OCÉANO
st.header("01 / BELOW THE SURFACE - THE OCEAN")
col1, col2, col3 = st.columns(3)
with col1:
   st.markdown("""
<div class="card">
<h3>Layers of the deep</h3>
<p>Sunlight fades; pressure rises.</p>
</div>
   """, unsafe_allow_html=True)
with col2:
   st.markdown("""
<div class="card">
<h3>Life finds a way</h3>
<p>Strange adaptations for extreme habitats.</p>
</div>
   """, unsafe_allow_html=True)
with col3:
   st.markdown("""
<div class="card">
<h3>A moving ocean</h3>
<p>Tides and currents reshape coastlines.</p>
</div>
   """, unsafe_allow_html=True)
st.divider()
# BASE DE DATOS EXCEL
st.header("02 / DATABASE EXPLORER")
carpeta = Path(__file__).parent
archivos = list(carpeta.glob("*.xlsx"))
if archivos:
   archivo = st.selectbox(
       "Select your database",
       archivos,
       format_func=lambda x: x.name
   )
   try:
       excel = pd.ExcelFile(archivo)
       hoja = st.selectbox(
           "Select worksheet",
           excel.sheet_names
       )
       datos = pd.read_excel(archivo, sheet_name=hoja)
       st.success("Database connected successfully!")
       st.metric("Total records", len(datos))
       st.subheader("Database information")
       st.dataframe(datos, use_container_width=True)
       st.subheader("Search database")
       columna = st.selectbox(
           "Choose a column",
           datos.columns.tolist()
       )
       busqueda = st.text_input("Search")
       if busqueda:
           resultado = datos[
               datos[columna].astype(str).str.contains(
                   busqueda,
                   case=False,
                   na=False
               )
           ]
           st.dataframe(resultado, use_container_width=True)
           st.write("Results:", len(resultado))
   except Exception as error:
       st.error(f"Excel error: {error}")
    