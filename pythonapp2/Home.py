import streamlit as st
import pandas as pd

#st.set_page_config(layout="wide") ->> To make the box wider containing name and details wider.

col1, col2 = st.columns(2) # st is module and columns is the method.
# This method will return two column objects.

with col1:
    st.image("pythonapp2/images/photome.png") #width=300 to adjust image width.


with col2:
    st.title("Parth Singh Chauhan")
    content = """
    Hey, I am Parth! I am a Python Programmer, a student and an enthusiast.
    """

    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("pythonapp2/data.csv", sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("pythonapp2/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("pythonapp2/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
