# SP25_DS5111_materials

Reading and lab resources for DS5111 Spring 2025

## VM Setup Instructions(Section 1)

1. run the following to update sys packages:
```bash
sudo apt update
```

## Setup Git credentials and SSH key(from first week in class instruction)

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

5. Run init script and add executable, very important!:
```bash
chmod +x init.sh
./init.sh
```

## Project-Specific Setup(Section 2)

### 1. Install Chrome Headless Browser
Run the chrome installation script:
```bash
chmod +x scripts/install_chrome.sh
./scripts/install_chrome.sh

# Test chrome installation
google-chrome --headless --dump-dom https://example.com
```

### 2. Python Environment Setup(this file contents were taken from my Professors example in their Repo!)
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
source env/bin/activate  #I needed to activate env first
make ygainers.csv #then test
deactivate  #then you can/need to deactivate the env when done
```

### Project Structure
Tree command to check structure
```bash
tree ._I env
```

```bash
├── LICENSE
├── Makefile
├── README.md
├── init.sh
├── requirements.txt
├── sample_data
│   └── ygainers_sample.csv
├── scripts
│   ├── 00_00_setup_script_for_git_github.md
│   ├── 00_01_setup_git_global_creds.sh
│   └── install_chrome.sh
├── text
│   ├── README.md
│   └── aws_login.md
├── ygainers.csv
└── ygainers.html

4 directories, 13 files
```

## Directory Organization, Sample Data, and Extra Credit

### Key Directories
- Root directory: Contains essential setup files
 - init.sh: VM initialization script
 - Makefile: Manages Python environment and data collection(from professor github)
 - requirements.txt: Python dependencies(from professor github)

- scripts/: Utility scripts
 - install_chrome.sh: Chrome headless browser installer(from instructions and online sources)
 - 00_00_setup_script_for_git_github.md: Git setup guide(from first week)
 - 00_01_setup_git_global_creds.sh: Git credentials setup script(from first week)

- sample_data/: Example datasets
 - ygainers_sample.csv: Sample of scraped Yahoo Finance gainers data that was talked about in class, put in sample_data folder and labeled
