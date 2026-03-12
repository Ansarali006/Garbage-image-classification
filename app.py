import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json

model=tf.keras.models.load_model("garbage_classification_model.keras")

with open("class_names.json","r") as f:
    class_names=json.load(f)

st.title("Garbage Classification")
st.write("Upload an image for classification")

uploaded_image=st.file_uploader("choose an image",type=['jpg','jpeg','png','jfif'])
st.write("The model can classify the following classes:")

st.write(", ".join(class_names))

if uploaded_image is not None:
    image=Image.open(uploaded_image)
    st.image(image,caption="uploaded image",width=200)

if st.button("Predict"):
    image=image.resize((224,224))
    image_array=np.array(image)
    image_array=np.expand_dims(image_array,0)

    prediction = model.predict(image_array)
    predicted_class = np.argmax(prediction)
    st.success(f"predicted class:{class_names[predicted_class]}")
