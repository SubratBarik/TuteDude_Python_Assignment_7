# PostgreSQL Database Operations using Python

This project shows how to perform basic database operations using Python and PostgreSQL. The program connects to a PostgreSQL database, creates a table, inserts employee data, and displays records from the table.

Operations implemented:
- Database connection
- Table creation
- Insert data
- Fetch data
- User input insertion

## Requirements

Python 3.x  
PostgreSQL  
psycopg2  
python-dotenv

## Install dependency

pip install psycopg2 python-dotenv

## Create a .env file in the project root and add the following variables:

DB_NAME=db_name
DB_USER=db_username
DB_PASSWORD=db_password
DB_HOST=db_host
DB_PORT=db_port

## Database Setup

Create database in PostgreSQL:

CREATE DATABASE db_employees;

## Run the program

python db_operations.py

Setup Environment Variables

