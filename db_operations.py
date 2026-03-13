# --------------------------------
# Packages
# --------------------------------
import psycopg2
import sys
import os
from dotenv import load_dotenv

load_dotenv()

# --------------------------------
# Database Connection Function
# --------------------------------
def getConnection():
    try:
        return psycopg2.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
    except psycopg2.OperationalError as e:
        print("Database connection failed:", e)
        sys.exit(1)


# --------------------------------
# Create Table
# --------------------------------
def table():

    conn = getConnection()

    if conn is None:
        return

    try:
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS tbl_employees(
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            email VARCHAR(100)
        )
        """)

        conn.commit()

        print("Employees table is ready!")

    except Exception as e:
        print("Error creating table:", e)

    finally:
        cur.close()
        conn.close()


# --------------------------------
# Insert Data
# --------------------------------
def data_insert(name, age, email):

    conn = getConnection()

    if conn is None:
        return

    try:
        cur = conn.cursor()

        query = """
        INSERT INTO tbl_employees(name, age, email)
        VALUES (%s, %s, %s)
        """

        cur.execute(query, (name, age, email))
        conn.commit()

        print("\nEmployee data inserted successfully")

    except Exception as e:
        print("Error inserting data:", e)

    finally:
        cur.close()
        conn.close()


# --------------------------------
# Fetch Data
# --------------------------------
def fetch_data():

    conn = getConnection()

    if conn is None:
        return

    try:
        cur = conn.cursor()

        query = "SELECT id, name, age, email FROM tbl_employees"
        cur.execute(query)

        rows = cur.fetchall()

        if not rows:
            print("\nNo employee records found.\n")
            return

        print("\nEmployee Records:\n")

        for emp in rows:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Email: {emp[3]}")

    except Exception as e:
        print("Error fetching data:", e)

    finally:
        cur.close()
        conn.close()


# --------------------------------
# User Input Function
# --------------------------------
def user_inputs():

    try:
        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: "))
        email = input("Enter Email Address: ").strip()

        data_insert(name, age, email)

    except ValueError:
        print("Invalid age input")


# --------------------------------
# Main Program
# --------------------------------
def main():

    print("\nPostgreSQL & Python Database Operations\n")

    # conn = getConnection()

    # if conn is None:
    #     print("Unable to connect to database. Exiting...")
    #     return
    
    # conn.close()

    table()

    while True:
        print("\nPlease enter your choice to proceed: ")
        print("\n1 Insert Employee Data")
        print("2 View Employees")
        print("3 Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_inputs()

        elif choice == "2":
            fetch_data()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()