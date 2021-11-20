import mysql.connector as sqltor
mycon = sqltor.connect(host = "localhost", user = "root", passwd = "Admin$#")
cursor = mycon.cursor()
cursor.execute("CREATE database Products")
print("List of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())
if mycon.is_connected():
    print("Connection succesfull")
else: 
    print("Connection failed")

"""
def admin():
    print("1.Add New Product\n2.Review Products\n3.Remove Product\n4.Update Product")
    input_choice = int(input("Enter your choice: "))
    if input_choice == 1:


print("Welcome")
print("1.Admin\n2.User\n3.Exit")
admin_password = "Admin123"
choice = int(input("Enter (A/U): "))
if choice == "A":
    input_password = input("Enter your password: ")
    if input_password == admin_password:
        admin()
else:
    user()
"""