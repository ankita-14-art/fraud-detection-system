# fraud-detection-system
Project Overview

This project is a Fraud Detection and Transaction Analysis System built using Python, MySQL, and Machine Learning.
It helps in:

Analyzing financial transactions

Detecting fraudulent activities using rule-based logic and ML models

Visualizing transaction patterns for better insights



---

🛠️ Tech Stack

Python (Pandas, Matplotlib, Seaborn, Scikit-learn)

MySQL (Database to store transactions)

Jupyter Notebook / VS Code



---

⚙️ Features

✔️ Import transaction data into MySQL
✔️ Perform Exploratory Data Analysis (EDA)
✔️ Rule-based fraud detection (high transaction amount, suspicious type)
✔️ SQL queries for business insights (top spenders, transaction patterns)
✔️ Machine Learning model for fraud prediction (Logistic Regression)
✔️ Visualizations: fraud vs non-fraud, transaction distribution, heatmaps


---

📂 Project Structure

fraud-detection-system/
│-- transactions.csv          # Sample transaction dataset
│-- fraud_detection.py        # Main Python script
│-- README.md                 # Documentation


---

🚀 How to Run

1. Clone this repository

git clone https://github.com/YourUsername/fraud-detection-system.git
cd fraud-detection-system


2. Install dependencies

pip install mysql-connector-python pandas matplotlib seaborn scikit-learn


3. Create MySQL Database

CREATE DATABASE fraud_detection;
USE fraud_detection;
CREATE TABLE transactions (
    Transaction_ID INT PRIMARY KEY,
    User_ID INT,
    Amount FLOAT,
    Time VARCHAR(50),
    Transaction_Type VARCHAR(50),
    Is_Fraud INT
);


4. Import transactions.csv into MySQL


5. Run the script

python fraud_detection.py




---

📊 Sample Outputs

Fraud vs Non-Fraud transaction graph

Transaction amount distribution

SQL-based top users by spending

ML Model evaluation report



---

👩‍💻 Author

Ankita Dash
📌 Aspiring Data Analyst | Python & SQL Enthusiast
