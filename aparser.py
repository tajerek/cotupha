#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from functionforDownloadButtons import download_button
###################################

def new_only(file1, file2) :
    list1 = []
    for index, row in file1.iterrows():
        code = row['Code'].strip()
        list1.append(str(code))
    for index, row in file2.iterrows():
        code = str(row['Code']).strip()
        if code in list1:
            file2 = file2.drop(index)
    return(file2) 
    
def removed(file1, file2) :
    list2 = []
    for index, row in file2.iterrows():
        code = row['Code'].strip()
        list2.append(str(code))
    for index, row in file1.iterrows():
        code = str(row['Code']).strip()
        if code in list2:
            file1 = file1.drop(index)
    return(file1)     

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

new = new_only (df1, df2)
removed = removed (df1, df2)
if st.button("Show new items"):
    st.dataframe(new)
c29, c30, c31 = st.columns([1, 1, 1])

with c30:

    Button1 = download_button(
        new,
        "New.csv",
        "Download New items",
    )

with c31:

    Button2 = download_button(
        removed,
        "removed.csv",
        "Download Removed items",
    )
st.markdown("""---""")