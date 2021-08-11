#!/bin/bash

# Creates a user record for the current VSCODE user
# Gives a personalised greeting
# Adds configuration options for SQLite
# Creates run aliases
# Author: Matt Rudge

echo "Setting the greeting"
sed -i "s/USER_NAME/$_VSCODE_USER_NAME/g" ${VSCODE_REPO_ROOT}/README.md
echo "Creating the ${VSCODE_USER} user in MySQL"
mysql -e "CREATE USER '${VSCODE_USER}'@'%' IDENTIFIED BY '';" -u root
echo "Granting privileges"
mysql -e "GRANT ALL PRIVILEGES ON *.* TO '${_VSCODEUSER}'@'%' WITH GRANT OPTION;" -u root
echo "Creating .sqliterc file"
echo ".headers on" > ~/.sqliterc
echo ".mode column" >> ~/.sqliterc
echo "Adding run aliases"
echo 'alias run="python3 $GITPOD_REPO_ROOT/manage.py runserver 0.0.0.0:8000"' >> ~/.bashrc
echo 'alias python=python3' >> ~/.bashrc
echo 'alias pip=pip3' >> ~/.bashrc
echo "Done"
source ~/.bashrc
