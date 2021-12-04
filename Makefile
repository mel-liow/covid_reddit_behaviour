# covid reddit behavior
# author: Mel Liow
# date: 2021-12-01

all: docs/

# Download data
data/raw/*: src/download_datasets.py
	python src/download_datasets.py data/raw/
    
# Process the raw data 
data/processed/*: src/process_raw.py data/raw/*
	python src/process_raw.py --in_dir='data/raw/' --out_dir='data/processed/'

# Run statistical tests
analysis/stat_tests/stat_tests.csv: src/stat_tests.py data/processed/*
	python src/stat_tests.py --data_path='data/processed/' --output='analysis/stat_tests/stat_tests.csv'

# Create EDA diagrams
eda/figures/*: src/eda_script.py data/processed/*
	python src/eda_script.py --data_path='data/processed/' --output='eda/figures/'

# Write the report
reports/_build/ : eda/figures/* analysis/stat_tests/stat_tests.csv
	cp -a eda/figures/* reports/images 
	jupyter-book build --all reports/

# Copy files from _build to docs/
docs/ : reports/_build/
	cp -a reports/_build/html/. docs/

# Clean up
clean: 
	rm -rf data/raw/*
	rm -rf data/processed/*
	rm -rf analysis/stat_tests/*
	rm -rf eda/figures/*
	rm -rf reports/_build/*
	rm -rf reports/images/*
    