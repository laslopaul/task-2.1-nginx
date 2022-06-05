#!/usr/bin/env python3
# Python script to insert secure values to wp-config.php file

import requests
import re

WP_USER = "wordpressuser"
WP_PASSWD = "Wordpress1234"
WP_DATABASE = "wordpress"
WP_CONFIG_PATH = "/var/www/wordpress/wp-config.php"

# Get secure salt from Wordpress generator
r = requests.get("https://api.wordpress.org/secret-key/1.1/salt/")
salts = re.findall(r"\'.{64}\'", r.text)

# Read wp-config
with open(WP_CONFIG_PATH) as f:
    buffer = f.read()

# Insert MySQL credentials
buffer = buffer.replace("database_name_here", WP_DATABASE)
buffer = buffer.replace("username_here", WP_USER)
buffer = buffer.replace("password_here", WP_PASSWD)

# Insert previously generated salts
while salts:
    salt = salts.pop()
    buffer = buffer.replace("'put your unique phrase here'", salt, 1)

# Set the filesystem method to direct
buffer += "define( 'FS_METHOD', 'direct' );\n"

# Set the site URL
buffer += "define('WP_HOME','http://192.168.56.3/blog');\n"
buffer += "define('WP_SITEURL','http://192.168.56.3/blog');\n"

# Avoid 500 Server Error when accessing wp-admin
buffer += """$_SERVER['REQUEST_URI'] = str_replace("/wp-admin/", "/blog/wp-admin/",  $_SERVER['REQUEST_URI']);\n"""

# Write changes to wp-config
with open(WP_CONFIG_PATH, "w") as f:
    f.write(buffer)
