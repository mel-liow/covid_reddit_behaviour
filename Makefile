# covid reddit behavior
# author: Mel Liow
# date: 2021-12-01

all:
	jupyter-book build reports

# download data
data/raw/*: src/download_datasets.py
	python src/download_datasets.py data/raw/
    
# Process the raw data 
data/processed/*: src/process_raw.py
	python src/process_raw.py --in_dir='data/raw/' --out_dir='data/processed/'

# Run statistical tests
analysis/stat_tests/stat_tests.csv: src/stat_tests.py
	python src/stat_tests.py --data_path='data/processed/' --output='analysis/stat_tests/stat_tests.csv'

# Create EDA diagrams
eda/figures/ : src/processed/ eda/eda_script.py
	python src/eda_script.py --data_path='data/processed/' --output='eda/figures/'

# Write the report
reports/ : 
	jupyter-book build reports

# Clean up
clean: 
	rm -rf data/raw/*
	rm -rf data/processed/*
	rm -rf analysis/stat_tests/*
	rm -rf eda/figures/*
    