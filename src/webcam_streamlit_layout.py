import streamlit as st
import base64

def Logos():

    Logo_HS = open("../logos/HS-OS-Logo-Standard-rgb.jpg", "rb")
    content_read_Logo_HS = Logo_HS.read()
    data_url_Logo_HS = base64.b64encode(content_read_Logo_HS).decode("utf-8")
    Logo_HS.close()

    Logo_Minion = open("../logos/Minion_Logo.PNG", "rb")
    content_read_Logo_Minion = Logo_Minion.read()
    data_url_Logo_Minion = base64.b64encode(content_read_Logo_Minion).decode("utf-8")
    Logo_Minion.close()

    st.markdown(
        f""" 
        <div>
        <img src="data:image/gif;base64,{data_url_Logo_HS}" width="200" style="margin:5px" align="left">
        <img src="data:image/gif;base64,{data_url_Logo_Minion}" width="100" style="margin:5px" align="right">
        </div>""",unsafe_allow_html=True)

def button():
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #009ee3; color: #ffffff; text-align:center;font-family: Arial;
    }
    div.stButton > button:hover {
        background-color:#00ff00; color: #fffff; text-align:center; font-family: Arial;
    }
    </style>""",unsafe_allow_html=True)



def header(text):
    html_temp = f"""
    <h1 style = "color:#009ee3; text_align:center; font-weight: bold; font-family: Arial; "> {text} </h1>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html = True)

def button2():
    m = st.markdown("""
    <style>
        .button {
        color: #009ee3; font-family: Arial;
        }
    </style>""",unsafe_allow_html=True)

def Loading_Spinner_GIF():
    GIF_file = open("../logos/Minion_Loading.gif", "rb")
    content_read = GIF_file.read()
    data_url = base64.b64encode(content_read).decode("utf-8")
    GIF_file.close()

    st.markdown(
        f""" 
        <div style="width:200px; height:200px; margin:0px auto;">
        <img src="data:image/gif;base64,{data_url}" widht="200" height="200" alt="Minion Loading">
        </div>""",unsafe_allow_html=True
    )

def sub_text(text):

    html_temp = f"""
    <p style = "color:#585657; text_align:justify; font-family: Arial; font-size:23px"> {text} </p>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html = True)