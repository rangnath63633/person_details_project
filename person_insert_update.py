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

    test = True
    while test:
        print("1 for insert to Person details")
        print("2 for update to Person details")
        print("3 for shows all Persons details")
        print("4 for delete the person information")
        print("5 for exist")
        choice = int(input("select your operation :"))

        print()

        if choice == 1:
            name = input("Enter your name:")
            age = int(input("Enter your age:"))
            location = input("Enter your location:")
            insert = f"insert into {table_name} (name,age,location) values (%s, %s, %s)"
            data_to_insert = (name,age,location)
            mycursor.execute(insert,data_to_insert)
            conn.commit()
            print("person details inserted successfully.")
            print("-----------------------------------")
            print()
        elif choice == 2:

            update_test =True
            while update_test:
                update_choice = int(
                    input("select your column number for update. 1.name, 2.age, 3.location, 4.Homepage : "))
                if update_choice == 1:
                    new_name = input("Enter here update name :")
                    row_id = int(input("Enter your id:"))
                    update = f"update {table_name} set name=%s where id=%s"
                    mycursor.execute(update,(new_name,row_id))
                    conn.commit()
                    print("person name updated successfully.")
                    print("-----------------------------------")
                    print()
                elif update_choice == 2:
                    new_age = int(input("Enter here update age :"))
                    row_id = int(input("Enter your id:"))
                    update = f"update {table_name} set age=%s where id=%s"
                    mycursor.execute(update, (new_age, row_id))
                    conn.commit()
                    print("person age updated successfully.")
                    print("-----------------------------------")
                    print()
                elif update_choice == 3:
                    new_location = input("Enter here update location :")
                    row_id = int(input("Enter your id:"))
                    update = f"update {table_name} set location=%s where id=%s"
                    mycursor.execute(update, (new_location, row_id))
                    conn.commit()
                    print("person location updated successfully.")
                    print("-----------------------------------")
                    print()
                else:
                    update_test = False

        elif choice == 3:
            mycursor.execute(f"select * from {table_name}")
            mydata = mycursor.fetchall()

            print("ID  NAME   AGE   Location")
            print("-----------------------------------")
            # for i in mycursor:
            #     print(i)
            for i in mydata:
                print(i)

            print("-----------------------------------")
            print()
        elif choice == 4:
            record_id = int(input("Enter the id for deleting person record:"))
            rec_id =(record_id,)
            delete=f"delete from {table_name} where id=%s"
            mycursor.execute(delete, rec_id)
            conn.commit()
            print("person record deleted successfully.")

        else :
            test = False


except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        mycursor.close()
        conn.close()