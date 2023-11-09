import mysql.connector
conn = None
mycursor =None
try:
    conn = mysql.connector.connect(host="localhost",user="ranga",passwd="1234",database="ranga")

    mycursor = conn.cursor()

    table_name = "person"

    check_table = f"show tables like '{table_name}'"
    mycursor.execute(check_table)

    if mycursor.fetchone():
        print(f"Table '{table_name}' already exists.")
    else:
        create_table = f"""
        create table {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name varchar(50), age INT, location varchar(100)
        )
        """
        mycursor.execute(create_table)
        conn.commit()
        print(f"Table '{table_name}' created successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        mycursor.close()
        conn.close()