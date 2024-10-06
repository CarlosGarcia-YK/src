import streamlit as st
import os
import base64

# Configuración de la página
st.set_page_config(page_title="Contactos - NASA Seismic Challenge", page_icon="📞")

# Ruta a la carpeta de imágenes
current_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(current_dir, '..', 'image')  # Cambiado '../src/image' a '../image'

# Verificar si la ruta a la carpeta de imágenes es correcta
if not os.path.isdir(image_dir):
    st.error(f"No se encontró la carpeta de imágenes: {image_dir}")

# Leer y codificar la imagen de fondo
background_image_path = os.path.join(image_dir, 'carina08_hubble_960.jpg')

try:
    with open(background_image_path, 'rb') as f:
        background_image_data = f.read()
    background_image_base64 = base64.b64encode(background_image_data).decode()
except FileNotFoundError:
    st.error(f"No se encontró la imagen de fondo: {background_image_path}")
    background_image_base64 = ''

# Estilos CSS personalizados
css = f"""
<style>
    /* Fondo de la aplicación */
    .stApp {{
        background-image: url("data:image/jpg;base64,{background_image_base64}");
        background-size: cover;
        background-position: center;
    }}
    /* Estilos para los contactos */
    .contact-item {{
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        background-color: rgba(0, 0, 0, 0.8);
        padding: 10px;
        border-radius: 10px;
    }}
    .contact-description h3 {{
        margin: 0;
        color: #00bcd4;
    }}
    .contact-description p {{
        margin: 5px 0;
    }}
    a {{
        text-decoration: none;
        color: inherit;
    }}
    /* Estilos para el pie de página */
    footer {{
        background-color: #1a1a1a;
        padding: 20px;
        text-align: center;
        margin-top: 40px;
        color: #777;
    }}
</style>
"""

# Inyección de los estilos CSS personalizados
st.markdown(css, unsafe_allow_html=True)

# Título de la página
st.title("Contactos")

# Información de los contactos
contactos = [
    {
        "nombre": "Mauricio Pacheco",
        "imagen": "El_miau.png",
        "descripcion": "Data Engineer.",
        "link": "https://www.linkedin.com/in/mauricio-pacheco-lizama-475a4a203"
    },
    {
        "nombre": "Yuridia Villanueva",
        "imagen": "la_yuri.jpg",
        "descripcion": "Robotic Engineer.",
        "link": "https://www.linkedin.com/in/yuridia-villanueva-206b27217"
    },
    {
        "nombre": "Carlos Garcia",
        "imagen": "Garcia_Carlos.png",
        "descripcion": "Robotic Engineer.",
        "link": "https://www.linkedin.com/in/carlos-jes%C3%BAs-garcia-cano-9a9ab2189"
    },
    {
        "nombre": "Krishna Sandoval",
        "imagen": "kri.png",
        "descripcion": "Data Engineer.",
        "link": "#"  # Reemplaza con el enlace real si está disponible
    },
    {
        "nombre": "Christian Montero",
        "imagen": "foto2.png",
        "descripcion": "Data Engineer",
        "link": "https://www.linkedin.com/in/christian-can-montero-567267295"
    },
]

# Mostrar los contactos
for contact in contactos:
    image_path = os.path.join(image_dir, contact['imagen'])
    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()
        image_base64 = base64.b64encode(image_data).decode()
        image_html = f'<img src="data:image/png;base64,{image_base64}" alt="{contact["nombre"]}" style="width: 100px; height: 100px; object-fit: cover; border-radius: 50%; margin-right: 20px;">'
    except FileNotFoundError:
        st.error(f"No se encontró la imagen: {image_path}")
        image_html = ''

    st.markdown(f"""
    <a href="{contact['link']}" target="_blank">
        <div class="contact-item">
            {image_html}
            <div class="contact-description">
                <h3>{contact['nombre']}</h3>
                <p>{contact['descripcion']}</p>
            </div>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Pie de página
st.markdown("""
<footer>
    <p>Simulador del Sitio Web de la NASA - Hecho con fines educativos</p>
</footer>
""", unsafe_allow_html=True)