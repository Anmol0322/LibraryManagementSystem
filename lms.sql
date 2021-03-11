create database lms;
use lms;
create table student(std_id int(2) primary key not null,std_name varchar(30) not null,college varchar(20) not null,branch varchar(10) not null,year int(2) not null,library varchar(15) not null, ph_no bigint(11) unique);
create table book(std_id int(2) foreign key references student(std_id), book_name varchar(30) not null, author varchar(20) not null,isbn varchar(20) unique); 