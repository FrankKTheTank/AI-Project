import tensorflow as tf
import streamlit as st


def load_model():
  model=tf.keras.models.load_model('../MyModel/testModel')
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()

st.write("""
         # Legobrick Classification
         """
         )

file = st.file_uploader("Please upload an brain scan file", type=["jpg", "png"])

import cv2
from PIL import Image, ImageOps
import numpy as np
st.set_option('deprecation.showfileUploaderEncoding', False)

def import_and_predict(image_data, model):
    
        size = (200,200)
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img[np.newaxis,...]
    
        prediction = model.predict(img_reshape)
        
        return prediction

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    #img = image.load_img(image, target_size=(200,200,3))
    predictions = import_and_predict(image, model)
    score = tf.nn.softmax(predictions[0])
    score = score *100
    st.write(score)
    st.write(predictions)
    #st.write(score)
    #X = st.image.img_to_array(img)
    #X = np.expand_dims(X,axis=0)
    #images = np.vstack([X])

    #val = model.predict(image)

    if predictions == 0:
         st.write(
            "This image most likely belongs to Oben with a {:.2f} percent confidence."
                .format(np.max(score)))
    else:
         st.write(
    "This image most likely belongs to Unten with a {:.2f} percent confidence."
    .format(np.max(score)))


