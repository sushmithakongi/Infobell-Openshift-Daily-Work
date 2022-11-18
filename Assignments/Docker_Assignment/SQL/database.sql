use db;

create table students(
    id int not null AUTO_INCREMENT,
    name varchar(100) not null,
    age int not null,
    primary key (id)
);

insert into students(name, age) 
values("Aniket", 26), ("Sanket", 31);