# MVC Can Help You Create Better Data Apps

## Introduction

Model-View-Controller (MVC) is a widely used software design pattern that separates concerns in application development, improving maintainability and scalability. In the field of data science and analytics, integrating MVC principles can lead to more structured and modular solutions.

This article explores how we can leverage MVC in Python using Streamlit, a powerful framework for building data-driven web applications connected to a SQL Server database.

## Understanding MVC

MVC divides an application into three interconnected components:

- **Model**: Manages data, business logic, and rules.
- **View**: Displays data and user interface elements.
- **Controller**: Handles user inputs, processes them, and updates the Model or View accordingly.

By following this structure, we create a more maintainable, scalable, and reusable codebase.

## Applying MVC in a Streamlit Application with SQL Server

### 1. Setting Up the Project Structure

A well-structured project using MVC might have the following folder structure:

```sh
src/
├── models/
│   ├── database.py
├── views/
│   ├── ui.py
├── controllers/
│   ├── app_controller.py
├── main.py
```

### 2. Implementing the Model (Database Layer)

The Model handles database operations, including retrieving and updating data.

```python
# models/database.py
import pyodbc
import pandas as pd

CONN_STR = "DRIVER={SQL Server};SERVER=your_server;DATABASE=your_db;UID=your_user;PWD=your_password"

def get_contacts():
    """Fetch all contacts from the database."""
    conn = pyodbc.connect(CONN_STR)
    query = "SELECT * FROM contacts"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def get_goals():
    """Fetch all goals from the database."""
    conn = pyodbc.connect(CONN_STR)
    query = "SELECT * FROM goals"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
```

### 3. Implementing the View (User Interface)

The View handles the presentation and user interaction.

```python
# views/ui.py
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show_contacts(df):
    """Display the contacts in the UI."""
    st.write("## Contacts")
    st.dataframe(df)
    
    # Visualization: Count of contacts per first letter of name
    if not df.empty:
        df['initial'] = df['name'].str[0]
        fig, ax = plt.subplots()
        sns.countplot(x='initial', data=df, ax=ax, order=sorted(df['initial'].unique()))
        ax.set_title("Contacts by Initial Letter")
        st.pyplot(fig)

def show_goals(df):
    """Display the goals in the UI."""
    st.write("## Goals")
    st.dataframe(df)
    
    # Visualization: Goals Achieved vs. Pending
    if not df.empty:
        achieved_counts = df['achieved'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(achieved_counts, labels=['Pending', 'Achieved'], autopct='%1.1f%%', colors=['red', 'green'])
        ax.set_title("Goals Achievement Status")
        st.pyplot(fig)
```

### 4. Implementing the Controller (Application Logic)

The Controller coordinates the interaction between the Model and the View.

```python
# controllers/app_controller.py
import models.database as model
import views.ui as view

def main():
    """Main application logic."""
    st.sidebar.title("Navigation")
    option = st.sidebar.selectbox("Choose a section", ["Contacts", "Goals"])
    
    if option == "Contacts":
        df = model.get_contacts()
        view.show_contacts(df)
    elif option == "Goals":
        df = model.get_goals()
        view.show_goals(df)
```

### 5. Running the Application

We create a `main.py` file to serve as the entry point of our application.

```python
# main.py
import streamlit as st
from controllers import app_controller

st.title("MVC in Streamlit with SQL Server")
app_controller.main()
```

Run the application using the command:

```sh
streamlit run main.py
```

---

## Benefits of MVC in Data Applications

1. **Separation of Concerns** - Improves modularity and maintainability.
2. **Reusability** - Components can be used across multiple projects.
3. **Scalability** - Easy to expand and modify each layer independently.
4. **Collaboration** - Different team members can work on different layers without conflicts.

---

## Conclusion

By leveraging MVC principles in a Streamlit application connected to a SQL Server database, we create a structured, maintainable, and scalable data application. This approach helps us build robust solutions that are easy to manage and expand over time.

Start using MVC in your data-driven projects today and experience the benefits of a well-structured application!

