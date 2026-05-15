CREATE DATABASE veloxis_db;
USE veloxis_db;
create table users (
id int auto_increment primary key,
username varchar(50),
email varchar(100),
password varchar(255));
