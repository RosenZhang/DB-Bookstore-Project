CREATE DATABASE dbproject CHARACTER SET UTF8;

CREATE USER DBprojectUser@localhost IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON dbproject.* TO DBprojectUser@localhost;

FLUSH PRIVILEGES;
