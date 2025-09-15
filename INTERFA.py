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


with col1:
    st.header("📷 Captura de la Cámara")
    img_buffer = st.camera_input("Toma una foto", key="camera")

    if img_buffer:
        # Convertir el buffer de imagen a un objeto de imagen PIL
        img_pil = Image.open(img_buffer)
        
        # Convertir la imagen PIL a un array de NumPy para OpenCV
        img_np = np.array(img_pil)

        # --- LÓGICA PRINCIPAL ---
        # 1. Detectar productos (usando la función simulada)
        productos_detectados = detectar_productos_simulado(img_np)
        
        # 2. Obtener el producto buscado en la otra columna
        # (Se usa session_state para acceder al valor desde aquí)
        producto_a_buscar = st.session_state.get("search_query", "")

        # 3. Dibujar las detecciones en la imagen
        imagen_resultado = dibujar_detecciones(img_np, productos_detectados, producto_a_buscar)

        # 4. Mostrar la imagen con las detecciones
        st.image(imagen_resultado, caption="Imagen Procesada", use_column_width=True)




with col2:
    st.header("📊 Análisis y Búsqueda")
    
    # Cuadro de texto para buscar producto
    buscar_producto = st.text_input("Buscar Producto", key="search_query", placeholder="Ej: Caja, Botella...")

    st.subheader("Descripción")

