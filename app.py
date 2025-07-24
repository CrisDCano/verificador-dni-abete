import streamlit as st
from PIL import Image
import pytesseract

st.set_page_config(page_title="Verificador de DNI - Hospital Abete")

st.title("📄 Verificador de DNI - Hospital Abete")
st.write("Subí **ambas caras del DNI (frente y dorso)** y el sistema verificará el domicilio y fechas.")

st.subheader("📸 Subí ambas caras del DNI")
dni_frente = st.file_uploader("Frente del DNI", type=["jpg", "jpeg", "png"])
dni_dorso = st.file_uploader("Dorso del DNI", type=["jpg", "jpeg", "png"])

if dni_frente and dni_dorso:
    st.success("✅ Imágenes subidas correctamente")

    image_frente = Image.open(dni_frente)
    image_dorso = Image.open(dni_dorso)

    st.image(image_frente, caption="Frente del DNI", use_column_width=True)
    st.image(image_dorso, caption="Dorso del DNI", use_column_width=True)

    st.subheader("🔍 Extracción de datos:")

    texto_frente = pytesseract.image_to_string(image_frente, lang="eng+spa")
    texto_dorso = pytesseract.image_to_string(image_dorso, lang="eng+spa")

    texto_total = texto_frente + "\n" + texto_dorso
    st.text_area("Texto detectado", value=texto_total, height=200)

    # Verificación básica
    if "MALVINAS ARGENTINAS" in texto_total.upper():
        st.success("✅ Domicilio en Malvinas Argentinas detectado")
    else:
        st.error("❌ Domicilio en Malvinas Argentinas NO detectado")

    if "VENC" in texto_total.upper() or "2030" in texto_total:
        st.info("ℹ️ Fecha de vencimiento detectada")
else:
    st.info("Cargá ambas imágenes para continuar")

st.markdown("---")
st.caption("Desarrollado por CrisDCano con amor para el Hospital Abete 🏥
