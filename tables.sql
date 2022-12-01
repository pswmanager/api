CREATE TABLE IF NOT EXISTS USERS(
    id int auto_increment,
    username varchar(20),
    password varchar(10),
    email varchar(30),
    primary key(id, username)
);

drop table PASSWORDS;
 
CREATE TABLE IF NOT EXISTS PASSWORDS1(
	id int auto_increment primary key,
    platform varchar(20),
    username varchar(20),
    password varchar(20),
    user_id int not null,
    foreign key(user_id) references USERS(id) on update cascade on delete cascade
);