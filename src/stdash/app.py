import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
st.title('CNN JOB MON')

image_path = "./pic/myimage.jpg"
st.image(image_path, caption='Welcome Image', use_column_width=True)


st.header("프로젝트 소개")
st.write("이 프로젝트는 4가지 기능이 있습니다.")
st.write("1. mnist Database에 저장되어 있는, 손글씨로 적힌 숫자 파일의 요청 시간과 예측된 시각을 도식화하여 나타냅니다.")
st.write("2. mnist Database에 저장되어 있는, 손글씨로 적힌 숫자 파일의 요청자와 처리자의 숫자를 나타냅니다. 이로써 요청자와 처리자의 균형을 확인할 수 있습니다.")
st.write("3. 파일을 올릴 수 있습니다.")
st.write("4. 업로드한 파일이 핫도그인지 아닌지 알 수 있습니다.")

st.header("피드백 남기기")
feedback = st.text_area("피드백을 남겨주세요:")
if st.button("전송"):
    st.success("피드백이 전송되었습니다!")
else:
    st.error("당신의 피드백은 받지 않습니다.")
