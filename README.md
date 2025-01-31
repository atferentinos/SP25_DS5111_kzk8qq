# SP25_DS5111_materials

Reading and lab resources for DS5111 Spring 2025

## VM Setup Instructions

1. run the following to update sys packages:
```bash
sudo apt update
```

## Setup Git credentials and SSH key(from first week)

2.generate SSH key and configure:
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your-email@example.com"

# Start ssh-agent and add key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy your public key to add to GitHub
cat ~/.ssh/id_ed25519.pub
```

3. Configure Git credentials:
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

4. Clone repo:
```bash
git clone [paste your SSH clone URL from the green button on GitHub]
```

5. Run init script:
```bash
chmod +x init.sh
./init.sh
```

## Project-Specific Setup

### 1. Install Chrome Headless Browser
Run the chrome installation script:
```bash
chmod +x scripts/install_chrome.sh
./scripts/install_chrome.sh

# Test chrome installation
google-chrome --headless --dump-dom https://example.com
```

### 2. Python Environment Setup
Our requirements.txt contains:
- pandas
- lxml

### 3. Virtual Environment Setup
Create and update virtual environment:
```bash
make update
```

### 4. Test Setup
Test the headless browser:
```bash
make ygainers.csv
```

### Project Structure
Use tree command to see structure:
```bash
tree . -I env
```
