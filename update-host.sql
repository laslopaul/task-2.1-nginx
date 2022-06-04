# Update wordpress hostname to make it work under /blog endpoint
# You need to run this script after completing WP installation

UPDATE wp_options SET option_value="http://192.168.56.3/blog/" WHERE option_name="siteurl";
UPDATE wp_options SET option_value="http://192.168.56.3/blog/" WHERE option_name="home";
