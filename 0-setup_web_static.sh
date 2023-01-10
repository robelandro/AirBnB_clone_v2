#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static

# Make sure nginx is installed
sudo apt -y update;
sudo apt install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Test file to see if everything works correctly
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    fake HTML
  </body>
    </html>" | sudo tee  /data/web_static/releases/test/index.html

# Create a symlink, recreate it if it exists

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change all ownership of folders and files inside /data to ubuntu
sudo chown -R ubuntu:ubuntu /data

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i "s/^\}$/\tlocation \/hbnb_static\/ \{\n\t\talias \/data\/web_static\/current\/\;\n\t\}\n\}/" /etc/nginx/sites-available/default
sudo service nginx restart
