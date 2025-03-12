import streamlit as st
from controllers import app_controller

st.title("MVC Data App")
app_controller.main()