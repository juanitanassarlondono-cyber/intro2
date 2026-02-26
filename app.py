import streamlit as st
from PIL import Image

st.title("Bienvenido a primera app")

st.header("Aqui empiezas a navegar en mi app")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open("caballitos.jpg")
st.image(image, caption='Libertad')

texto = st.text_input("escribe algo","este es el texto")
st. write('el texto escrito es' , texto)


st.subheader("ahora son 3 columnas")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodalesmejoran la experiencia de usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
   st.write("Correcto!")

with col2:
  st.subheader("Esta es la segunda columna")
  modo == st.radio("Que modalidad es la primera en tu interfaz", ("Visual", "auditiva", "táctil"))
  if modo == "Visual":
    st.write("La vista es fundamentalpara tu interfaz")
  if modo == "auditiva":
    st.write("La audición es fundamental para tu interfaz")
  if modo == "Táctil":
   st.write("El tacto es fundamental para tu interfaz")


                    
