## DNA2pro

Program for translating DNA sequences in FASTA to proteins FASTA. Can filter out short translated sequences

### Requirements
Before run install biopython library:

        pip install biopython

### Usage
Before running specify initial data in `DNA2pro.py` script:

- **DNA_FILE_NAME** - input filename with DNA sequences in FASTA format
- **PRO_FILE_NAME** - output filename with proteins sequences in FASTA format
- **FILTERING** - filtering of translated protein sequences, integer number (0 - no filtering, 1 and more - translations that has continuous sequence of length less than specified value will be dropped, continuous sequence - protein sequence before first stop '*')

To run program from terminal print: 

        python DNA2pro.py 
