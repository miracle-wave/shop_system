create database if not exists shop_system default charset utf8;

create table if not exists Stock(txm int unsigned not null, jj float not null, cgsl int not null, cgrq datetime not null) default charset utf8;

create table if not exists Inventory(txm int unsigned not null, spmc varchar(50) not null, sccs varchar(50) not null, spgg varchar(50) not null, lsj float not null, kcl int unsigned not null) default charset utf8;

create table if not exists Sellgoods(txm int unsigned not null, spmc varchar(50) not null, xssl int unsigned not null, xssj datetime not null) default charset utf8;











