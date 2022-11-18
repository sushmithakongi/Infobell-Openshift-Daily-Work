#pip install mysql-connector-python

import mysql.connector
conn= mysql.connector.connect(host="localhost",port=3306,user="root",password="Dhiraj@123")

cur=conn.cursor()
#cur.execute("show databases")

#for i in cur:
    #print(i)

a= "redbus" #input("enter database name : ")

cur.execute(f"use {a}")
#cur.execute("show tables")

#for i in cur:
    #print(i)


b=input("enter start point : ")
b=f"{b}"
c=input("enter end point : ")
cur.execute(f"select busname,startpoint, endpoint,price,bustime from buses where lower(startpoint)=\"{b}\" and lower(endpoint) = \"{c}\"")
for i in cur:
    print("bus : ",i[0])
    print("starting point : ",i[1])
    print("ending point: ",i[2])
    print("price : ",i[3])
    #print("tier : ",i[5])
    print("time : ",i[4])
