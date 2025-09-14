# -------------------------------
# Transaction Analysis & Fraud Detection System
# -------------------------------

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# -------------------------------
# Step 1: Connect to MySQL
# -------------------------------
conn = None  # Initialize conn to None
try:
    conn = mysql.connector.connect(
        host='localhost',         # Your MySQL host
        port=3306,
        user='root',     # Your MySQL username
        password='ankita2005p', # Your MySQL password
        database='fraud_detection'
    )
    print("Connection to MySQL successful!")

# -------------------------------
# Step 2: Load data from MySQL
# -------------------------------
    df = pd.read_sql("SELECT * FROM transactions", conn)
    print("Data Preview:")
    print(df.head())
    print("\nData Info Before Cleaning:")
    print(df.info())

# -------------------------------
# Step 3: Data Cleaning (FIX for the ValueError)
# -------------------------------
    # Remove any whitespace from column names that might cause issues
    df.columns = df.columns.str.strip()
    
    # The 'Is_Fraud' column is likely of type 'object' with string values ('0', '1').
    # We need to convert it to an integer (1=fraud, 0=non-fraud) for plotting and modeling.
    print("\nUnique values in 'Is_FRaud' before conversion:", df['Is_FRaud'].unique())
    df['Is_FRaud'] = df['Is_FRaud'].astype(int)
    
    print("\nData Info After Cleaning:")
    print(df.info())

# -------------------------------
# Step 4: Exploratory Data Analysis
# -------------------------------
    # Fraud vs Non-Fraud counts
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Is_FRaud', data=df)
    plt.title("Fraud vs Non-Fraud Transactions")
    plt.show()

    # Transaction Amount Distribution
    plt.figure(figsize=(6, 4))
    sns.histplot(df['Amount'], bins=50)
    plt.title("Transaction Amount Distribution")
    plt.show()

    # Optional: Correlation Heatmap
    plt.figure(figsize=(6, 4))
    sns.heatmap(df.corr(numeric_only=True), annot=True)
    plt.title("Correlation Heatmap")
    plt.show()

# -------------------------------
# Step 5: Rule-Based Fraud Detection
# -------------------------------
    # Simple rules: high amount or suspicious type
    fraud_txns = df[(df['Amount'] > 2000) | (df['Transaction_TYpe'] == 'suspicious')]
    print("\nPotential Fraudulent Transactions:")
    print(fraud_txns)

# -------------------------------
# Step 6: SQL Queries for Insights
# -------------------------------
    # Top users by total transaction amount
    query = """
    SELECT User_ID, COUNT(*) AS txn_count, SUM(Amount) AS total_amount
    FROM transactions
    GROUP BY User_ID
    ORDER BY total_amount DESC;
    """
    top_users = pd.read_sql(query, conn)
    print("\nTop Users by Transaction Amount:")
    print(top_users.head())

# -------------------------------
# Step 7: (Optional) ML Model for Fraud Detection
# -------------------------------
    # Using only 'Amount' as feature for simplicity
    X = df[['Amount']]
    y = df['Is_FRaud']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("\nML Model Evaluation:")
    print(classification_report(y_test, y_pred))

except mysql.connector.Error as err:
    # This block will execute if the connection fails
    print(f"\nError: {err}")
    print("Please check your MySQL credentials, server status, and permissions.")

finally:
    # This block ensures the connection is closed, whether an error occurred or not
    if conn and conn.is_connected():
        conn.close()
        print("\nMySQL connection is closed.")