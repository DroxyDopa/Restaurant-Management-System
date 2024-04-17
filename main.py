import mysql.connector
username=input("Enter your mysql user name: ")
pwd=input('Enter your mysql password: ')
mydb=mysql.connector.connect(
    host='localhost',
    user=username,
    passwd=pwd,
    database='restaurant')

mycursor=mydb.cursor()

#<-------------------------------------------------  Add Functions  ------------------------------------------------------------------------------------>
#FUNCTION TO ADD RESTAURANT INFORMATION 
addRestaurantForm="insert into restaurant1 values(%s,'%s','%s','%s','%s')"
def addRestaurant():
        num=input("Enter Restaurant ID: ")
        while len(num)!=4 or num.isnumeric()==False:
                num=input("Enter a valid 4 digit Restaurant ID: ")
        numlist=[]
        mycursor.execute('select RESTAURANT_ID from restaurant1')
        for x in mycursor:
                numlist+=x
                while int(num) in numlist:
                        num=input('Restaurant ID already exists in database. Enter another valid number: ')
        name=input("Enter Restaurant name: ")

        loc=input("Enter Restaurant Location: ")
                     
        cont=int(input("Enter contact number: "))

        OCT=input("Enter opening and closing time: ")
                
        restro=(num,name,loc,cont,OCT)
        mycursor.execute(addRestaurantForm %restro)
        mydb.commit()
        print('Restaurant details added successfully.')
        print('**********************************')


#FUNCTION TO ADD EMPLOYEE INFORMATION 
addEmployeeForm="insert into employee values(%s,'%s','%s','%s','%s')"
def addEmployee():
        num=input("Enter Employee ID: ")
        numlist=[]
        mycursor.execute('select EMP_ID from employee')
        for x in mycursor:
                numlist+=x
                while int(num) in numlist:
                        num=input('Employee ID already exists in database. Enter another valid number: ')

        fname=input("Enter Employee's First name")

        lname=input("Enter Employee's Last name: ")

        cont=int(input("Enter Employee's Contact Number: "))

        role=input("Enter Employee's Role: ")

                  
        emp=(num,fname,lname,cont,role)
        mycursor.execute(addEmployeeForm %emp)
        mydb.commit()
        print('Employee details added successfully')
        print('**********************************')


#FUNCTION TO ADD CUSTOMER INFORMATION 
addCustomerForm="insert into customer values(%s,'%s','%s','%s','%s')"
def addCustomer():
        num=input("Enter Customer ID: ")
        numlist=[]
        mycursor.execute('select Customer_Id from customer')
        for x in mycursor:
                numlist+=x
                while int(num) in numlist:
                        num=input('Customer ID already exists in database. Enter another valid number: ')

        fname=input("Enter Customer's First name")

        lname=input("Enter Customer's Last name: ")

        cont=int(input("Enter Customer's Contact Number: "))

        eid=input("Enter Customer's Email-ID: ")

                  
        cus=(num,fname,lname,cont,eid)
        mycursor.execute(addCustomerForm %cus)
        mydb.commit()
        print('Customer details added successfully')
        print('**********************************')

#FUNCTION TO ADD OWNER INFORMATION 
addOwnerForm="insert into owner values('%s','%s','%s')"
def addOwner():

        fname=input("Enter Owner's First name")

        lname=input("Enter Owner's Last name: ")

        cont=int(input("Enter Owner's Contact Number: "))
                  
        own=(fname,lname,cont)
        mycursor.execute(addOwnerForm %own)
        mydb.commit()
        print('Owner details added successfully')
        print('**********************************')


#FUNCTION TO ADD ORDER INFORMATION 
addCus_OrderForm="insert into customer_order values(%s,'%s','%s')"
def addCus_Order():
        num=input("Enter Order ID: ")
        numlist=[]
        mycursor.execute('select Order_Id from customer_order')
        for x in mycursor:
                numlist+=x
                while int(num) in numlist:
                        num=input('Order ID already exists in database. Enter another valid number: ')

        otime=input("Enter the time of Order placed: ")

        price=input("Enter the Price: ")

                  
        cusord=(num,otime,price)
        mycursor.execute(addCus_OrderForm %cusord)
        mydb.commit()
        print("Customer's order details added successfully")
        print('**********************************')

#FUNCTION TO ADD MENU INFORMATION 
addMenuForm="insert into menu values('%s','%s','%s','%s')"
def addMenu():

        name=input("Enter the name of the dish")

        price=input("Enter the price of the dish: ")

        ftype=input("Enter the type of dish: ")

        cat=input("Enter the category of dish: ")
                  
        men=(name,price,ftype,cat)
        mycursor.execute(addMenuForm %men)
        mydb.commit()
        print('Menu details added successfully')
        print('**********************************')




#<-------------------------------------------------d Delete Functions  ------------------------------------------------------------------------------------>


