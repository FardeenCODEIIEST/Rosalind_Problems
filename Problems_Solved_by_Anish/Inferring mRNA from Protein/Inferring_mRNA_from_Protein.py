codon_table = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4,
    'H': 2, 'I': 3, 'K': 2, 'L': 6, 'M': 1, 'N': 2,
    'P': 4, 'Q': 2, 'R': 6, 'S': 6, 'T': 4, 'V': 4,
    'W': 1, 'Y': 2, 'Stop': 3
}

def calculate_rna_possibilities(protein_string):
    total_possibilities = 1
    
    for amino_acid in protein_string:
        total_possibilities *= codon_table[amino_acid]
        total_possibilities %= 1000000  
    
    total_possibilities *= codon_table['Stop']
    total_possibilities %= 1000000  
    
    return total_possibilities

with open('rosalind_mrna.txt', 'r') as file:
    protein_string = file.read().strip()

total_possibilities = calculate_rna_possibilities(protein_string)

print(total_possibilities)
