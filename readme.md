## BiotextUtils

Script `dna2pro.py` is created for translating DNA sequences in FASTA to proteins FASTA. Can filter out short translated sequences.

Script `frag_align.py` is created for extracting specific fragment from all sequences in an alignment.

### Requirements
Before run install biopython library:

        pip install biopython

### dna2pro.py script
Before running specify initial data in `dna2pro.py` script:

- **DNA_FILE_NAME** - input filename with DNA sequences in FASTA format
- **PRO_FILE_NAME** - output filename for writing proteins sequences in FASTA format
- **FILTERING** - filtering of translated protein sequences, integer number (0 - no filtering, 1 and more - translations that has continuous sequence of length less than specified value will be dropped, continuous sequence - protein sequence before first stop '*')

To run program from terminal print: 

        python dna2pro.py 

### frag_align.py script
Before running specify initial data in `frag_align.py` script:

- **ALIGNMENT_FILE_NAME** - input filename with alignment in FASTA format
- **FRAGMENTS_FILE_NAME** - output filename for writing fragments in FASTA format
- **START** - start position of fragment in an alignment (numerating from 0)
- **END** - end position of fragment in an alignment (numerating from 0)
- **REMOVE_GAPS** - removing gaps in fragments

To run program from terminal print: 

        python frag_align.py 
