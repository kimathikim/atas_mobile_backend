CREATE DATABASE IF NOT EXISTS atas_mobile;
CREATE USER IF NOT EXISTS 'atas'@'localhost' IDENTIFIED BY 'Team_Project';
GRANT ALL PRIVILEGES ON `atas_mobile`.* TO 'atas'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'atas'@'localhost';
FLUSH PRIVILEGES;
