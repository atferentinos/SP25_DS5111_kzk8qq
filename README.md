# SP25_DS5111_materials

# Setting up chrome headless browser and virtual environment
Learning goals:
* Create a bootstrap script to do the base floor setup for your VM
* Install the google-chrome-stable app, so we can use the headless browser for data collection
* Take our first steps to set up a dev environment: creating a virtual environment and makefile
* Create a README documentation so a new Data Scientist could catch up quickly
* *write a CSV normalizer to standardize data from different sources
* add a linter to automate base
* add tests and automate with the makefile
* pylint to refactor our code
* get workflow operational
* add badge to demonstrate the test are passing
* applying Design Patterns to code

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
This repository includes a CSV normalizer tool that standardizes CSV files from different sources to a consistent format.
```bash
mkdir sample_data

#moving files into there
mv ygainers.csv sample_data/
mv ygainers.html sample_data/
```
### Create new branch for this lab section
create a new branch
```bash
git status
git checkout -b LAB-03_csv_normalizer
git push
git push --set-upstream origin LAB-03_csv_normalizer
git push
```

### CSV Normalizer Tool
Need to make sample_data dir and move non root scripts
```bash
#create directory bin
mkdir bin

#new file
nano bin/normalize_csv.py
```
### CSV Normalizer Tool
Code for the tool
```bash
#add csv normalizer code you will write
```

### Installing pylint
install pylint
```bash
nano requirements.txt
#add pylint 
```

### Test pylint
test pylint
```bash
pylint bin/normalize_csv.py

pylint --generate-rcfile >> pylintrc
```

### Add pylint to Makefile
add pylint to makefile
```bash
lint: 
        pylint bin/normalize_csv.py
```

### Setting up pytest
add pytest to requirements.txt file
```bash
nano requirements.txt
#add pytest
make update 
```
### Setting up pytest
create tests directory
```bash
mkdir tests
```

### create test py file
create test py file
```bash
nano test_Module_5.py
#insert test code to there
```

### test the pytest
test the pytest file
```bash
#run
pytest -vv tests
```

### add pytest to Makefile
add pytest to makefile
```bash
test: lint
        pytest -vvx tests
```
### github directory and file addition
add github workflows and file
```bash
mkdir .github/workflows
touch .github/workflows/validations.yml
```
### add yml content
insert info for feature validation
```bash
#insert code for workflow valdiation
name: Feature Validation

on:
  push:
  workflow_dispatch:

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10"]

    steps:
      - uses: actions/checkout@v4
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          make update
      - name: Test with pytest
        run: |
          make test
```

### optional to delete push in the automation
```bash
name: Feature Validation
on:

  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11"]
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python3 -m venv env
          source env/bin/activate
          pip install --upgrade pip
          pip install pytest pylint
          pip install -r requirements.txt
      - name: Run tests and linting
        run: |
          source env/bin/activate
          make test
```

### Create directory Structure and add files
directory structure 
```bash
cd bin
mkdir gainers
cd gainers
nano factory.py
nano base.py
nano wsj.py
nano yahoo.py
cd
nano get_gainer.py
```

### Use example script to file in .py files
example script supplied fill in factory,base,wsj,yahoo
```bash
#nano into each file and adjust code with script template with code from previous lab
```
### update Makefile to include gainers
adding info to makefile to elaborate on testing 
```bash
vim makefile

gainers:
        @if [ -z "$(SRC)" ]; then \
                echo "Error: SRC parameter is required"; \
                echo "Usage: make gainers SRC=yahoo"; \
                echo "   or: make gainers SRC=wsj"; \
                exit 1; \
        fi
        @echo "Processing gainers data from $(SRC)..."
        @python get_gainer.py $(SRC)
```

### add test file to tests
adding test file to tests to test gainers
```bash
cd tests
nano test_gainers.py
#insert code to test
#this will allow us to run tests with make file
```

### test Makefile and test
run make test, should achieve high lint score and pass all tests
```bash
make test
```

### add mock class EXTRA CREDIT OPTION
adding mock tests to run test without the need for download
```bash
# add mock to factory and section to test mock in test_gainers
#example
from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo
from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ
from bin.gainers.mock import GainerDownloadMock, GainerProcessMock

class GainerFactory:
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj', 'test'], f"Unrecognized gainer type {choice}"
        self.choice = choice 
    
    def get_downloader(self):
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()
        elif self.choice == 'test':
            return GainerDownloadMock()
    
    def get_processor(self):
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        elif self.choice == 'wsj':
            return GainerProcessWSJ()
        elif self.choice == 'test':
            return GainerProcessMock()
```

### push changes
push changes of normalizer code
```bash
git add  all .
git commit -m "note"
git push
```

### activate the environment to test Yahoo and WSJ
testing gainers
```bash
source env/bin/activate
make gainers SRC=yahoo
make gainers SRC=wsj
```

### update Makefile
update Makefile to encorporate gainers
```bash
gainers:
        @if [ -z "$(SRC)" ]; then \
                echo "Error: Please specify source with SRC=yahoo or SRC=wsj"; \
                exit 1; \
        fi
        python get_gainer.py --source $(SRC) --output-dir $(OUTPUT_DIR)
```

