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

### Creating Crontab Timing
This way gainers will run throughout the day
```bash
crontab -e

# Morning market open (9:31 AM ET)
31 9 * * 1-5 cd /home/ubuntu/SP25_DS5111_kzk8qq && . /home/ubuntu/SP25_DS5111_kzk8qq/env/bin/activate && /home/ubuntu/SP25_DS5111_kzk8qq/env/bin/python3 get_gainer.py --source yahoo --output-dir "Data_Collection_LAB_07"
31 9 * * 1-5 cd /home/ubuntu/SP25_DS5111_kzk8qq && . /home/ubuntu/SP25_DS5111_kzk8qq/env/bin/activate && /home/ubuntu/SP25_DS5111_kzk8qq/env/bin/python3 get_gainer.py --source wsj --output-dir "Data_Collection_LAB_07"

# Mid-day check (12:30 PM ET)
30 12 * * 1-5 cd /home/ubuntu/SP25_DS5111_kzk8qq && . /home/ubuntu/SP25_DS5111_kzk8qq/env/bin/activate && /home/ubuntu/SP25_DS5111_kzk8qq/env/bin/python3 get_gainer.py --source yahoo --output-dir "Data_Collection_LAB_07"
30 12 * * 1-5 cd /home/ubuntu/SP25_DS5111_kzk8qq && . /home/ubuntu/SP25_DS5111_kzk8qq/env/bin/activate && /home/ubuntu/SP25_DS5111_kzk8qq/env/bin/python3 get_gainer.py --source wsj --output-dir "Data_Collection_LAB_07"

# Market close (4:01 PM ET)
01 16 * * 1-5 cd /home/ubuntu/SP25_DS5111_kzk8qq && . /home/ubuntu/SP25_DS5111_kzk8qq/env/bin/activate && /home/ubuntu/SP25_DS5111_kzk8qq/env/bin/python3 get_gainer.py --source yahoo --output-dir "Data_Collection_LAB_07"
01 16 * * 1-5 cd /home/ubuntu/SP25_DS5111_kzk8qq && . /home/ubuntu/SP25_DS5111_kzk8qq/env/bin/activate && /home/ubuntu/SP25_DS5111_kzk8qq/env/bin/python3 get_gainer.py --source wsj --output-dir "Data_Collection_LAB_07"
```

