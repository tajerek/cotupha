#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd

###################################
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode

###################################

from functionforDownloadButtons import download_button

###################################


def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

st.set_page_config(page_icon="✂️", page_title="Ameni BM")

#st.image("https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/balloon_1f388.png", width=100)
st.image("download.png",    width=100)

st.title("Analyse Mensuelle par Ameni Ben Mansour.")

st.subheader('Upload your files for the two consecutive months :')

txt_file1 = st.file_uploader("", type=["   ", "txt","docx","doc","rtf"], key="1")
#if  st.button("Process"):
if txt_file1 is not None:
    df1 = pd.read_csv(txt_file1, sep="\t")
    st.success("Upload Successful !")
    st.write("Number of records: "+str(len(df1)))
    file_container = st.expander("View Uploaded File")
    file_container.write(df1)
else:
    st.info(f""" 👆 Upload the file for the FIRST month.""")   
    st.stop()
    
    
st.markdown("""---""")
    
txt_file2 = st.file_uploader("", type=["   ", "txt","docx","doc","rtf"], key="2")
#if  st.button("Process"):
if txt_file2 is not None:
    df2 = pd.read_csv(txt_file2, sep="\t")
    st.success("Upload Successful !")
    st.write("Number of records: "+str(len(df2)))
    file_container = st.expander("View Uploaded File")
    file_container.write(df2)
else:
    st.info(f""" 👆 Upload the file for the SECOND month.""") 
    st.stop()    

st.markdown("""---""")    
st.subheader("New items only will appear below 👇 ")
st.text("")

c29, c30, c31 = st.columns([1, 1, 1])

with c29:

    Button1 = download_button(
        df1,
        "New.csv",
        "Download New items",
    )

with c30:

    Button2 = download_button(
        df2,
        "removed.csv",
        "Download Removed items",
    )
st.markdown("""---""")