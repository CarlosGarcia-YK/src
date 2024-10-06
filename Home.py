import streamlit as st

# Configuración de la página
st.set_page_config(page_title="NASA Seismic Challenge", page_icon="🌍")

# Título de la aplicación
st.title("NASA Seismic Challenge")

st.markdown("""
Welcome to the NASA SEISMIC CHALLENGE APP.
""")

# Canva embed (HTML iframe)
st.markdown("""
<div style="position: relative; width: 100%; height: 0; padding-top: 56.2500%; padding-bottom: 0;
 box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
    <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https://www.canva.com/design/DAGSvgnC_Os/KMZ3Gp5q5Ctb_w5SjYdgUw/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
    </iframe>
</div>
<a href="https://www.canva.com/design/DAGSvgnC_Os/KMZ3Gp5q5Ctb_w5SjYdgUw/view?utm_content=DAGSvgnC_Os&utm_campaign=designshare&utm_medium=embeds&utm_source=link" target="_blank" rel="noopener"></a
""", unsafe_allow_html=True)

# Footer
st.markdown("""
---
Hecho con 💻 para el NASA Hackathon 2024
""")
