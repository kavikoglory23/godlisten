#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.header("sample web app")
st.write("*my app*")
value=st.slider("val")
st.write(value, "squares is",value*value)

