from Bio import SeqIO

DNA_FILE_NAME = "dna-example.fasta"
PRO_FILE_NAME = "proteins.fasta"
FILTERING = 200


with open(PRO_FILE_NAME, "w") as output_handle:
    for record in SeqIO.parse(DNA_FILE_NAME, "fasta"):
        draft_translation = record.seq.translate()
        if FILTERING > 0:
            first_stop = draft_translation.find("*")
            if first_stop == -1:
                first_protein = draft_translation
            else:
                first_protein = draft_translation[:first_stop]

            if len(first_protein) >= FILTERING:
                record.seq = first_protein
                SeqIO.write(record, output_handle, "fasta")
        else:
            record.seq = draft_translation
            SeqIO.write(record, output_handle, "fasta")