### writing Entity Relationship Diagram(ERD) in mermaidjs
code for the ERD diagram made in mermaidjs
```bash
   erDiagram
    RAW_DAILY_GAINERS ||--o{ CONSOLIDATED_GAINERS : transforms_to
    RAW_DAILY_GAINERS {
        string symbol
        string name
        float price
        float change
        float change_percent
        float volume
        float avg_vol_3m
        string market_cap
        float pe_ratio
        float wk52_change
        string wk52_range
        string source
        datetime timestamp
        string file_name
    }
    
    CONSOLIDATED_GAINERS ||--o{ SYMBOL_FREQUENCY : aggregates_to
    CONSOLIDATED_GAINERS ||--o{ PRICE_DISTRIBUTION : aggregates_to
    CONSOLIDATED_GAINERS ||--o{ VOLUME_DISTRIBUTION : aggregates_to
    CONSOLIDATED_GAINERS ||--o{ DAY_OF_WEEK_STATS : aggregates_to
    CONSOLIDATED_GAINERS {
        string symbol
        string name
        float price
        float change
        float change_percent
        float volume
        float avg_vol_3m
        string market_cap
        float pe_ratio
        float wk52_change
        string wk52_range
        string source
        date date
        time time
        string day_of_week
    }
    
    SYMBOL_FREQUENCY {
        string symbol
        string name
        int appearance_count
        date first_appearance
        date last_appearance
        float avg_price
        float avg_change_percent
        int max_streak_length
        int sources_count
    }
    
    PRICE_DISTRIBUTION {
        string price_range
        int symbol_count
        int unique_symbols
        float avg_change_percent
        float median_change_percent
        float avg_volume
    }
    
    VOLUME_DISTRIBUTION {
        string volume_range
        int symbol_count
        int unique_symbols
        float avg_change_percent
        float avg_price
    }
    
    DAY_OF_WEEK_STATS {
        string day_of_week
        int gainer_count
        int unique_symbols
        float avg_change_percent
        float avg_volume
    }
    
    SYMBOL_FREQUENCY ||--o{ RECURRING_SYMBOLS_ANALYSIS : feeds_into
    RECURRING_SYMBOLS_ANALYSIS {
        string symbol
        string name
        int appearance_count
        string sources
        float avg_days_between_appearances
        float avg_price_change_between_appearances
        float appearance_frequency
        float avg_volume
        string gainer_pattern
        string performance_category
    }
    
    PRICE_DISTRIBUTION ||--o{ PRICE_RANGE_ANALYSIS : feeds_into
    PRICE_RANGE_ANALYSIS {
        string price_range
        int symbol_count
        int recurring_symbols_count
        float recurring_symbol_percentage
        float avg_appearances
        float high_performers_percentage
        float avg_volume
        float weighted_success_score
    }
    
    VOLUME_DISTRIBUTION ||--o{ VOLUME_PATTERN_ANALYSIS : feeds_into
    VOLUME_PATTERN_ANALYSIS {
        string volume_range
        float avg_change_percent
        float price_correlation
        float liquidity_score
        string trading_recommendation
    }
    
    DAY_OF_WEEK_STATS ||--o{ TRADING_PATTERN_ANALYSIS : feeds_into
    TRADING_PATTERN_ANALYSIS {
        string day_of_week
        float avg_gainers_per_day
        float avg_change_percent
        float repeat_percentage
        string volume_trend
        string trading_strategy
    }"
```
****
### Added the Diagram IMAGE to Root Directory 
Added Image so I can refer to later
```bash
#added file through github interactions
#mermaid-diagram-2025-03-23-150300.png
```
### Filed in ERD.md in root directory with Report Outline
Added Image so I can refer to later
```bash
nano ERD.md
#add the report and code for ERD
```
### Set up Snowflake login in with professor
ensured had snowflake access 
add installs to requirements folder
```bash
vim requirements.txt
dbt-core
dbt-snowflake
```
### make project directory
```bash
mkdir projects
```
### set up DBT initialization
```bash
dbt init project
Enter a Number: 1 # should be the only option
account: rja95216
user: your uva email address
password: DS5111<uvaid>
role: DS5111_DBT
warehouse: COMPUTE_WH
database: DATA_SCIENCE
schema: <uvaid>
threads: 1
```
### test dbt debug for connection
```bash
#navigate to gainers folders in projects
dbt debug
```
### test with snowflake and dbt
```bash
#create numbers.csv
nano numbers.csv
#paste
en,sp,fr,de
one,uno,un,einz
two,dos,deux,zwei
three,tres,trois,drei
```
### create models
```bash
SELECT FR 
FROM DATA_SCIENCE.ABC1234_RAW.NUMBERS;
SELECT FR 
FROM DATA_SCIENCE.ABC1234_RAW.NUMBERS
```
### schema updates
```bash

version: 2

models:
  - name: my_first_dbt_model
    description: "A starter dbt model"
    columns:
      - name: id
        description: "The primary key for this table"
        data_tests:
          - unique
          - not_null

  - name: my_second_dbt_model
    description: "A starter dbt model"
    columns:
      - name: id
        description: "The primary key for this table"
        data_tests:
          - unique
          - not_null
  - name: french 
    description: "test french table"
    columns:
      - name: FR 
        description: "The primary key for this table"
        data_tests:
          - unique
          - not_null
          - accepted_values:
              values:  ['un', 'deux', 'trois']
  - name: enfr
    description: "insure all values in en column are also in ende"
    columns:
      - name: EN
        data_tests:
          - relationships:
              to: ref('ende')
              field: EN
```
### Final Report
Place for Final Report for class
```bash
#DS5111_Final_Report
```
### Project Structure
Tree command to check structure
```bash
tree . -I env
```
```bash
.
├── DS5111_Final_Report.pdf
├── Data_Collection_LAB_07
│   ├── wsjgainers_norm_20250307_165202.csv
│   ├── wsjgainers_norm_20250307_165402.csv
│   ├── wsjgainers_norm_20250307_165602.csv
│   ├── wsjgainers_norm_20250307_185502.csv
│   ├── wsjgainers_norm_20250310_154613.csv
│   ├── wsjgainers_norm_20250310_163102.csv
│   ├── wsjgainers_norm_20250310_173002.csv
│   ├── wsjgainers_norm_20250310_191246.csv
│   ├── wsjgainers_norm_20250310_200420.csv
│   ├── wsjgainers_norm_20250311_093102.csv
│   ├── wsjgainers_norm_20250311_123002.csv
│   ├── wsjgainers_norm_20250311_160103.csv
│   ├── wsjgainers_norm_20250311_163102.csv
│   ├── wsjgainers_norm_20250312_093102.csv
│   ├── wsjgainers_norm_20250312_123002.csv
│   ├── wsjgainers_norm_20250312_160102.csv
│   ├── wsjgainers_norm_20250312_163102.csv
│   ├── wsjgainers_norm_20250313_093102.csv
│   ├── wsjgainers_norm_20250313_123002.csv
│   ├── wsjgainers_norm_20250313_160102.csv
│   ├── wsjgainers_norm_20250313_163101.csv
│   ├── wsjgainers_norm_20250314_093103.csv
│   ├── wsjgainers_norm_20250314_123002.csv
│   ├── wsjgainers_norm_20250314_160102.csv
│   ├── wsjgainers_norm_20250314_163101.csv
│   ├── wsjgainers_norm_20250315_163102.csv
│   ├── wsjgainers_norm_20250316_163102.csv
│   ├── wsjgainers_norm_20250317_093102.csv
│   ├── wsjgainers_norm_20250317_123002.csv
│   ├── wsjgainers_norm_20250317_160103.csv
│   ├── wsjgainers_norm_20250317_163102.csv
│   ├── wsjgainers_norm_20250318_093102.csv
│   ├── wsjgainers_norm_20250318_123002.csv
│   ├── wsjgainers_norm_20250318_160103.csv
│   ├── wsjgainers_norm_20250318_163102.csv
│   ├── ygainers_norm_20250306_012908.csv
│   ├── ygainers_norm_20250306_174044.csv
│   ├── ygainers_norm_20250307_165203.csv
│   ├── ygainers_norm_20250307_165402.csv
│   ├── ygainers_norm_20250307_165603.csv
│   ├── ygainers_norm_20250307_185503.csv
│   ├── ygainers_norm_20250310_154600.csv
│   ├── ygainers_norm_20250310_163003.csv
│   ├── ygainers_norm_20250310_173002.csv
│   ├── ygainers_norm_20250310_191235.csv
│   ├── ygainers_norm_20250310_200410.csv
│   ├── ygainers_norm_20250311_093102.csv
│   ├── ygainers_norm_20250311_123002.csv
│   ├── ygainers_norm_20250311_160103.csv
│   ├── ygainers_norm_20250311_163002.csv
│   ├── ygainers_norm_20250312_093103.csv
│   ├── ygainers_norm_20250312_123003.csv
│   ├── ygainers_norm_20250312_160103.csv
│   ├── ygainers_norm_20250312_163002.csv
│   ├── ygainers_norm_20250313_123003.csv
│   ├── ygainers_norm_20250313_160103.csv
│   ├── ygainers_norm_20250313_163002.csv
│   ├── ygainers_norm_20250314_093103.csv
│   ├── ygainers_norm_20250314_123003.csv
│   ├── ygainers_norm_20250314_160103.csv
│   ├── ygainers_norm_20250314_163002.csv
│   ├── ygainers_norm_20250315_163002.csv
│   ├── ygainers_norm_20250316_163002.csv
│   ├── ygainers_norm_20250317_093102.csv
│   ├── ygainers_norm_20250317_123002.csv
│   ├── ygainers_norm_20250317_160103.csv
│   ├── ygainers_norm_20250317_163002.csv
│   ├── ygainers_norm_20250318_093103.csv
│   ├── ygainers_norm_20250318_123002.csv
│   ├── ygainers_norm_20250318_160103.csv
│   └── ygainers_norm_20250318_163002.csv
├── ERD.md
├── LICENSE
├── Makefile
├── README.md
├── bin
│   ├── __pycache__
│   ├── gainers
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── base.py
│   │   ├── factory.py
│   │   ├── mock.py
│   │   ├── wsj.py
│   │   └── yahoo.py
│   └── normalize_csv.py
├── data
│   ├── wsj_gainers_norm_20250305_232906.csv
│   ├── wsjgainers_norm_20250306_010005.csv
│   ├── ygainers_norm_20250305_231843.csv
│   ├── ygainers_norm_20250306_001722.csv
│   └── ygainers_norm_20250306_010104.csv
├── get_gainer.py
├── init.sh
├── logs
│   └── dbt.log
├── mermaid-diagram-2025-04-17-090304.png
├── mock_gainers.csv
├── projects
│   ├── gainers
│   │   ├── README.md
│   │   ├── analyses
│   │   ├── dbt_project.yml
│   │   ├── logs
│   │   │   └── dbt.log
│   │   ├── macros
│   │   ├── models
│   │   │   ├── example
│   │   │   │   ├── ende.sql
│   │   │   │   ├── enfr.sql
│   │   │   │   ├── french.sql
│   │   │   │   ├── my_first_dbt_model.sql
│   │   │   │   ├── my_second_dbt_model.sql
│   │   │   │   └── schema.yml
│   │   │   └── models
│   │   │       └── stock_gainers
│   │   │           ├── gainers_consolidated.sql
│   │   │           ├── intermediate
│   │   │           │   ├── int_consolidated_gainers.sql
│   │   │           │   ├── int_daily_combined.sql
│   │   │           │   ├── int_day_of_week_stats.sql
│   │   │           │   ├── int_price_distribution.sql
│   │   │           │   ├── int_symbol_frequency.sql
│   │   │           │   └── int_symbol_performance.sql
│   │   │           ├── marts
│   │   │           │   ├── final_analysis.sql
│   │   │           │   ├── price_range_analysis.sql
│   │   │           │   ├── recurring_symbols_analysis.sql
│   │   │           │   └── trading_pattern_analysis.sql
│   │   │           ├── simplest_test.sql
│   │   │           └── sources.yml
│   │   ├── normalize_all.py
│   │   ├── seeds
│   │   │   ├── numbers.numbers
│   │   │   ├── wsjgainers_norm_20250307_165202.numbers
│   │   │   ├── wsjgainers_norm_20250307_165202_norm.csv
│   │   │   ├── wsjgainers_norm_20250307_165402.csv
│   │   │   ├── wsjgainers_norm_20250307_165602.numbers
│   │   │   ├── wsjgainers_norm_20250307_165602_norm.csv
│   │   │   ├── wsjgainers_norm_20250307_185502.numbers
│   │   │   ├── wsjgainers_norm_20250307_185502_norm.csv
│   │   │   ├── wsjgainers_norm_20250310_154613.numbers
│   │   │   ├── wsjgainers_norm_20250310_154613_norm.csv
│   │   │   ├── wsjgainers_norm_20250310_163102.numbers
│   │   │   ├── wsjgainers_norm_20250310_163102_norm.csv
│   │   │   ├── wsjgainers_norm_20250310_173002.numbers
│   │   │   ├── wsjgainers_norm_20250310_173002_norm.csv
│   │   │   ├── wsjgainers_norm_20250310_191246.numbers
│   │   │   ├── wsjgainers_norm_20250310_191246_norm.csv
│   │   │   ├── wsjgainers_norm_20250310_200420.numbers
│   │   │   ├── wsjgainers_norm_20250310_200420_norm.csv
│   │   │   ├── wsjgainers_norm_20250311_093102.numbers
│   │   │   ├── wsjgainers_norm_20250311_093102_norm.csv
│   │   │   ├── wsjgainers_norm_20250311_123002.numbers
│   │   │   ├── wsjgainers_norm_20250311_123002_norm.csv
│   │   │   ├── wsjgainers_norm_20250311_160103.numbers
│   │   │   ├── wsjgainers_norm_20250311_160103_norm.csv
│   │   │   ├── wsjgainers_norm_20250311_163102.numbers
│   │   │   ├── wsjgainers_norm_20250311_163102_norm.csv
│   │   │   ├── wsjgainers_norm_20250312_093102.numbers
│   │   │   ├── wsjgainers_norm_20250312_093102_norm.csv
│   │   │   ├── wsjgainers_norm_20250312_123002.numbers
│   │   │   ├── wsjgainers_norm_20250312_123002_norm.csv
│   │   │   ├── wsjgainers_norm_20250312_160102.numbers
│   │   │   ├── wsjgainers_norm_20250312_160102_norm.csv
│   │   │   ├── wsjgainers_norm_20250312_163102.numbers
│   │   │   ├── wsjgainers_norm_20250312_163102_norm.csv
│   │   │   ├── wsjgainers_norm_20250313_093102.numbers
│   │   │   ├── wsjgainers_norm_20250313_093102_norm.csv
│   │   │   ├── wsjgainers_norm_20250313_123002.numbers
│   │   │   ├── wsjgainers_norm_20250313_123002_norm.csv
│   │   │   ├── wsjgainers_norm_20250313_160102.numbers
│   │   │   ├── wsjgainers_norm_20250313_160102_norm.csv
│   │   │   ├── wsjgainers_norm_20250313_163101.numbers
│   │   │   ├── wsjgainers_norm_20250313_163101_norm.csv
│   │   │   ├── wsjgainers_norm_20250314_093103.numbers
│   │   │   ├── wsjgainers_norm_20250314_093103_norm.csv
│   │   │   ├── wsjgainers_norm_20250314_123002.numbers
│   │   │   ├── wsjgainers_norm_20250314_123002_norm.csv
│   │   │   ├── wsjgainers_norm_20250314_160102.numbers
│   │   │   ├── wsjgainers_norm_20250314_160102_norm.csv
│   │   │   ├── wsjgainers_norm_20250314_163101.numbers
│   │   │   ├── wsjgainers_norm_20250314_163101_norm.csv
│   │   │   ├── wsjgainers_norm_20250315_163102.numbers
│   │   │   ├── wsjgainers_norm_20250315_163102_norm.csv
│   │   │   ├── wsjgainers_norm_20250316_163102.numbers
│   │   │   ├── wsjgainers_norm_20250316_163102_norm.csv
│   │   │   ├── wsjgainers_norm_20250317_093102.numbers
│   │   │   ├── wsjgainers_norm_20250317_093102_norm.csv
│   │   │   ├── wsjgainers_norm_20250317_123002.numbers
│   │   │   ├── wsjgainers_norm_20250317_123002_norm.csv
│   │   │   ├── wsjgainers_norm_20250317_160103.numbers
│   │   │   ├── wsjgainers_norm_20250317_160103_norm.csv
│   │   │   ├── wsjgainers_norm_20250317_163102.numbers
│   │   │   ├── wsjgainers_norm_20250317_163102_norm.csv
│   │   │   ├── wsjgainers_norm_20250318_093102.numbers
│   │   │   ├── wsjgainers_norm_20250318_093102_norm.csv
│   │   │   ├── wsjgainers_norm_20250318_123002.numbers
│   │   │   ├── wsjgainers_norm_20250318_123002_norm.csv
│   │   │   ├── wsjgainers_norm_20250318_160103.numbers
│   │   │   ├── wsjgainers_norm_20250318_160103_norm.csv
│   │   │   ├── wsjgainers_norm_20250318_163102.numbers
│   │   │   ├── wsjgainers_norm_20250318_163102_norm.csv
│   │   │   ├── ygainers_norm_20250306_012908.numbers
│   │   │   ├── ygainers_norm_20250306_012908_norm.csv
│   │   │   ├── ygainers_norm_20250306_174044.numbers
│   │   │   ├── ygainers_norm_20250306_174044_norm.csv
│   │   │   ├── ygainers_norm_20250307_165203.numbers
│   │   │   ├── ygainers_norm_20250307_165203_norm.csv
│   │   │   ├── ygainers_norm_20250307_165402.numbers
│   │   │   ├── ygainers_norm_20250307_165402_norm.csv
│   │   │   ├── ygainers_norm_20250307_165603.numbers
│   │   │   ├── ygainers_norm_20250307_165603_norm.csv
│   │   │   ├── ygainers_norm_20250307_185503.numbers
│   │   │   ├── ygainers_norm_20250307_185503_norm.csv
│   │   │   ├── ygainers_norm_20250310_154600.numbers
│   │   │   ├── ygainers_norm_20250310_154600_norm.csv
│   │   │   ├── ygainers_norm_20250310_163003.numbers
│   │   │   ├── ygainers_norm_20250310_163003_norm.csv
│   │   │   ├── ygainers_norm_20250310_173002.numbers
│   │   │   ├── ygainers_norm_20250310_173002_norm.csv
│   │   │   ├── ygainers_norm_20250310_191235.numbers
│   │   │   ├── ygainers_norm_20250310_191235_norm.csv
│   │   │   ├── ygainers_norm_20250310_200410.numbers
│   │   │   ├── ygainers_norm_20250310_200410_norm.csv
│   │   │   ├── ygainers_norm_20250311_093102.numbers
│   │   │   ├── ygainers_norm_20250311_093102_norm.csv
│   │   │   ├── ygainers_norm_20250311_123002.numbers
│   │   │   ├── ygainers_norm_20250311_123002_norm.csv
│   │   │   ├── ygainers_norm_20250311_160103.numbers
│   │   │   ├── ygainers_norm_20250311_160103_norm.csv
│   │   │   ├── ygainers_norm_20250311_163002.numbers
│   │   │   ├── ygainers_norm_20250311_163002_norm.csv
│   │   │   ├── ygainers_norm_20250312_093103.numbers
│   │   │   ├── ygainers_norm_20250312_093103_norm.csv
│   │   │   ├── ygainers_norm_20250312_123003.numbers
│   │   │   ├── ygainers_norm_20250312_123003_norm.csv
│   │   │   ├── ygainers_norm_20250312_160103.numbers
│   │   │   ├── ygainers_norm_20250312_160103_norm.csv
│   │   │   ├── ygainers_norm_20250312_163002.numbers
│   │   │   ├── ygainers_norm_20250312_163002_norm.csv
│   │   │   ├── ygainers_norm_20250313_123003.numbers
│   │   │   ├── ygainers_norm_20250313_123003_norm.csv
│   │   │   ├── ygainers_norm_20250313_160103.numbers
│   │   │   ├── ygainers_norm_20250313_160103_norm.csv
│   │   │   ├── ygainers_norm_20250313_163002.numbers
│   │   │   ├── ygainers_norm_20250313_163002_norm.csv
│   │   │   ├── ygainers_norm_20250314_093103.numbers
│   │   │   ├── ygainers_norm_20250314_093103_norm.csv
│   │   │   ├── ygainers_norm_20250314_123003.numbers
│   │   │   ├── ygainers_norm_20250314_123003_norm.csv
│   │   │   ├── ygainers_norm_20250314_160103.numbers
│   │   │   ├── ygainers_norm_20250314_160103_norm.csv
│   │   │   ├── ygainers_norm_20250314_163002.numbers
│   │   │   ├── ygainers_norm_20250314_163002_norm.csv
│   │   │   ├── ygainers_norm_20250315_163002.numbers
│   │   │   ├── ygainers_norm_20250315_163002_norm.csv
│   │   │   ├── ygainers_norm_20250316_163002.numbers
│   │   │   ├── ygainers_norm_20250316_163002_norm.csv
│   │   │   ├── ygainers_norm_20250317_093102.numbers
│   │   │   ├── ygainers_norm_20250317_093102_norm.csv
│   │   │   ├── ygainers_norm_20250317_123002.numbers
│   │   │   ├── ygainers_norm_20250317_123002_norm.csv
│   │   │   ├── ygainers_norm_20250317_160103.numbers
│   │   │   ├── ygainers_norm_20250317_160103_norm.csv
│   │   │   ├── ygainers_norm_20250317_163002.numbers
│   │   │   ├── ygainers_norm_20250317_163002_norm.csv
│   │   │   ├── ygainers_norm_20250318_093103.numbers
│   │   │   ├── ygainers_norm_20250318_093103_norm.csv
│   │   │   ├── ygainers_norm_20250318_123002.numbers
│   │   │   ├── ygainers_norm_20250318_123002_norm.csv
│   │   │   ├── ygainers_norm_20250318_160103.numbers
│   │   │   ├── ygainers_norm_20250318_160103_norm.csv
│   │   │   ├── ygainers_norm_20250318_163002.numbers
│   │   │   └── ygainers_norm_20250318_163002_norm.csv
│   │   ├── snapshots
│   │   ├── target
│   │   │   ├── compiled
│   │   │   │   └── gainers
│   │   │   │       └── models
│   │   │   │           ├── example
│   │   │   │           │   ├── ende.sql
│   │   │   │           │   ├── enfr.sql
│   │   │   │           │   ├── french.sql
│   │   │   │           │   ├── my_first_dbt_model.sql
│   │   │   │           │   ├── my_second_dbt_model.sql
│   │   │   │           │   └── schema.yml
│   │   │   │           │       ├── accepted_values_french_FR__un__deux__troi.sql
│   │   │   │           │       ├── accepted_values_french_FR__un__deux__trois.sql
│   │   │   │           │       ├── not_null_french_FR.sql
│   │   │   │           │       ├── not_null_my_first_dbt_model_id.sql
│   │   │   │           │       ├── not_null_my_second_dbt_model_id.sql
│   │   │   │           │       ├── relationships_enfr_EN__EN__ref_ende_.sql
│   │   │   │           │       ├── unique_french_FR.sql
│   │   │   │           │       ├── unique_my_first_dbt_model_id.sql
│   │   │   │           │       └── unique_my_second_dbt_model_id.sql
│   │   │   │           └── models
│   │   │   │               └── stock_gainers
│   │   │   │                   ├── gainers_consolidated.sql
│   │   │   │                   ├── intermediate
│   │   │   │                   │   ├── int_daily_combined.sql
│   │   │   │                   │   ├── int_day_of_week_stats.sql
│   │   │   │                   │   ├── int_price_distribution.sql
│   │   │   │                   │   ├── int_symbol_frequency.sql
│   │   │   │                   │   ├── int_symbol_performance.sql
│   │   │   │                   │   └── int_volume_distribution.sql
│   │   │   │                   ├── marts
│   │   │   │                   │   ├── final_analysis.sql
│   │   │   │                   │   ├── price_range_analysis.sql
│   │   │   │                   │   ├── recurring_symbols_analysis.sql
│   │   │   │                   │   ├── trading_pattern_analysis.sql
│   │   │   │                   │   └── volume_pattern_analysis.sql
│   │   │   │                   ├── simplest_test.sql
│   │   │   │                   ├── source_test.sql
│   │   │   │                   ├── stg_consolidated_gainers.sql
│   │   │   │                   └── test_gainers.sql
│   │   │   ├── graph.gpickle
│   │   │   ├── graph_summary.json
│   │   │   ├── manifest.json
│   │   │   ├── partial_parse.msgpack
│   │   │   ├── run
│   │   │   │   └── gainers
│   │   │   │       ├── models
│   │   │   │       │   ├── example
│   │   │   │       │   │   ├── ende.sql
│   │   │   │       │   │   ├── enfr.sql
│   │   │   │       │   │   ├── french.sql
│   │   │   │       │   │   ├── my_first_dbt_model.sql
│   │   │   │       │   │   ├── my_second_dbt_model.sql
│   │   │   │       │   │   └── schema.yml
│   │   │   │       │   │       ├── accepted_values_french_FR__un__deux__troi.sql
│   │   │   │       │   │       ├── accepted_values_french_FR__un__deux__trois.sql
│   │   │   │       │   │       ├── not_null_french_FR.sql
│   │   │   │       │   │       ├── not_null_my_first_dbt_model_id.sql
│   │   │   │       │   │       ├── not_null_my_second_dbt_model_id.sql
│   │   │   │       │   │       ├── relationships_enfr_EN__EN__ref_ende_.sql
│   │   │   │       │   │       ├── unique_french_FR.sql
│   │   │   │       │   │       ├── unique_my_first_dbt_model_id.sql
│   │   │   │       │   │       └── unique_my_second_dbt_model_id.sql
│   │   │   │       │   └── models
│   │   │   │       │       └── stock_gainers
│   │   │   │       │           ├── gainers_consolidated.sql
│   │   │   │       │           ├── intermediate
│   │   │   │       │           │   ├── int_daily_combined.sql
│   │   │   │       │           │   ├── int_day_of_week_stats.sql
│   │   │   │       │           │   ├── int_price_distribution.sql
│   │   │   │       │           │   ├── int_symbol_frequency.sql
│   │   │   │       │           │   ├── int_symbol_performance.sql
│   │   │   │       │           │   └── int_volume_distribution.sql
│   │   │   │       │           ├── marts
│   │   │   │       │           │   ├── final_analysis.sql
│   │   │   │       │           │   ├── price_range_analysis.sql
│   │   │   │       │           │   ├── recurring_symbols_analysis.sql
│   │   │   │       │           │   ├── trading_pattern_analysis.sql
│   │   │   │       │           │   └── volume_pattern_analysis.sql
│   │   │   │       │           ├── simplest_test.sql
│   │   │   │       │           ├── source_test.sql
│   │   │   │       │           ├── stg_consolidated_gainers.sql
│   │   │   │       │           └── test_gainers.sql
│   │   │   │       └── seeds
│   │   │   │           ├── numbers.csv
│   │   │   │           ├── wsjgainers_norm_20250307_165202_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250307_165602_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250307_185502_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250310_154613_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250310_163102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250310_173002_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250310_191246_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250310_200420_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250311_093102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250311_123002_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250311_160103_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250311_163102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250312_093102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250312_123002_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250312_160102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250312_163102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250313_093102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250313_123002_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250313_160102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250313_163101_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250314_093103_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250314_123002_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250314_160102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250314_163101_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250315_163102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250316_163102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250317_093102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250317_123002_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250317_160103_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250317_163102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250318_093102_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250318_123002_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250318_160103_norm.csv
│   │   │   │           ├── wsjgainers_norm_20250318_163102_norm.csv
│   │   │   │           ├── ygainers_norm_20250306_012908_norm.csv
│   │   │   │           ├── ygainers_norm_20250306_174044_norm.csv
│   │   │   │           ├── ygainers_norm_20250307_165203_norm.csv
│   │   │   │           ├── ygainers_norm_20250307_165402_norm.csv
│   │   │   │           ├── ygainers_norm_20250307_165603_norm.csv
│   │   │   │           ├── ygainers_norm_20250307_185503_norm.csv
│   │   │   │           ├── ygainers_norm_20250310_154600_norm.csv
│   │   │   │           ├── ygainers_norm_20250310_163003_norm.csv
│   │   │   │           ├── ygainers_norm_20250310_173002_norm.csv
│   │   │   │           ├── ygainers_norm_20250310_191235_norm.csv
│   │   │   │           ├── ygainers_norm_20250310_200410_norm.csv
│   │   │   │           ├── ygainers_norm_20250311_093102_norm.csv
│   │   │   │           ├── ygainers_norm_20250311_123002_norm.csv
│   │   │   │           ├── ygainers_norm_20250311_160103_norm.csv
│   │   │   │           ├── ygainers_norm_20250311_163002_norm.csv
│   │   │   │           ├── ygainers_norm_20250312_093103_norm.csv
│   │   │   │           ├── ygainers_norm_20250312_123003_norm.csv
│   │   │   │           ├── ygainers_norm_20250312_160103_norm.csv
│   │   │   │           ├── ygainers_norm_20250312_163002_norm.csv
│   │   │   │           ├── ygainers_norm_20250313_123003_norm.csv
│   │   │   │           ├── ygainers_norm_20250313_160103_norm.csv
│   │   │   │           ├── ygainers_norm_20250313_163002_norm.csv
│   │   │   │           ├── ygainers_norm_20250314_093103_norm.csv
│   │   │   │           ├── ygainers_norm_20250314_123003_norm.csv
│   │   │   │           ├── ygainers_norm_20250314_160103_norm.csv
│   │   │   │           ├── ygainers_norm_20250314_163002_norm.csv
│   │   │   │           ├── ygainers_norm_20250315_163002_norm.csv
│   │   │   │           ├── ygainers_norm_20250316_163002_norm.csv
│   │   │   │           ├── ygainers_norm_20250317_093102_norm.csv
│   │   │   │           ├── ygainers_norm_20250317_123002_norm.csv
│   │   │   │           ├── ygainers_norm_20250317_160103_norm.csv
│   │   │   │           ├── ygainers_norm_20250317_163002_norm.csv
│   │   │   │           ├── ygainers_norm_20250318_093103_norm.csv
│   │   │   │           ├── ygainers_norm_20250318_123002_norm.csv
│   │   │   │           ├── ygainers_norm_20250318_160103_norm.csv
│   │   │   │           └── ygainers_norm_20250318_163002_norm.csv
│   │   │   ├── run_results.json
│   │   │   └── semantic_manifest.json
│   │   └── tests
│   └── logs
│       └── dbt.log
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
├── storage
│   ├── test.txt
│   ├── wsj_gainers.csv
│   ├── wsj_gainers.html
│   ├── wsj_gainers_norm.csv
│   ├── wsjgainers.csv
│   ├── wsjgainers.html
│   ├── wsjgainers_norm.csv
│   ├── ygainers.csv
│   ├── ygainers.html
│   └── ygainers_norm.csv
├── tests
│   ├── __pycache__
│   ├── test_Module_5.py
│   ├── test_environment.py
│   └── test_gainers.py
└── text
    ├── README.md
    └── aws_login.md

49 directories, 420 files
```

