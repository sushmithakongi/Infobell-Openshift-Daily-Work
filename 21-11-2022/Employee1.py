import psycopg2

conn= psycopg2.connect(host="host.docker.internal",dbname="malkeet",user="postgres",password="postgres",port="5432")
cur = conn.cursor()


insert_script='insert into employeeinfo (id,name,salary,dept_id) values (%s,%s,%s,%s)'
list_values=[]
for i in range(1):
    a=int(input("Enter id"))
    b=input("Enter Name")
    c=int(input("Enter Salary"))
    d=input("Enter Dept id")
    insert_values= (a,b,c,d)
    list_values.append(insert_values)
for i in list_values:
    cur.execute(insert_script,i)

cur.execute('Select * from employeeinfo')
get_all_data= cur.fetchall()

print(get_all_data)
conn.commit()
cur.close()
conn.close()