from Bio import SeqIO
from Bio.Seq import Seq

ALIGNMENT_FILE_NAME = "alignment-example.fasta"
FRAGMENTS_FILE_NAME = "fragments.fasta"
FRAGMENT_NAME = "fragment"
START = 100
END = 150
REMOVE_GAPS = False

with open(FRAGMENTS_FILE_NAME, "w") as output_handle:
    for record in SeqIO.parse(ALIGNMENT_FILE_NAME, "fasta"):
        fragment_seq = record.seq[START:END]
        if REMOVE_GAPS:
            seq_wo_gaps = "".join([sign for sign in str(fragment_seq) if sign != "-"])
            fragment_seq = Seq(seq_wo_gaps)

        record.seq = fragment_seq
        record.description += f" [{FRAGMENT_NAME}]"
        SeqIO.write(record, output_handle, "fasta")
