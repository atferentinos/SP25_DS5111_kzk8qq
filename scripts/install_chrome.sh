#!/bin/bash

# chrome pkg
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# install chrome
sudo apt install ./google-chrome-stable_current_amd64.deb -y

# cleaning
rm google-chrome-stable_current_amd64.deb

# test if worked
if google-chrome --version; then
    echo "chrome success!"
else
    echo "chrome failed!"
    exit 1
fi
