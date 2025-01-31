# SP25_DS5111_materials

Reading and lab resources for DS5111 Spring 2025

## VM Setup Instructions

1. run the following to update sys packages

   
sudo apt update

## Setup Git credentials and SSH key(from first week)

2.generate SSH key and configure

### gen SSH key

ssh-keygen -t ed25519 -C "your-email@example.com"

### Start ssh-agent and add key

eval "$(ssh-agent -s)" ssh-add ~/.ssh/id_ed25519

### Copy your public key to add to GitHub

cat ~/.ssh/id_ed25519.pub

### Configure Git credentials

3. global creds

git config --global user.name "Your Name" git config --global user.email "your-email@example.com"

### Clone repo
4. clone repo

git clone [paste your SSH clone URL from the green button on GitHub]

### Run init script
5. run init

chmod +x init.sh
./init.sh


## Project-Specific Setup

### 1. Install Chrome Headless Browser
```bash
# Execute chrome installation script
chmod +x scripts/install_chrome.sh
./scripts/install_chrome.sh

# Test chrome installation
google-chrome --headless --dump-dom https://example.com
