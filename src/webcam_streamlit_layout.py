import streamlit as st
import base64 # used in set_bg_hack to encode bg image
from datetime import date # used in write_image for file name
import time # used in write_image for file name
import cv2 # used in write_image for writing images

def button():
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #009ee3; color: #ffffff; text-align:center;
    }
    div.stButton > button:hover {
        background-color:#00ff00; color: #fffff; text-align:center;
    }
    </style>""",unsafe_allow_html=True)

def header(text):
    html_temp = f"""
    <h1 style = "color:#009ee3; text_align:center; font-weight: bold;"> {text} </h1>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html = True)


#def Logo_HS():
 #   main_logo = "Flower.png"
  #  main_logo_ext="png"
   # st.markdown(
    #    f"""
     #   <img>
      #  .reportview-container {{
       #      img: url(data:image/{main_logo_ext};base64,{base64.b64encode(open(main_logo, "rb").read()).decode()})
        # }}
       #  </img>
        # """,
       # unsafe_allow_html=True
    #)


