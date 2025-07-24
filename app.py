import streamlit as st
from PIL import Image

st.set_page_config(page_title="Verificador de DNI - Hospital Abete", layout="centered")

st.title("📄 Verificador de DNI - Hospital Abete")
st.write("Subí **fotos del DNI (frente y dorso)** y el sistema verificará si cumple los requisitos.")

# Subida de imágenes
st.subheader("📤 Subí las imágenes del DNI")

dni_frente = st.file_uploader("Frente del DNI", type=["jpg", "jpeg", "png"], key="frente")
dni_dorso = st.file_uploader("Dorso del DNI", type=["jpg", "jpeg", "png"], key="dorso")

if dni_frente and dni_dorso:
    st.success("✅ Imágenes subidas correctamente")
    st.image(Image.open(dni_frente), caption="Frente del DNI", use_column_width=True)
    st.image(Image.open(dni_dorso), caption="Dorso del DNI", use_column_width=True)
else:
    st.info("Cargá ambas imágenes para continuar.")

st.markdown("---")
st.caption("Desarrollado por CrisDCano 💚 Hospital Abete")
