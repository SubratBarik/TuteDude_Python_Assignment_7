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
        conn = psycopg2.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return conn
    
    # except Exception as e:
    #     print("Database connection error:", e)
    #     sys.exit(1)
    except psycopg2.OperationalError:
        print("Database authentication failed. Check credentials properly.")
        sys.exit(1)


# --------------------------------
# Create Table
# --------------------------------
def table():

    conn = getConnection()

    if not conn:
        return

    try:
        cur = conn.cursor()

        # Check if table exists
        cur.execute(
            "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name=%s)",
            ('tbl_employees',)
        )

        exists = cur.fetchone()[0]

        if exists:
            print("Table 'tbl_employees' already exists.")
        else:
            cur.execute("""
                CREATE TABLE tbl_employees(
                    emp_id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    department VARCHAR(100),
                    salary INT
                )
            """)
            conn.commit()

            print("Employees table created successfully.")

    except Exception as e:
        print("Error:", e)

    finally:
        cur.close()
        conn.close()


# --------------------------------
# Insert Data
# --------------------------------
def data_insert(name, department, salary):

    conn = getConnection()

    if conn is None:
        return

    try:
        cur = conn.cursor()

        query = """
        INSERT INTO tbl_employees(name, department, salary)
        VALUES (%s, %s, %s)
        """

        cur.execute(query, (name, department, salary))
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

        query = "SELECT * FROM tbl_employees"
        cur.execute(query)

        rows = cur.fetchall()

        print("\nEmployee Records:\n")

        for row in rows:
            print(row)

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
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = int(input("Enter Salary: "))

        data_insert(name, department, salary)

    except ValueError:
        print("Invalid salary input")



# --------------------------------
# Main Program
# --------------------------------
def main():

    print("\nPostgreSQL & Python Database Operations\n")

    conn = getConnection()

    if conn is None:
        print("Unable to connect to database. Exiting...")
        return
    
    conn.close()

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
