import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="ranga", passwd="1234", database="ranga")

mycursor = mydb.cursor()

# mycursor.execute("show databases")
# for i in mycursor:
#     print(i)

mycursor.execute("select * from student")
# for i in mycursor:
#     print(i)

# fetch all records
# result = mycursor.fetchall()
# for i in result:
#     print(i)

# fetch one record
# result = mycursor.fetchone()
# for i in result:
#     print(i)

mycursor.execute("insert into student values('Jhon','RMIT')")

print("hello changes done")
print("check the code in git hub repository")