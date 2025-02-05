# SP25_DS5111_materials

# Setting up chrome headless browser and virtual environment
Learning goals:
* Create a bootstrap script to do the base floor setup for your VM
* Install the google-chrome-stable app, so we can use the headless browser for data collection
* Take our first steps to set up a dev environment: creating a virtual environment and makefile
* Create a README documentation so a new Data Scientist could catch up quickly

# 1 Documenting and automatng a way to recreate VM for project
## 1.1 Automating the sequence to recreate VM. 
We want to be immune to a cloud instance crashing.  The `cloud` may seem permanent and solid since
it usually associated with 'backing up' important data, photos, documents etc.  However few people
realize how ephemeral cloud instances are.  What makes them fault tolerant is a good bootstrap sequence
to recreate/clone a VM quickly.  Review and or execute the manual steps, then create a general init file.
* These are the manual steps:
    - `sudo apt update`                      # To bring VM snapshot up to date with package versions
    - `sudo apt install make -y`             # so we can use makefiles
    - `sudo apt install python3.12-venv -y`  # so we can create python virtual environments
    - `sudo apt install tree`                # a usefull tool for listing files in tree form
* Create a script to execute the manual steps above.  Name it `init.sh` and check it in to your repository.


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

# to note here, you could just copy the ssh output to your github ssh keys section in settings(what I did)
# Copy your public key to add to GitHub
cat ~/.ssh/id_ed25519.pub
```

3. Configure Git credentials:
```bash
# make sure you use your actual github info, you can check in your Github settings
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

4. Clone repo:
```bash
git clone [paste your SSH clone URL from the green button on GitHub]
```

5. Run init script and add executable, very important!:
```bash
#this makes executable
chmod +x init.sh
./init.sh
```

## Project-Specific Setup(Section 2)

### 1. Install Chrome Headless Browser
need to make chrome install script, only way to get the html connection to work without error I found!
```bash
cd scripts
nano install_chrome.sh
```
```bash
#when in the install_chrome.sh script
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
```
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

### Organization prep for extra credit
Need to make sample_data dir and move non root scripts
```bash
mkdir sample_data

#moving files into there
mv ygainers.csv sample_data/
mv ygainers.html sample_data/
```

### Project Structure
Tree command to check structure
```bash
tree . -I env
```

```bash
#my example output
├── LICENSE
├── Makefile
├── README.md
├── init.sh
├── requirements.txt
├── sample_data
│   ├── ygainers.csv
│   ├── ygainers.html
│   └── ygainers_sample.csv
├── scripts
│   ├── 00_00_setup_script_for_git_github.md
│   ├── 00_01_setup_git_global_creds.sh
│   └── install_chrome.sh
└── text
    ├── README.md
    └── aws_login.md

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
 - ygainers.html: was output from running Makefile so I also moved there
 - ygainers.csv: was output from running Makefile so I also moved there
