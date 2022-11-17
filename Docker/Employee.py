import streamlit as st
import psycopg2

st.title('Employee Information')

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
    a=st.number_input("Enter id")
    b=st.text_input("Enter Name")
    c=st.number_input("Enter Salary")
    d=st.number_input("Enter Dept id")
    insert_values= (a,b,c,d)
    list_values.append(insert_values)
cur.execute(insert_script,list_values)
'''
cur.execute('Select * from employeeinfo')
s=cur.fetchall()
st.write(s)
'''
conn.commit()
cur.close()
conn.close()