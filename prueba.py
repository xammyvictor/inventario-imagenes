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
    "El sistema detectará objetos de un color específico y los contará."
)

# --- Función para detectar objetos por color ---
def detectar_objetos_por_color(image):
    # Convertir a espacio de color HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Rango de color para el rojo (ajustar si es necesario)
    min_rojo = np.array([0, 100, 100], dtype="uint8")
    max_rojo = np.array([10, 255, 255], dtype="uint8")
    min_rojo2 = np.array([170, 100, 100], dtype="uint8")
    max_rojo2 = np.array([180, 255, 255], dtype="uint8")   
    # Crear la máscara de color
    mask = cv2.inRange(hsv, min_rojo, max_rojo)
    mask2 = cv2.inRange(hsv, min_rojo2, max_rojo2)
    mascara_final = cv2.bitwise_or(mask, mask2)
    # Encontrar contornos en la máscara
    contours, _ = cv2.findContours(mascara_final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    object_count = 0
    
    # Dibujar recuadros alrededor de los objetos detectados
    for contour in contours:
        # Filtrar por área para evitar pequeños ruidos
        if cv2.contourArea(contour) > 500: # El valor 500 es arbitrario, puedes ajustarlo
            object_count += 1
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(image, "Objeto", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
    return image, object_count

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
    
    st.subheader("Conteo de Objetos")
    
    if img_buffer is not None:
        st.success("¡Foto capturada! Analizando la imagen...")
        
        # Convertir la imagen de Streamlit a un formato que OpenCV entienda
        file_bytes = np.asarray(bytearray(img_buffer.read()), dtype=np.uint8)
        image_bgr = cv2.imdecode(file_bytes, 1)

        # Realizar la detección de objetos
        processed_image, object_count = detectar_objetos_por_color(image_bgr.copy())

        # Mostrar la imagen procesada
        st.image(processed_image, channels="BGR", caption="Objetos Detectados")

        # Mostrar el conteo
        st.write(f"Se detectaron **{object_count}** objetos rojos.")
