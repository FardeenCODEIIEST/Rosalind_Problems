
def reverse_complement(dna_string):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    reverse_complement_string = ''.join(complement[base] for base in reversed(dna_string))
    
    return reverse_complement_string

with open('rosalind_revc.txt', 'r') as file:
    dna_string = file.read().strip()

reverse_complement_string = reverse_complement(dna_string)

print(reverse_complement_string)