## Directory Organization, Sample Data, and Extra Credit
# Updated Key Directories

* **Root directory**: Contains essential setup files (`LICENSE`, `README.md`, `Makefile`, `requirements.txt`, `init.sh`, `get_gainer.py`, `pylintrc`, `ERD.md`)
* **`bin/`**: Contains Python scripts for data processing
  * `normalize_csv.py`: Script for normalizing CSV data
  * `gainers/`: Package directory for gainer data collection
    * `__init__.py`: Package initialization file
    * `base.py`: Base class for gainer implementations
    * `factory.py`: Factory pattern implementation for gainer selection
    * `mock.py`: Mock implementation for testing
    * `wsj.py`: Wall Street Journal data scraper implementation
    * `yahoo.py`: Yahoo Finance data scraper implementation
* **`Data_Collection_LAB_07/`**: Contains extensive collection of CSV files
  * Multiple `wsjgainers_norm_*.csv` files from March 7-18, 2025
  * Multiple `ygainers_norm_*.csv` files from March 6-18, 2025
* **`data/`**: Contains baseline normalized CSV files
  * `wsj_gainers_norm_*.csv`: Initial Wall Street Journal data
  * `wsjgainers_norm_*.csv`: Alternative format Wall Street Journal data
  * `ygainers_norm_*.csv`: Initial Yahoo Finance data
