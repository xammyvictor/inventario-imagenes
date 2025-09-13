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

with col2:
    st.header("📊 Análisis y Búsqueda")
    
    # Cuadro de texto para buscar producto
    buscar_producto = st.text_input("Buscar Producto", key="search_query", placeholder="Ej: Caja, Botella...")

    st.subheader("Descripción")