### make storage for data collection
Data_Collection
```bash
mkdir Data_Collection_LAB_07
```

### add timing for CRON
This way gainers will run throughout the day
```bash
crontab -e

# Morning market open (9:31 AM EST)
31 9 * * 1-5 cd /home/ubuntu/SP25_DS5111_kzk8qq && make gainers SRC=yahoo OUTPUT_DIR=Data_Collection_LAB_07
31 9 * * 1-5 cd /home/ubuntu/SP25_DS5111_kzk8qq && make gainers SRC=wsj OUTPUT_DIR=Data_Collection_LAB_07

# Mid-day check (12:30 PM EST)
30 12 * * 1-5 cd /home/ubuntu/SP25_DS5111_kzk8qq && make gainers SRC=yahoo OUTPUT_DIR=Data_Collection_LAB_07
30 12 * * 1-5 cd /home/ubuntu/SP25_DS5111_kzk8qq && make gainers SRC=wsj OUTPUT_DIR=Data_Collection_LAB_07

# Market close (4:01 PM EST)
1 16 * * 1-5 cd /home/ubuntu/SP25_DS5111_kzk8qq && make gainers SRC=yahoo OUTPUT_DIR=Data_Collection_LAB_07
1 16 * * 1-5 cd /home/ubuntu/SP25_DS5111_kzk8qq && make gainers SRC=wsj OUTPUT_DIR=Data_Collection_LAB_07
```
****

### Project Structure
Tree command to check structure
```bash
tree . -I env
```

```bash
.
├── LICENSE
├── Makefile
├── README.md
├── bin
│   ├── __pycache__
│   │   └── normalize_csv.cpython-312.pyc
│   ├── gainers
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── base.cpython-312.pyc
│   │   │   ├── factory.cpython-312.pyc
│   │   │   ├── mock.cpython-312.pyc
│   │   │   ├── wsj.cpython-312.pyc
│   │   │   └── yahoo.cpython-312.pyc
│   │   ├── base.py
│   │   ├── factory.py
│   │   ├── mock.py
│   │   ├── wsj.py
│   │   └── yahoo.py
│   └── normalize_csv.py
├── get_gainer.py
├── init.sh
├── mock_gainers.csv
├── pylintrc
├── requirements.txt
├── sample_data
│   ├── ygainers.csv
│   ├── ygainers.html
│   ├── ygainers_norm.csv
│   └── ygainers_sample.csv
├── scripts
│   ├── 00_00_setup_script_for_git_github.md
│   ├── 00_01_setup_git_global_creds.sh
│   └── install_chrome.sh
├── test.txt
├── tests
│   ├── __pycache__
│   │   ├── test_Module_5.cpython-312-pytest-7.4.4.pyc
│   │   ├── test_Module_5.cpython-312-pytest-8.3.4.pyc
│   │   ├── test_environment.cpython-312-pytest-7.4.4.pyc
│   │   └── test_gainers.cpython-312-pytest-7.4.4.pyc
│   ├── test_Module_5.py
│   ├── test_environment.py
│   └── test_gainers.py
└── text
    ├── README.md
    └── aws_login.md

10 directories, 39 files
```

## Directory Organization, Sample Data, and Extra Credit

### Key Directories
* Root directory: Contains essential setup files
* `bin/`: Contains Python scripts for data processing
 * `normalize_csv.py`: Script for normalizing CSV data
 * `gainers/`: Package directory for gainer data collection
   * `__init__.py`: Package initialization file
   * `base.py`: Base class for gainer implementations
   * `factory.py`: Factory pattern implementation for gainer selection
   * `mock.py`: Mock implementation for testing
   * `wsj.py`: Wall Street Journal data scraper implementation
   * `yahoo.py`: Yahoo Finance data scraper implementation
* `init.sh`: VM initialization script
* `Makefile`: Manages Python environment and data collection
* `requirements.txt`: Python dependencies
* `scripts/`: Utility scripts
 * `install_chrome.sh`: Chrome headless browser installer
 * `00_00_setup_script_for_git_github.md`: Git setup guide
 * `00_01_setup_git_global_creds.sh`: Git credentials setup script
* `sample_data/`: Example datasets
 * `ygainers_sample.csv`: Sample of scraped Yahoo Finance gainers data
 * `ygainers.html`: HTML output from running Makefile
 * `ygainers.csv`: CSV output from running Makefile
 * `ygainers_norm.csv`: Normalized version of the CSV data
* `tests/`: Contains test files for the project
 * `test_Module_5.py`: Tests for Module 5 functionality
 * `test_environment.py`: Tests for environment setup
 * `test_gainers.py`: Tests for gainers functionality

[![Feature Validation](https://github.com/atferentinos/SP25_DS5111_kzk8qq/actions/workflows/validations.yml/badge.svg)](https://github.com/atferentinos/SP25_DS5111_kzk8qq/actions/workflows/validations.yml)
