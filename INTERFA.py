import streamlit as st
import numpy as np
import cv2
from PIL import Image

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Inventario de Bodega",
    page_icon="📦",
    layout="wide"
)

# --- TÍTULO Y DESCRIPCIÓN ---
st.title("📦 Sistema de Inventario de Bodega")
st.write(
    "Utiliza la cámara para capturar una imagen de la estantería. "
    "El sistema detectará los productos, los contará y mostrará su ubicación."
)

col1, col2 = st.columns([2, 1])

# Inicializar la variable de estado
if "show_camera" not in st.session_state:
    st.session_state.show_camera = False

with col1:
    st.header("📷 Captura de la Cámara")
    
    # Contenedor para los botones
    btn_col1, btn_col2 = st.columns(2)
    
    with btn_col1:
        if st.button("Mostrar Cámara"):
            st.session_state.show_camera = True
    
    with btn_col2:
        if st.button("Ocultar Cámara"):
            st.session_state.show_camera = False

    # El resto del código dentro de este bloque
    if st.session_state.show_camera:
        img_buffer = st.camera_input("Toma una foto", key="camera")
    else:
        st.info("Presiona 'Mostrar Cámara' para activarla.")
        img_buffer = None

with col2:
    st.header("📊 Análisis y Búsqueda")
    
    buscar_producto = st.text_input("Buscar Producto", key="search_query", placeholder="Ej: Caja, Botella...")

    st.subheader("Descripción")

    # Esta línea también debe estar sangrada
    if img_buffer is not None:
        st.success("¡Foto capturada! Puedes continuar con el análisis.")
        # Aquí iría tu lógica de procesamiento de imagen
        # ...
