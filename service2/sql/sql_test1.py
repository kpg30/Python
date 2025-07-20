from sql_conn import get_mysql_conn

# Connect to MySQL
#connection = get_mysql_conn("")
connection = get_mysql_conn("test1")

if connection:
    cursor = connection.cursor()
    print("-----------------------------------")
    print(" Employee data ")
    print("-----------------------------------")

    # Describe the table to check the structure
    #cursor.execute("DESCRIBE employee_1")
    #table_structure = cursor.fetchall()

    # for row in table_structure:
    #     print(row)
    # cursor.execute("CREATE DATABASE IF NOT EXISTS test2;")
    cursor.execute("SHOW DATABASES;")
    databases= cursor.fetchall()
    for db in databases:
        print(db)
    
    cursor.execute("SELECT * FROM employee_1")
    employee_data = cursor.fetchall()
    for row in employee_data:
        print(row)

    # Close connection
    cursor.close()
    connection.close()
