import sqlite3

def create_database():

    conn = sqlite3.connect("data/expense_tracker.db")

    print("Database Created")

    conn.close()