import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
st.title('CNN JOB MON')

image_path = "./pic/myimage.jpg"
st.image(image_path, caption='Welcome Image', use_column_width=True)
