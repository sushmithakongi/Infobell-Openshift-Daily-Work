import psycopg2
import streamlit as st

st.title('Employee Information')

input1=st.number_input("Enter id")
input2=st.text_input("Enter Name")
input3=st.number_input("Enter Salary")
input4=st.text_input("Enter Dept id")

conn= psycopg2.connect(host="127.0.0.1",dbname="malkeet",user="postgres",password="postgres",port="5432")
cur = conn.cursor()

create_script='''create table IF NOT EXISTS employeeinfo(
                    id int  primary key,
                    name varchar(40) not null,
                    salary int,
                    dept_id varchar(30))'''
cur.execute(create_script)
insert_script='insert into employeeinfo (id,name,salary,dept_id) values (%s,%s,%s,%s)'
list_values=[]
for i in range(1):
    a=input1
    b=input2
    c=input3
    d=input4
    insert_values= (a,b,c,d)
    list_values.append(insert_values)
for i in list_values:
    cur.execute(insert_script,i)
'''
cur.execute('Select * from employeeinfo')
s=cur.fetchall()
for i in s:
    st.write(i)
'''
conn.commit()
cur.close()
conn.close()