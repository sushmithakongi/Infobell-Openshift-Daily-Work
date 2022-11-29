import psycopg2
import streamlit as st

if __name__ == "__main__":
    print('Application started')
    st.title('Restaurant Management System')
    st.write(""" Address : Maharashtra, India """)

    #hostname = 'host.docker.internal'
    hostname = 'localhost'
    database = 'restaurants'
    username = 'postgres'
    pwd = 'postgress'
    port_id = 5432


    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)

        cur = conn.cursor()
        print('Connected to database successfully')

        name=st.text_input('Enter Customers name: ','NA')

        st.subheader('Details of Customers data: ')
        cur.execute('Select * from customers limit 5')
        for records in cur.fetchall():
            st.write(records[1],records[2],records[3],records[5])
            
        st.subheader('Details of Price list data: ')
        cur.execute('Select * from price_list limit 5')
        for records in cur.fetchall():
            st.write(records[1],records[2],records[4])

        st.subheader('Details of Orders data: ')
        cur.execute('Select * from orders limit 5')
        for records in cur.fetchall():
            st.write(records)

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()