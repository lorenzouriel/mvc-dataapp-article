# MVC Can Help You Create Better Data Apps
Learning software design patterns can help you create better solutions.

I’m a huge fan of software design patterns. I started studying them when I realized that the quality of the code elevates when you incorporate this kind of model. The code becomes more readable, simpler, and more collaborative.

However, there’s something important to note: these patterns can be applied across many areas, including data applications.

***You can work with data and like coding.***

MVC is one of those patterns, and I have many examples of how it can help you create cleaner code. However, the best example, in my opinion, is its application in data apps.

In this article, we will build a data app using the tracking_habits database that I created earlier. The primary goal is to understand how the code is structured within the MVC pattern and why this separation is beneficial.

But, what is MVC?

## MVC (Model-View-Controller)
MVC is a design pattern that separates an application into three main components, each responsible for a distinct part of the process:
- **Model**: Represents the application's data, handles database interactions and encapsulates the business logic and rules.
- **View**: Displays the data to the user and manages the user interface elements, ensuring the information is presented clearly.
- **Controller**: Acts as an intermediary between the Model and View. It processes user inputs, updates the Model accordingly, and refreshes the View to reflect changes.

In essence, the roles can be summarized as:
- **Model**: The backend data and logic.
- **View:** The frontend interface, what the user interacts with.
- **Controller**: The logic that responds to user actions and updates both the data and interface.

Simple, right?

Now, let's build our data app.

## MVC with Streamlit

First of all, we need to understand the folder structure. Each component need to be organized in his respective folder:
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

The `main.py` will be responsible for initializing our `app_controller.py`. This encapsulates the controller logic only in the `app_controller.py`, I create the `main.py` to serve as the entry point of our application.

### Models > `database.py`
The Model handles database operations, including retrieving and updating data.
```python
import pyodbc
import pandas as pd
import dotenv
import os

dotenv.load_dotenv()

CONN_STR = os.getenv('CONN_STR')

def get_contacts():
    """fetch all contacts from the database"""
    conn = pyodbc.connect(CONN_STR)
    query = "SELECT * FROM contacts"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def get_goals():
    """fetch all goals from the database"""
    conn = pyodbc.connect(CONN_STR)
    query = "SELECT * FROM goals"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
```

In this example I created only two functions to retrieve contacts and goals.

But, here you can create more specific methods and different requests for the database. 

One option too is divide even more the logic:
```sh
src/
├── models/
│   ├── contacts.py
│   ├── goals.py
```

It's recommended if your code became too big.

### Views > `ui.py`
The View handles the presentation and user interaction.
```python
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
```

The `show_contacts(df)` displays a table of contacts and a bar chart showing how many contacts start with each letter and the `show_goals(df)` displays a table of goals and a pie chart showing the percentage of "Achieved" vs "Pending" goals.

It's a simple UI just for teaching purposes.

### Controller > `app_controller.py`
The Controller coordinates the interaction between the Model and the View.
```python
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
```

This code defines the main logic of a Streamlit application, managing navigation `("Go to", ["Contacts", "Goals"])`. It coordinates interactions between the Model (data retrieval) and the View (UI display), ensuring the correct content is shown based on user selection.

Since it stays in the middle of the process, it doesn’t directly fetch data (Model) or display it (View), but instead:
1. Gets data from the `models.database` (Model).
2. Passes it to `views.ui` (View) for display.
3. Handles user navigation between "Contacts" and "Goals."

After understanding all this, you can simply run: `streamlit run main.py`

## Benefits
**Scalability** is the major benefit I can see here, when you adopt MVC is easy to expand and modify each layer independently. Instead of trying to debud a code with 2000 lines, you can quickly follow errors in the specific component responsible.

Another key advantage is **collaboration**. The backend and frontend teams can work separately, each focusing on their respective layers without interfering with one another.

This separation also leads to **reusability**, each component can be reused across multiple projects, you can reuse your code.

## More Examples of MVC in Data Role
I know, not everyone create codes like this. Sometimes, we work on Reports, APIs, and ETLs instead of traditional applications.

But guess what?

The MVC concept can be applied to them!

### 1. Reporting 
- **Model**: Fetching and structuring data from a database or API.
- **View**: Displaying reports in graphs, tables and dashboards.
- **Controller**: Handling user interactions such as filtering, exporting and scheduling reports.

### 2. ETL (Extract, Transform, Load)
- **Model**: Handles data extraction, transformation logic and storage.
- **View**: Provides status updates, logs and data previews.
- **Controller**: Manages the workflow execution, error handling and user inputs

### 3. APIs
- **Model**: Defines database schema and business rules.
- **View**: Acts as API responses, formatting JSON or XML output.
- **Controller**: Manages API requests, authentication, and response handling.

It's that famous phrase: the concept exists and you've already applied it, you just didn't know it yet.

## Flow explanation:
1. User interaction with the Streamlit interface.
2. The View (`views/ui.py`) displays data and graphics.
3. The Controller (`controllers/app_controller.py`) manages the logic, capturing user actions and requesting data from the Model.
4. The Model (`models/database.py`) retrieves information from SQL Server.
5. Data is sent back to the Controller, which is passed to the View, updating the user interface.

### Architecture
![architecture](/src/docs/architecture.png)