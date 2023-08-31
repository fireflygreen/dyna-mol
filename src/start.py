import streamlit as st
import pandas as pd

st.title("command preview for ls-dyna")

st.header("upload the K-file first")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
  data = pd.read_csv(uploaded_file)
  st.write(data)
  
with st.sidebar:
  core_node = st.number_input("core/node", 8)
  node_use = st.number_input("node", 1)
  workingDir = st.text_input("working directory", "/home/comp/lsdyna")
