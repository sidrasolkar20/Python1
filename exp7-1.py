# exp7-1
# WAP to demonstrate CRUD (create,read,update,delete) operation on database using sqlite3
# Name:Sidra Solkar
# UIN: 231P087
# Roll No.: 43
import sqlite3

n = 0
while n != 7:
    print(" 1. Create\n 2. Insert\n 3. Select\n 4. Update\n 5. Delete\n 6. Drop table\n 7. Exit")
    n = int(input("Enter your operation: "))

    if n == 1:
        # create table in database
        try:
            conn = sqlite3.connect("Test.db")
            print("Opened database successfully")
            conn.execute("""
                CREATE TABLE IF NOT EXISTS Factory (
                    ID int primary key not null,
                    NAME text not null,
                    AGE int not null,
                    ADDRESS char(50),
                    SALARY real
                );
            """)
            print("Table created successfully")
            conn.close()
        except sqlite3.Error as e:
            print("Error creating table:", e)

    elif n == 2:
        # insert into database
        try:
            conn = sqlite3.connect("Test.db")
            print("Opened database successfully")
            conn.execute("INSERT INTO Factory (ID, NAME, AGE, ADDRESS, SALARY) VALUES (1, 'Virat Kohli', 28, 'RCB', 2000000.0)")
            conn.execute("INSERT INTO Factory (ID, NAME, AGE, ADDRESS, SALARY) VALUES (2, 'Rohit Sharma', 30, 'MI', 4000000.0)")
            conn.execute("INSERT INTO Factory (ID, NAME, AGE, ADDRESS, SALARY) VALUES (3, 'Mohd Shami', 32, 'KXIP', 6000000.0)")
            conn.execute("INSERT INTO Factory (ID, NAME, AGE, ADDRESS, SALARY) VALUES (4, 'Bhuvneshwar', 27, 'SH', 6000000.0)")
            conn.commit()
            print("Insert operation done successfully")
            conn.close()
        except sqlite3.Error as e:
            print("Error inserting data:", e)

    elif n == 3:
        # select from database
        try:
            conn = sqlite3.connect("Test.db")
            print("Opened database successfully")
            cursor = conn.execute("SELECT ID, NAME, AGE, ADDRESS, SALARY FROM Factory")
            for row in cursor:
                print(f"ID = {row[0]}\nNAME = {row[1]}\nAGE = {row[2]}\nADDRESS = {row[3]}\nSALARY = {row[4]}\n")
            print("Select done successfully")
            conn.close()
        except sqlite3.Error as e:
            print("Error selecting data:", e)

    elif n == 4:
        # update database
        try:
            conn = sqlite3.connect("Test.db")
            print("Opened database successfully")
            conn.execute("UPDATE Factory SET SALARY = 250000.0 WHERE ID = 1")
            conn.commit()
            print("Total number of rows updated:", conn.total_changes)
            cursor = conn.execute("SELECT ID, NAME, AGE, ADDRESS, SALARY FROM Factory")
            for row in cursor:
                print(f"ID = {row[0]}\nNAME = {row[1]}\nAGE = {row[2]}\nADDRESS = {row[3]}\nSALARY = {row[4]}\n")
            print("Update done successfully")
            conn.close()
        except sqlite3.Error as e:
            print("Error updating data:", e)

    elif n == 5:
        # delete database
        try:
            conn = sqlite3.connect("Test.db")
            print("Opened database successfully")
            conn.execute("DELETE FROM Factory WHERE ID = 2")
            conn.commit()
            cursor = conn.execute("SELECT ID, NAME, AGE, ADDRESS, SALARY FROM Factory")
            for row in cursor:
                print(f"ID = {row[0]}\nNAME = {row[1]}\nAGE = {row[2]}\nADDRESS = {row[3]}\nSALARY = {row[4]}\n")
            print("Delete done successfully")
            conn.close()
        except sqlite3.Error as e:
            print("Error deleting data:", e)

    elif n == 6:
        # drop table
        try:
            conn = sqlite3.connect("Test.db")
            print("Opened database successfully")
            conn.execute("DROP TABLE IF EXISTS Factory")
            print("Deleted successfully")
            conn.close()
        except sqlite3.Error as e:
            print("Error dropping table:", e)

    elif n == 7:
        print("Exiting program.")
        print("Name: Sidra Solkar \nUIN: 231P087 \nRoll No: 43")


