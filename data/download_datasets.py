# author: Luke Collins
# date: 2021-11-18

"""This script downloads the csv files specified in files_to_download.txt
Usage: download_datasets.py [<output_dir>]
Options:
[<output_dir>]    Takes a directory to which dataset ought to be downloaded (optional)
""" 

from docopt import docopt
import requests
opt = docopt(__doc__)

def main(output_dir=''):
    with open('files_to_download.txt') as f:
        files = f.read().splitlines()
    
    number_of_files = len(files)
    for file in files:
        filename = file.split('/')[-1]
        print(f'downloading {filename}...')
        
        req = requests.get(file)

        if opt[output_dir] is not None:
            csv_file = open(opt[output_dir] + filename, 'wb')
        else:
            csv_file = open(filename, 'wb')
        
        csv_file.write(req.content)
        csv_file.close()

        print(f'{files.index(file) + 1}/{number_of_files} file downloads complete')

if __name__ == '__main__':
    main('<output_dir>')