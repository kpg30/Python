from sql_conn import get_mysql_conn

# Connect to MySQL
connection = get_mysql_conn("test1")

if connection:
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS employee_2 (
        id INT AUTO_INCREMENT PRIMARY KEY,  
        first_name VARCHAR(100) NOT NULL,   
        last_name VARCHAR(100) NOT NULL,    
        email VARCHAR(100) NOT NULL,        
        position VARCHAR(50),              
        salary DECIMAL(10, 2)               
    );""")


    # Prepare the insert query
    insert_query = """
    INSERT INTO employee_2 (first_name, last_name, email, position, salary)
    VALUES (%s, %s, %s, %s, %s)
    """

    # Data to be inserted
    data = [
        ('John', 'Doe', 'john.doe@example.com', 'Manager', 55000.00),
        ('Jane', 'Smith', 'jane.smith@example.com', 'Developer', 60000.00),
        ('Alice', 'Johnson', 'alice.johnson@example.com', 'Designer', 50000.00),
        ('Bob', 'Brown', 'bob.brown@example.com', 'HR Specialist', 45000.00)
    ]

    # Insert multiple records
    cursor.executemany(insert_query, data)

    # Commit the transaction
    connection.commit()

    print(f"{cursor.rowcount} rows inserted.")

    cursor.execute("""SELECT * FROM employee_2;""")
    data= cursor.fetchall()
    for row in data:
        print(row)

    # Close the connection
    cursor.close()
    connection.close()