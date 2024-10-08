''' PYTHON MYSQL PROJECT  BY  HARSH SETHI'''

import mysql.connector
db = mysql.connector.connect(host='localhost',user='root',password='harsh',database='MyDB')
if db:
    print('Connectivity with MySQL successful!')
else:
    print('Connection with MySQL not established!')

def show_database():   # function to show databases present in mysql
    import mysql.connector
    try:         # try block runs the code and tests it for errors
        cnx = mysql.connector.connect(host='localhost', user='root', password='harsh')
        cursor = cnx.cursor()
        cursor.execute('show databases')
        print('Displaying databases in MySQL...')
        for x in cursor:
            print(x)
    except:         # except block handles the errors in try block
        print('Error in connection!')
        
def show_tables():     # function to show tables present in the database'MyDB'
    import mysql.connector
    try:
        cnx = mysql.connector.connect(host='localhost', user='root', password='harsh', database='MyDB')
        cursor = cnx.cursor()
        cursor.execute('show tables')
        print('Displaying tables in MyDB database...')
        for x in cursor:
            print(x)
    except:
        print('Error in connection!')

def create_table():    # function to create a table in the database'MyDB'
    import mysql.connector
    cnx = mysql.connector.connect(host='localhost', user='root', password='harsh', database='MyDB')
    cursor = cnx.cursor()
    cursor.execute("create table FindCar (company varchar(20), model varchar(20) primary key, FuelType varchar(10), price int, power int, torque int)")
    print('FindCar table created...')

def disp_struct():     # function to display the structure of the table'FindCar'
    import mysql.connector
    try:
        cnx = mysql.connector.connect(host='localhost', user='root', password='harsh', database='MyDB')
        cursor = cnx.cursor()
        cursor.execute('desc FindCar')
        print('Displaying structure of table FindCar')
        for x in cursor:
            print(x)
    except:
        print('Error in connection!')

def add_data():     # function to insert values in the table'FindCar'
    import mysql.connector
    try:
        cnx = mysql.connector.connect(host='localhost', user='root', password='harsh', database='MyDB')
        cursor = cnx.cursor()
        company = input('Enter company:')
        model = input('Enter model:')
        fuel = input('Enter fuel type:')
        price = input('Enter price:')
        power = int(input('Enter power:'))
        torque = int(input('Enter torque:'))
        cursor.execute('insert into FindCar values(%s,%s,%s,%s,%s,%s)',(company,model,fuel,price,power,torque))   #each %s corresponds to a variable
        cnx.commit()  # commit makes the insert permanent in the table'FindCar'
        print('Record added...')
    except:
        cnx.rollback()  # to undo the result, we use rollback
        print('Record not added...')

def disp_alldata():     # function to display all the data of table'FindCar'
    import mysql.connector
    try:
        cnx = mysql.connector.connect(host='localhost', user='root', password='harsh', database='MyDB')
        cursor = cnx.cursor()
        cursor.execute('Select * from FindCar')
        results = cursor.fetchall()     # fetchall is used to fetch all records from the results set
        print('Company'.ljust(15),'Model'.ljust(15),'FuelType'.ljust(10),'Price'.ljust(15),'Power'.ljust(5),'Torque'.ljust(5))
        for x in results:
            print(str(x[0]).ljust(15),str(x[1]).ljust(15),str(x[2]).ljust(10),str(x[3]).ljust(15),str(x[4]).ljust(5),str(x[5]).ljust(5))
    except:
        print('Error,Unable to fetch data...')

def update_data():    # function to update table'FindCar' and increase the price by 50000
    import mysql.connector
    try:
        cnx = mysql.connector.connect(host='localhost', user='root', password='harsh', database='MyDB')
        cursor = cnx.cursor()
        cursor.execute("Update FindCar set Price=Price+50000")
        print(cursor.rowcount,'record updated...')
        cnx.commit()
    except:
        cnx.rollback()
        print('record not updated...')

