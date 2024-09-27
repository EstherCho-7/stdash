import streamlit as st
import requests

st.title("# STEP 3 / Upload File 🙌")
st.sidebar.markdown("# STEP 3 / Upload File 🙌")

def upload_file():
    url = 'http://43.202.66.118:8015/uploadfile/'
    file = st.file_uploader('숫자 업로드', type=['png', 'jpg', 'jpeg'])
    if file is not None: 
        files = {"file": (file.name, file.getvalue(), file.type)} 
        response = requests.post(url, files=files) 
        if response.status_code == 200:
            st.success("이미지 업로드 성공")
            st.write(response.json()) 
        else:
            st.error(f"이미지 업로드 실패: {response.status_code}")
            st.write(response.text) 
    else:
        st.warning("파일을 업로드해주세요.") 

upload_file()