#FUNCTION TO DELETE Owner'S DETAILS
def delOwner():
        num=input('Enter the Contact number whose data you want to delete: ')

        mycursor.execute('select Contact from Owner where Contact = %s', (num,))
        oc = mycursor.fetchone()

        if oc is None:
                print("There is no such result entries in the database")
                print("**********************************")

        else:
                mycursor.execute("delete from Owner where Contact=%s", (num,))
                mydb.commit()
                print("Result Deleted Successfully")
                print("**********************************")


#FUNCTION TO DELETE RESTAURANT'S RESULT
def delRestaurant():
        num=input('Enter the Restaurant ID whose data you want to delete: ')

        mycursor.execute('select RESTAURANT_ID from restaurant1 where RESTAURANT_ID = %s', (num,))
        rid = mycursor.fetchone()

        if rid is None:
                print("There is no such result entries in the database")
                print("**********************************")

        else:
                mycursor.execute("delete from restaurant1 where RESTAURANT_ID=%s", (num,))
                mydb.commit()
                print("Result Deleted Successfully")
                print("**********************************")

#FUNCTION TO DELETE Employee'S DETAILS
def delEmployee():
        num=input('Enter the EMP_ID whose data you want to delete: ')

        mycursor.execute('select EMP_ID from employee where EMP_ID = %s', (num,))
        oc = mycursor.fetchone()

        if oc is None:
                print("There is no such result entries in the database")
                print("**********************************")

        else:
                mycursor.execute("delete from employee where EMP_ID=%s", (num,))
                mydb.commit()
                print("Result Deleted Successfully")
                print("**********************************")


#FUNCTION TO DELETE Customer'S DETAILS
def delCustomer():
        num=input('Enter the Customer_Id whose data you want to delete: ')

        mycursor.execute('select Customer_Id from customer where Customer_Id = %s', (num,))
        oc = mycursor.fetchone()

        if oc is None:
                print("There is no such result entries in the database")
                print("**********************************")

        else:
                mycursor.execute("delete from customer where Customer_Id=%s", (num,))
                mydb.commit()
                print("Result Deleted Successfully")
                print("**********************************")



#FUNCTION TO DELETE Menu'S DETAILS
def delMenu():
        num=input('Enter the Dish Name whose data you want to delete: ')

        mycursor.execute('select Name from menu where Name = %s', (num,))
        oc = mycursor.fetchone()

        if oc is None:
                print("There is no such result entries in the database")
                print("**********************************")

        else:
                mycursor.execute("delete from menu where Name=%s", (num,))
                mydb.commit()
                print("Result Deleted Successfully")
                print("**********************************")


#FUNCTION TO DELETE CUSTOMER'S ORDER DETAILS
def delCus_Order():
        num=input('Enter the Order Id whose data you want to delete: ')

        mycursor.execute('select Order_Id from customer_order where Order_Id = %s', (num,))
        oc = mycursor.fetchone()

        if oc is None:
                print("There is no such result entries in the database")
                print("**********************************")

        else:
                mycursor.execute("delete from customer_order where Order_Id=%s", (num,))
                mydb.commit()
                print("Result Deleted Successfully")
                print("**********************************")




#<-------------------------------------------------  Print Functions  ------------------------------------------------------------------------------------>
#FUNCTION TO GET CUSTOMER DETAILS
getCustomerForm="select * from customer"
def getCustomer():
                numlist=[]
                mycursor.execute('select Customer_Id from customer')
                for x in mycursor:
                        numlist+=x
                if len(numlist)==0:
                        print("There are no result entries in the database")
                        print("**********************************")
                        
                else:
                    mycursor.execute(getCustomerForm)
                    row=mycursor.fetchone()
                    cid=row[0]
                    fname=row[1]
                    lname=row[2]
                    con=row[3]
                    eid=row[4]
                    print("Customer ID:",cid)
                    print("Customer's First Name: ",fname)
                    print("Customer's Last Name:",lname)
                    print("Customer's Contact Number:", con)
                    print("Customer's Email-ID:", eid)
                    print('**********************************')



#FUNCTION TO GET EMPLOYEE DETAILS
getEmployeeForm="select * from employee"
def getEmployee():
                numlist=[]
                mycursor.execute('select EMP_ID from employee')
                for x in mycursor:
                        numlist+=x
                if len(numlist)==0:
                        print("There are no result entries in the database")
                        print("**********************************")
                        
                else:
                    mycursor.execute(getEmployeeForm)
                    row=mycursor.fetchone()
                    eid=row[0]
                    fname=row[1]
                    lname=row[2]
                    con=row[3]
                    job=row[4]
                    print("Employee ID:",eid)
                    print("Employee's First Name: ",fname)
                    print("Employee's Last Name:",lname)
                    print("Employee's Contact Number:", con)
                    print("Employee's Email-ID:", job)
                    print('**********************************')


