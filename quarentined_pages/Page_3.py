import streamlit as st

st.set_page_config(
    page_title="Page 3",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://tcg3pl.sharepoint.com/',
        'Report a bug': "mailto:tds@tcg3pl.com",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('Using set_page_config()')