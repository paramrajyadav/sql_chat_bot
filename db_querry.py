import pandas as pd
import csv
def read_query_from_file():
    file_path = 'aux_data/query.txt'
    try:
        with open(file_path, 'r') as file:
            CreateTable = file.read()
            return CreateTable
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    
def file_name_from_file():
    file_path = 'aux_data/file_name.txt'
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()  # Remove leading/trailing whitespaces
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    

import sqlite3

def drop_all_tables():
    # Connect to the SQLite database
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    
    # Query to get the list of all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Drop each table
    for table_name in tables:
        table_name = table_name[0]
        drop_table_query = f"DROP TABLE IF EXISTS {table_name};"
        cursor.execute(drop_table_query)
        print(f"Dropped table {table_name}")
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    return None



    


def setup_database():

    
    import sqlite3
    create_table_querry=read_query_from_file()
    create_table_query_2 =create_table_querry

    # print(create_table_query_2)
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()

    
    # print(create_table_query_2)
    
    # Create a sample table
    cursor.execute(create_table_query_2)




    connection.commit()
    connection.close()
   

import sqlite3
import csv

def import_csv():
    try:
        connection = sqlite3.connect('db.db')
        c = connection.cursor()
        
        file = file_name_from_file()  # Assuming this function is defined elsewhere
        print("File to be imported:", file)
        
        with open(f"data/{file}.csv", 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            print("Opened CSV file")
            next(reader)  # Skip the header row if present
            
            # Dynamically determine the number of columns in the CSV
            first_row = next(reader)
            num_columns = len(first_row)
            placeholders = ','.join(['?'] * num_columns)
            
            # Re-insert the first row into the reader
            reader = csv.reader(f)
            next(reader)  # Skip the header row again
            
            for row in reader:
                print("Inserting row:", row)
                c.execute(f"INSERT INTO {file} VALUES ({placeholders})", row)
            
            connection.commit()
            print("Data imported successfully")
    except sqlite3.Error as e:
        print("SQLite error:", e)
    except Exception as e:
        print("Error:", e)
    finally:
        if connection:
            connection.close()
            print("Database connection closed")


    
        
    
if __name__ == "__main__":
    print(file_name_from_file())
    drop_all_tables()
    setup_database()
    import_csv()