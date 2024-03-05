import streamlit as st

st.set_page_config(
    page_title="Under Construction",
    page_icon="🚧",
)

# st.snow()

st.title('Displaying Three Columns')
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")