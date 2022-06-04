# Create Wordpress database and user

CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
CREATE USER 'wordpressuser'@'localhost' IDENTIFIED BY 'Wordpress1234';

GRANT ALL ON wordpress.* TO 'wordpressuser'@'localhost';