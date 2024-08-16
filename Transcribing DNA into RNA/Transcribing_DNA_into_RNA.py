def transcribe_dna_to_rna(dna_string):
    rna_string = dna_string.replace('T', 'U')
    return rna_string

with open('rosalind_rna.txt', 'r') as file:
    dna_string = file.read().strip()

rna_string = transcribe_dna_to_rna(dna_string)

print(rna_string)