#FUNCTION TO GET OWNER DETAILS
getOwnerForm="select * from owner"
def getOwner():
                numlist=[]
                mycursor.execute('select Fname from owner')
                for x in mycursor:
                        numlist+=x
                if len(numlist)==0:
                        print("There are no result entries in the database")
                        print("**********************************")
                        
                else:
                    mycursor.execute(getOwnerForm)
                    row=mycursor.fetchone()
                    fname=row[0]
                    lname=row[1]
                    con=row[2]
                    print("Owner's First Name:",fname)
                    print("Owner's Last Name:",lname)
                    print("Owner's Contact Number:", con)
                    print('**********************************')

#FUNCTION TO GET RESTAURANT DETAILS
getRestaurantForm="select * from Restaurant1"
def getRestaurant():
                numlist=[]
                mycursor.execute('select RESTAURANT_ID from Restaurant1')
                for x in mycursor:
                        numlist+=x
                if len(numlist)==0:
                        print("There are no result entries in the database")
                        print("**********************************")
                        
                else:
                    mycursor.execute(getRestaurantForm)
                    row=mycursor.fetchone()
                    rid=row[0]
                    name=row[1]
                    loc=row[2]
                    con=row[3]
                    OCT=row[4]
                    print("Restaurant ID:",rid)
                    print("Restaurant's Name:",name)
                    print("Restaurant's Location:",loc)
                    print("Restaurant's Contact Number:", con)
                    print("Restaurant's Opening and Closing time are ", OCT)
                    print('**********************************')

#FUNCTION TO GET CUSTOMER'S ORDER DETAILS
getCus_OrderForm="select * from customer_order"
def getCus_Order():
                numlist=[]
                mycursor.execute('select Order_Id from customer_order')
                for x in mycursor:
                        numlist+=x
                if len(numlist)==0:
                        print("There are no result entries in the database")
                        print("**********************************")
                        
                else:
                    mycursor.execute(getCus_OrderForm)
                    row=mycursor.fetchone()
                    oid=row[0]
                    ot=row[1]
                    price=row[2]
                    print("Order ID:",oid)
                    print("Order time: ",ot)
                    print("The Total Bill:",price)


#FUNCTION TO GET MENU DETAILS
getMenuForm="select * from Menu"
def getMenu():
                numlist=[]
                mycursor.execute('select Name from Menu')
                for x in mycursor:
                        numlist+=x
                if len(numlist)==0:
                        print("There are no result entries in the database")
                        print("**********************************")
                        
                else:
                    mycursor.execute(getMenuForm)
                    row=mycursor.fetchone()
                    name=row[0]
                    price=row[1]
                    typ=row[2]
                    cat=row[3]
                    print("Name of the Dish: ",name)
                    print("Price of the Dish: ",price)
                    print("Type of food(veg/non-veg/vegan): ",typ)
                    print("Category(Appetizer/Entree/Dessert): ", cat)
                    print('**********************************')

                    
                        
#<-------------------------------------------------  Main Code  ------------------------------------------------------------------------------------------>

while True:
        a=int(input("1. Add Information\n2. Get Information\n3. Delete Information\n4. Exit\nEnter the number correlating to your choice:"))
        
        if a == 1:
                print("1.  Add Customer Information")
                print("2.  Add Employee Information")
                print("3.  Add Restaurant Information")
                print("4.  Add Customer Order information")
                print("5.  Add items on the menu")
                print("6.  Add Owner Details")

                x1=int(input("Enter the number correlating to your choice: "))
                if x1 == 1:
                        addCustomer()
                elif x1 == 2:
                        addEmployee()
                elif x1 == 3:
                        addRestaurant()
                elif x1 == 4:
                        addCus_Order()
                elif x1 == 5:
                        addMenu()
                elif x1 == 6:
                        addOwner()
                else:
                        print("Please enter a number between 1 and 6")

        elif a == 2:
                print("1. Get Customer Information")
                print("2. Get Employee Information")
                print("3. Get Restaurant Information")
                print("4. Get Customer Order Information")
                print("5. Get Menu")
                print("6. Get Owner Information")

                x2=int(input("Enter the number correlating to your choice: "))
                if x2 == 1:
                        getCustomer()
                elif x2 == 2:
                        getEmployee()
                elif x2 == 3:
                        getRestaurant()
                elif x2 == 4:
                        getCus_Order()
                elif x2 == 5:
                        getMenu()
                elif x2 == 6:
                        getOwner()
                else:
                        print("Please enter a number between 1 and 6")

        elif a == 3:
                print("1. Delete Customer Information")
                print("2. Delete Employee Information")
                print("3. Delete Restaurant Information")
                print("4. Delete Customer Order Information")
                print("5. Delete Items on the Menu")
                print("6. Delete Owner Information")

                x3=int(input("Enter the number correlating to your choice: "))
                if x3 == 1:
                        delCustomer()
                elif x3 == 2:
                        delEmployee()
                elif x3 == 3:
                        delRestaurant()
                elif x3 == 4:
                        delCus_Order()
                elif x3 == 5:
                        delMenu()
                elif x3 == 6:
                        delOwner()
                else:
                        print("Please enter a number between 1 and 6")

        elif a == 4:
                exit()
        else:
                print("Please enter a number between 1 and 4")
        print("\n\n\n")
