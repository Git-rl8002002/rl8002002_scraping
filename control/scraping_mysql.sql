/*
 * database  scraping
 */ 
create database scraping DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
use scraping;


/*
 * network_attack
 */ 
create table network_attack(
	no int not null AUTO_INCREMENT PRIMARY KEY,
    a_time datetime null,
    a_type varchar(30) null,
    a_ip varchar(100) null,
    a_package varchar(300) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*
 * scraping_line_notify
 */ 
create table scraping_line_notify(
no int not null primary key AUTO_INCREMENT, 
s_time datetime null,
e_time datetime null,
kind varchar(300) null,
content text null,
total_counts varchar(100) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*
 * scraping_log
 */ 
create table scraping_log(
no int not null primary key AUTO_INCREMENT, 
s_time datetime null,
e_time datetime null,
kind varchar(300) null,
content text null,
total_counts varchar(100) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*
 * scraping_news
 */ 
create table scraping_news(
no int not null primary key AUTO_INCREMENT, 
r_time datetime null,
kind text null,    
title text null,
url text null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*
 * scraping_film
 */ 
create table scraping_film(
no int not null primary key AUTO_INCREMENT, 
r_time datetime null,
kind varchar(300) null,
title varchar(300) null,
url varchar(300) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


