# MVC Streamlit Application with SQL Server

## Overview
This project demonstrates how to implement the Model-View-Controller (MVC) pattern in a Streamlit application connected to a SQL Server database.

## Project Structure
```sh
mvc-dataapp-article/
├── models/
│   ├── database.py
├── views/
│   ├── ui.py
├── controllers/
│   ├── app_controller.py
├── main.py
```

- **models/database.py**: Handles database connections and queries.
- **views/ui.py**: Manages UI components and visualizations using Streamlit and Matplotlib/Seaborn.
- **controllers/app_controller.py**: Handles business logic and connects the Model and View.
- **main.py**: Entry point for the application.

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.8+
- Streamlit
- PyODBC (for SQL Server connection)
- Pandas
- Matplotlib
- Seaborn

## Installation
Clone the repository and install dependencies:

```sh
# Clone the repository
git clone https://github.com/lorenzouriel/mvc-dataapp-article.git
cd mvc-dataapp-article

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration
Edit `.env` to include your SQL Server connection details:
```python
CONN_STR = "DRIVER={SQL Server};SERVER=your_server;DATABASE=your_db;UID=your_user;PWD=your_password"
```

## Running the Application
Execute the following command to start the Streamlit app:
```sh
streamlit run main.py
```

This will start the Streamlit server, and you can access the application in your web browser.

## Features
- Fetch contacts and goals from SQL Server.
- Display data tables in the UI.
- Visualize contacts by initial letter.
- Show goal achievement status using pie charts.
- Follow MVC principles for a structured and maintainable codebase.