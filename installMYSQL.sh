#!/bin/bash

# Define the root password
MYSQL_ROOT_PASSWORD='Matei@2022'

# Update package information
echo "Updating package information..."
sudo apt update

# Install MySQL server
echo "Installing MySQL server..."
sudo apt install mysql-server -y

# Secure MySQL installation
echo "Securing MySQL installation..."
sudo mysql_secure_installation <<EOF

y
$MYSQL_ROOT_PASSWORD
$MYSQL_ROOT_PASSWORD
y
y
y
y
EOF

# Log in to MySQL and set the root password if not already set
echo "Setting MySQL root password..."
sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '$MYSQL_ROOT_PASSWORD'; FLUSH PRIVILEGES;"

# Test MySQL login with root password
echo "Testing MySQL root login..."
mysql -u root -p$MYSQL_ROOT_PASSWORD -e "SHOW DATABASES;"

echo "MySQL installation and setup complete."
