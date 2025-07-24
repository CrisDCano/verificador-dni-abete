
import streamlit as st
from PIL import Image
import pytesseract
import re
from datetime import datetime

st.set_page_config(page_title="Verificador de DNI - Hospital Abete", layout="centered")

st.title("📄 Verificador de DNI - Hospital Abete")
st.markdown("Subí una **foto del DNI (frente o dorso)** y el sistema verificará si cumple los requisitos.")

imagen = st.file_uploader("📷 Subí la imagen del DNI", type=["jpg", "jpeg", "png"])

if imagen:
    st.image(imagen, caption="Imagen cargada", use_column_width=True)

    texto = pytesseract.image_to_string(Image.open(imagen), lang='spa')

    st.subheader("🧠 Texto extraído")
    st.text(texto)

    nombre = re.search(r'NOMBRE:\s*(.*)', texto)
    domicilio = re.search(r'DOMICILIO:\s*(.*)', texto)
    fecha_emision = re.search(r'EMISION:\s*(\d{2}/\d{2}/\d{4})', texto)
    fecha_vencimiento = re.search(r'VENCIMIENTO:\s*(\d{2}/\d{2}/\d{4})', texto)
    dni = re.search(r'DNI:\s*(\d+)', texto)
    cuil = re.search(r'CUIL:\s*(\d{2}-\d{8}-\d)', texto)

    st.subheader("📋 Resultados de Verificación")

    if nombre:
        st.write("👤 **Nombre completo:**", nombre.group(1))
    if domicilio:
        st.write("🏠 **Domicilio:**", domicilio.group(1))
        if "MALVINAS ARGENTINAS" in domicilio.group(1).upper():
            st.success("✔️ Residencia en Malvinas Argentinas")
        else:
            st.error("❌ Residencia fuera de Malvinas Argentinas")
    if fecha_emision:
        fecha_emision_dt = datetime.strptime(fecha_emision.group(1), "%d/%m/%Y")
        antiguedad_meses = (datetime.today() - fecha_emision_dt).days // 30
        st.write("🗓️ **Fecha de emisión:**", fecha_emision.group(1))
        st.write("⏳ **Antigüedad:**", f"{antiguedad_meses} meses")
        if antiguedad_meses >= 6:
            st.success("✔️ Cumple antigüedad mínima")
        else:
            st.error("❌ No cumple antigüedad mínima")
    if fecha_vencimiento:
        fecha_vencimiento_dt = datetime.strptime(fecha_vencimiento.group(1), "%d/%m/%Y")
        if fecha_vencimiento_dt > datetime.today():
            st.success("✔️ DNI vigente")
        else:
            st.error("❌ DNI vencido")
    if dni:
        st.write("🆔 **DNI:**", dni.group(1))
    if cuil:
        st.write("🔢 **CUIL:**", cuil.group(1))
