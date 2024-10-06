import streamlit as st
import tensorflow as tf
import pandas as pd
import numpy as np
import os
import base64

# Set page config
st.set_page_config(page_title="Home - NASA Seismic Challenge", page_icon="🌍")

# Ruta a la carpeta de imágenes
current_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(current_dir, '..', 'image')
background_image_path = os.path.join(image_dir, 'carina08_hubble_960.jpg')

try:
    with open(background_image_path, 'rb') as f:
        background_image_data = f.read()
    background_image_base64 = base64.b64encode(background_image_data).decode()
except FileNotFoundError:
    st.error(f"Background image not found: {background_image_path}")
    background_image_base64 = ''

# CSS for background and styled container
css = f"""
<style>
    /* Application background */
    .stApp {{
        background-image: url("data:image/jpg;base64,{background_image_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    /* Styled rectangular container */
    .container {{
        background-color: rgba(0, 0, 50, 0.85); /* Semi-transparent background */
        padding: 60px 40px;
        border-radius: 15px;
        max-width: 800px;
        margin: 60px auto;
        color: #ffffff;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4); /* Add shadow to make it stand out */
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}
    .container h1 {{
        color: #00bcd4;
        font-size: 2.5rem;
        margin-bottom: 20px;
    }}
    .container p {{
        font-size: 1.2rem;
        margin-bottom: 20px;
        color: #ffffff;
    }}
    .container label {{
        font-size: 1rem;
        color: #00bcd4;
    }}
    .container .stButton button {{
        background-color: #00bcd4;
        color: #ffffff;
        border-radius: 10px;
        font-size: 1rem;
        padding: 10px 20px;
    }}
    .container .stButton button:hover {{
        background-color: #008c9e;
        transform: translateY(-2px);
    }}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(css, unsafe_allow_html=True)

# Model loading and logic functions
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('mi_modelo.h5')
    return model

def process_file(uploaded_file):
    if uploaded_file is not None:
        try:
            # Read the CSV
            df = pd.read_csv(uploaded_file)
            
            # Check the required columns
            required_columns = ['mean', 'std', 'max', 'min', 'energy', 'dominant_freq', 'amplitude', 'rms_amplitude', 'label']
            if all(col in df.columns for col in required_columns):
                st.success("File successfully uploaded with the required columns.")
                
                # Prepare the data
                X = df[required_columns[:-1]].values
                X = X.reshape((X.shape[0], X.shape[1], 1, 1))
    
                # Load the model and predict
                model = load_model()
                predictions = model.predict(X)
    
                # Show the first predictions
                st.write("Predictions (first 10):")
                st.write(predictions[:10])

                # Show output image after processing
                output_image_path = os.path.join(image_dir, 'output.png')
                if os.path.exists(output_image_path):
                    st.image(output_image_path, caption="Output Image", use_column_width=True)
                else:
                    st.error(f"Output image not found: {output_image_path}")

            else:
                st.error(f'The CSV file must contain the following columns: {", ".join(required_columns)}.')
        except Exception as e:
            st.error(f"Error processing the file: {e}")

st.markdown(f"""
    <div class="container">
        <h1>Upload your CSV file with seismic data</h1>
        <p>Please upload a CSV file that contains the following columns: mean, std, max, min, energy, dominant_freq, amplitude, rms_amplitude, label.</p>
  
    </div>
""", unsafe_allow_html=True)

# File uploader input
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Process file when uploaded
if uploaded_file is not None:
    process_file(uploaded_file)

st.markdown('</div>', unsafe_allow_html=True)
