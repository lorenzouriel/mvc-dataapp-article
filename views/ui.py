import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show_contacts(df):
    """display contacts in the UI"""
    st.write(" ## Contacts ")
    st.dataframe(df)

    # Visualize the data
    if not df.empty:
        df['initial'] = df['name'].str[0]
        fig, ax = plt.subplots()
        sns.countplot(x='initial', data=df, ax=ax, order=sorted(df['initial'].unique()))
        ax.set_title('Contacts')
        st.pyplot(fig)

def show_goals(df):
    """display goals in the UI"""
    st.write(" ## Goals ")
    st.dataframe(df)

    # Visualize the data
    if not df.empty:
        achieved_counts = df["achieved"].value_counts()
        labels = achieved_counts.index.map(lambda x: "Achieved" if x else "Pending")
        fig, ax = plt.subplots()
        ax.pie(achieved_counts, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.axis("equal") 
        st.pyplot(fig)