#!/bin/bash

# Update package list
sudo apt update

# Install required packages
sudo apt install make -y
sudo apt install python3.12-venv -y
sudo apt install tree -y

echo "Setup Complete!"
