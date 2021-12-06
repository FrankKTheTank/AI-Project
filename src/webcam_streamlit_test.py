import streamlit as st
import cv2
from PIL import Image, ImageOps
from webcam import webcam
import webcam_streamlit_layout as layout
img2 = Image.open(('../logos/HS-OS-Logo-Standard-rgb.jpg'))

#from streamlit_webrtc import webrtc_streamer
img = Image.open('../logos/Minion_Logo.PNG')
st.set_page_config(page_title="LEGO Classification", layout='wide')


def main():
    #layout.Logo_HS()
    with st.container():
        col1, col2, col3 = st.columns([0.5,3.5,0.25])
        col1.image(img2, use_column_width=True)
        col3.image(img, use_column_width=True)
    layout.header("LEGO Classification")
    st.title("LEGO Classification")
    menu = ["Home","Image Uploader","Webcam Uploader", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Image Uploader":
        st.subheader("Image Uploader")
        file = st.file_uploader("Please upload an brain scan file", type=["jpg", "png"])
        if file is None:
            st.text("Please upload an image file")
        else:
            image = Image.open(file)
            st.image(image, use_column_width=True)
    elif choice == "Webcam Uploader":
        st.subheader("Webcam Uploader")

        #funktioniert nur für Windows https://github.com/tconkling/streamlit-webcam
        captured_image = webcam()
        if captured_image is None:
            st.write("Wait for capture...")
        else:
            st.write("Got an image from the webcam")
            st.image(captured_image)

        #funktioniert auch für Smartphone allerdings nicht so gut
        #run = st.checkbox("Run")
        #FRAME_WINDOW = st.image([])
        #camera = cv2.VideoCapture(0)


        #while run:
        #    ret, frame = camera.read()
        #    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #    FRAME_WINDOW.image(frame)



    else:
        st.subheader("About")






if __name__ == '__main__':
    main()