def delete_data():     # function to delete data from table'FindCar'by giving the model of the car
    import mysql.connector
    try:
        cnx = mysql.connector.connect(host='localhost', user='root', password='harsh', database='MyDB')
        cursor = cnx.cursor()
        model = input('Enter model:')
        sql = 'Delete from FindCar where model = %s'
        val = (model,)
        cursor.execute(sql,val)
        print(cursor.rowcount, "record(s) deleted")
        cnx.commit()
    except:
        cnx.rollback()
        print("Record(s) not deleted...")

def disp_desc_power():    # function to display table'FindCar' in decreasing order of power
    import mysql.connector
    try:
        cnx = mysql.connector.connect(host='localhost', user='root', password='harsh', database='MyDB')
        cursor = cnx.cursor()
        cursor.execute('Select * from FindCar order by power desc')
        results = cursor.fetchall()
        print('*****Displaying Car Details*****')
        for x in results:
            print('Company:',x[0])
            print('Model:',x[1])
            print('FuelType:',x[2])
            print('Price:',x[3])
            print('Power(Hp):',x[4])
            print('Torque(Nm):',x[5])
            print('===================================')
    except:
        print('Error, unable to execute query ...')

def search_like():    # function to search cars of a particular fuel type from table'FindCar'
    import mysql.connector
    try:
        cnx = mysql.connector.connect(host='localhost', user='root', password='harsh', database='MyDB')
        cursor = cnx.cursor()
        fuel = input('Enter fuel type(petrol/diesel):')
        cursor.execute('Select * from FindCar where FuelType like %s ',(fuel,))
        results = cursor.fetchall()
        print('*****Displaying Car Details from FuelType',fuel,'*****')
        for x in results:
            print('Company:',x[0])
            print('Model:',x[1])
            print('FuelType:',x[2])
            print('Price:',x[3])
            print('Power(Hp):',x[4])
            print('Torque(Nm):',x[5])
            print('===================================')
    except:
        print('Error, unable to execute query ...')

def search_between():    # function to search cars within the given price range from table'FindCar'
    import mysql.connector
    try:
        cnx = mysql.connector.connect(host='localhost', user='root', password='harsh', database='MyDB')
        cursor = cnx.cursor()
        low = int(input('Enter minimum price:'))
        high = int(input('Enter maximum price:'))
        cursor.execute("Select * from FindCar where price between %s AND %s",(low,high))
        results = cursor.fetchall()
        print('*****Displaying Car Details with price in the range',low,'and',high,'*****')
        for x in results:
            print('Company:',x[0])
            print('Model:',x[1])
            print('FuelType:',x[2])
            print('Price:',x[3])
            print('Power(Hp):',x[4])
            print('Torque(Nm):',x[5])
            print('===================================')
    except:
        print('Error, unable to execute query ...')

def menu():
    while True:
        print('====================MENU====================')
        print('Press 1 to show databases')
        print('Press 2 to create table "FindCar"')
        print('Press 3 to show tables in the database')
        print('Press 4 to display structure of the table')
        print('Press 5 to add record')
        print('Press 6 to update record(s)')
        print('Press 7 to delete record(s)')
        print('Press 8 to display all record(s)')
        print('Press 9 to sort the data in descending order of power')
        print('Press 10 to search for cars of a particular fuel type')
        print('Press 11 to search for cars with price in the given range')
        print('Press 12 to exit')
        print('============================================')
        choice = int(input('Enter your choice:'))
        if choice == 1: show_database()
        elif choice == 2: create_table()
        elif choice == 3: show_tables()
        elif choice == 4: disp_struct()
        elif choice == 5: add_data()
        elif choice == 6: update_data()
        elif choice == 7: delete_data()
        elif choice == 8: disp_alldata()
        elif choice == 9: disp_desc_power()
        elif choice == 10: search_like()
        elif choice == 11 : search_between()
        elif choice == 12 :
            print('Exiting...')
            break
        else: print('Invalid Input !')

menu()
