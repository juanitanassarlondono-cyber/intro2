import streamlit as st
from PIL import Image

st.title("Bienvenido a primera app")

st.header("Aqui empiezas a navegar en mi app")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open("caballitos.jpg")
st.image(image, caption='Libertad')

texto = st.text_input("escribe algo","este es el texto")
st. write('el texto escrito es' , texto)
                    
