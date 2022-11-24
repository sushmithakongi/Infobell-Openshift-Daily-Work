create table IF NOT EXISTS employeeinfo(
                    id int  primary key,
                    name varchar(40) not null,
                    salary int,
                    dept_id varchar(30))