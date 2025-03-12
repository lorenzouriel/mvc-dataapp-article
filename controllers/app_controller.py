import models.database as model
import views.ui as view
import streamlit as st

def main():
    """main application logic"""
    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Go to", ["Contacts", "Goals"])

    if option == "Contacts":
        df = model.get_contacts()
        view.show_contacts(df)
    elif option == "Goals":
        df = model.get_goals()
        view.show_goals(df)
