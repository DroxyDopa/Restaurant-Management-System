import mysql.connector

username=input("Enter your mysql user name: ")
pwd=input('Enter your mysql password: ')
mydb=mysql.connector.connect(
    host='localhost',
    user=username,
    passwd=pwd)
mycursor=mydb.cursor()
mycursor.execute("drop database if exists restaurant;")
mydb.commit
mycursor.execute("create database restaurant")
mydb.commit()
mydb=mysql.connector.connect(
    host='localhost',
    user=username,
    passwd=pwd,
    database='restaurant')
mycursor=mydb.cursor()

mycursor.execute("create table RESTAURANT1(RESTAURANT_ID int primary key, Name varchar(100) NOT NULL, Location varchar(100) NOT NULL, Contact varchar(100) NOT NULL, Opening_Closing_Time varchar(100) NOT NULL)")
mydb.commit()

mycursor.execute("create table OWNER(Fname varchar(15) NOT NULL, Lname varchar(15) NOT NULL, Contact varchar(100) NOT NULL)")
mydb.commit()

mycursor.execute("create table EMPLOYEE(EMP_ID int primary key, Fname varchar(15) NOT NULL, Lname varchar(15) NOT NULL, Contact varchar(20) NOT NULL, Job_Role varchar(30) NOT NULL)")
mydb.commit()

mycursor.execute("create table CUSTOMER(Customer_Id int PRIMARY KEY, Fname varchar(50) NOT NULL, Lname varchar(50) NOT NULL, Contact_Number varchar(50) NOT NULL, Email_Id varchar(50) DEFAULT NULL)")
mydb.commit()

mycursor.execute("create table MENU(Name varchar(100) NOT NULL, Price varchar(20) NOT NULL, Type varchar(20) DEFAULT NULL, Category varchar(30) NOT NULL)")
mydb.commit()

mycursor.execute("create table CUSTOMER_ORDER(Order_Id int primary key, Order_time varchar(20) NOT NULL, price varchar(20) NOT NULL)")
mydb.commit()

print("Database Created Successfully!")

