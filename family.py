import pymysql
import sys
 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='familyislove',
)
def add():
    first_name = input("Enter First Name: ")
    last_name = input ("Enter Last Name: ")
    relation = input("Enter Relation: ")
    description = input("Describe him/her: ")
 
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO family (`first_name`, `last_name`, `relation`,`description`) VALUES (%s, %s, %s, %s)"
            try:
                cursor.execute(sql, (first_name, last_name, relation, description))
                print("Data added successfully")
            except:
                print("Oops! Something wrong")
                
        connection.commit()
    finally:
        print ("\n")
        return

def read():
    print ("DATA\n")
    try:
        with connection.cursor() as cursor:
            sql = "select * from family"
            cursor.execute(sql)
            connection.commit()
            results = cursor.fetchall()
            print("ID\tFirst_Name\t\tLast_Name\t\tRelation\t\tDescription")
            for row in results :
                print(str(row[0]) + "\t" + row[1] + "\t\t\t" + row[2] + "\t\t\t" , row[3] + "\t\t\t" + row[4])

        connection.commit()
    finally:
        print ("")
        return
def update():
    read()
    print("")
    id = input("Enter the id of your family to update: ")
    first_name = input("Enter new first_name: ")
    last_name = input("Enter new last_name: ")
    relation = input("Enter new relation: ")
    description = input("Enter new description: ")
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE family SET `first_name`=%s, `last_name`=%s , `relation`=%s, `description`=%s WHERE `id` = %s"
            try:
                cursor.execute(sql, (first_name, last_name, relation, description, id))
                print("Successfully Updated")
            except:
                print("Oops! Something wrong")
 
        connection.commit()
    finally:
        print ("")
        return
def delete():
    read()
    print("")
    id = input("Enter the id of your family to delete: ")
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM family WHERE id = %s"
            try:
                cursor.execute(sql, (id))
                print("Successfully Deleted")
            except:
                print("Oops! Something wrong")
 
        connection.commit()
    finally:
        print ("")
        return
def search():
    print("\n")
    first_name = input("Enter the first_name of your family you want to search: ")
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from family WHERE first_name = %s"
            try:
                cursor.execute(sql, (first_name))
                result = cursor.fetchall()
                print("ID\tFirst_Name\t\tLast_Name\t\tRelation\t\tDescription")
                for row in result:
                    print(str(row[0]) + "\t" + row[1] + "\t\t\t" + row[2] + "\t\t\t" + row[3] + "\t\t\t" + row[4])
            except:
                print("Oops! Something wrong")

        connection.commit()
    finally:
        print("")
        return
def exit():
    sys.exit(0)

choice = 1
while choice:
    print ("***Family is Love***\n\n")
    print ("[1] = Create a new data")
    print ("[2] = Read data")
    print ("[3] = Update data")
    print ("[4] = Delete data")
    print ("[5] = Search data")
    print ("[6] = Exit")

    choice = input("Choices: ")

    if choice == "1":
        add()
    elif choice == "2":
        read()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        search()
    elif choice == "6":
        exit()
        
    else:
        print ("Invalid Input!\n")
        choice = 1
