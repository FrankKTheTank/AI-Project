import streamlit as st
import webcam_streamlit_layout as layout
from webcam import webcam  #https://github.com/tconkling/streamlit-webcam
from PIL import Image

# es gibt eine neue Version von streamlit --> auf dem Server aktualisieren

def main_structure():
    img = Image.open('Minion_Logo.PNG')
    img2 = Image.open('HS-OS-Logo-Standard-rgb.jpg')
    with st.container():
        col1, col2, col3 = st.columns([1,2.5,0.5])
        col1.image(img2, use_column_width=True)
        col3.image(img, use_column_width=True)


    st.title("HEllo World")
    layout.header("LEGO Classification")
    menu = ["Home","Image Uploader","Webcam Uploader", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Image Uploader":
        Image_Uploader()

    elif choice == "Webcam Uploader":
        Webcam()

    elif choice == "About":
        About()

    elif choice == "Home":
        Home()


def Image_Uploader():
    st.subheader("Image Uploader")
    file = st.file_uploader("Please upload an brain scan file", type=["jpg", "png"])
    if file is not None:

        with st.container():
            col1, col2, col3 = st.columns([0.5,3,0.5])
            col2.write("Preview of your choosen image")
            image = Image.open(file)
            col2.image(image,width=400, use_column_width=True)

        with st.container():
            col1, col2, col3 = st.columns([3,0.5,3])
            layout.button()
            if col2.button("identify"):
                layout.Loading_Spinner_GIF()



def Webcam():
    st.write("""
        - Accesses the user's webcam and displays the video feed in the browser.
        - Click the "Capture Frame" button to grab the current video frame and
        return it to Streamlit.
        """)
    captured_image = webcam()
    if captured_image is None:
        st.write("Waiting for capture...")
    else:
        st.write("Got an image from the webcam:")
        st.image(captured_image)

        with st.container():
            col1, col2, col3 = st.columns([3,0.5,3])
            layout.button()
            if col2.button("identify"):
                col2.write("Got it")

def About():
    pass #special thanks to Prof and Saschas

def Home():

    text = """
    <center> <b> Welcome to the LEGO Classification App. </br> </center>
    
    """
    layout.sub_text(text)

    st.write("""
        This app allows you to take/upload photos and classify the LEGO bricks as defect od intact.
        The model was trained with the following error classes:
        - painted
        - deformed
        - smacked
        - scratched
        """)


def Spinner():

    st.image("Minion_Loading.gif")




if __name__ == '__main__':
    main_structure()