* **`logs/`**: Contains log files
  * `dbt.log`: DBT logging information
* **`projects/`**: Contains DBT project files
  * `gainers/`: DBT project directory
    * Standard DBT structure with models, macros, tests, etc.
    * Contains compiled SQL models in the target directory
  * `logs/`: Additional log directory for DBT
* **`sample_data/`**: Example datasets
  * `ygainers_sample.csv`: Sample of scraped Yahoo Finance gainers data
  * `ygainers.html`: HTML output from running Makefile
  * `ygainers.csv`: CSV output from running Makefile
  * `ygainers_norm.csv`: Normalized version of the CSV data
* **`scripts/`**: Utility scripts
  * `install_chrome.sh`: Chrome headless browser installer
  * `00_00_setup_script_for_git_github.md`: Git setup guide
  * `00_01_setup_git_global_creds.sh`: Git credentials setup script
* **`storage/`**: Contains data files moved from the root directory
  * Various `.csv` and `.html` files for both WSJ and Yahoo Finance data
* **`tests/`**: Contains test files for the project
  * `test_Module_5.py`: Tests for Module 5 functionality
  * `test_environment.py`: Tests for environment setup
  * `test_gainers.py`: Tests for gainers functionality
* **`text/`**: Docs
  * `README.md`: Additional documentation
  * `DS5111_Final_Report`: Final Report
  * `aws_login.md`: AWS login information

[![Feature Validation](https://github.com/atferentinos/SP25_DS5111_kzk8qq/actions/workflows/validations.yml/badge.svg?branch=LAB-08_erd_diagram)](https://github.com/atferentinos/SP25_DS5111_kzk8qq/actions/workflows/validations.yml)
