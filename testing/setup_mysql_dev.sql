-- Create a new database, if it already exists the code fails.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED WITH authentaiction_plugin BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev' @ 'localhost';

GRANT SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_dev'@'localhost';
