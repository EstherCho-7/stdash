import streamlit as st
from transformers import pipeline
import io
import random
from PIL import Image

def get_max_label(p):
  max_score = 0
  max_label = ""
  for item in p:
      if item['score'] > max_score:
          max_score = item['score']
          max_label = item['label']
  return max_label

@st.cache_resource
def load_model():
    return pipeline("image-classification", model="julien-c/hotdog-not-hotdog")

model = load_model()

st.title("# STEP 3 / Hotdog or Not Hotdog 🤔")
st.sidebar.markdown("# STEP 3 / Hotdog or Not Hotdog 🤔")

def hotdog_or_not():
    hotdog = "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQweb_7o7OrtlTP75oX2Q_keaoVYgAhMsYVp1sCafoNEdtSSaHps3n7NtNZwT_ufZGPyH7_9MFcao_r8QWr3Fdz17RitvZXLTU4dNsxr73m6V1scsH3_ZZHRw&usqp=CAE"
    dog = "https://hearingsense.com.au/wp-content/uploads/2022/01/8-Fun-Facts-About-Your-Dog-s-Ears-1024x512.webp"
    image_url = random.choice([hotdog, dog]) 
    st.image(image_url, caption="Image")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    st.write("Classifying the image...")
    prediction = model(img)

    label = get_max_label(prediction) 

    score = prediction[0]['score']

    st.write(f"Prediction: {label}")
    st.write(f"Confidence Score: {score:.2f}")

    if score > 0.8:
        st.success("핫도그입니다!")
    else:
        st.warning("핫도그가 아닙니다!")

hotdog_or_not()
