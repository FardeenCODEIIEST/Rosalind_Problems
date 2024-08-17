def count_nucleotides(dna_string):
    a_count = dna_string.count('A')
    c_count = dna_string.count('C')
    g_count = dna_string.count('G')
    t_count = dna_string.count('T')
    
    return a_count, c_count, g_count, t_count

with open('rosalind_dna.txt', 'r') as file:
    dna_string = file.read().strip()

a_count, c_count, g_count, t_count = count_nucleotides(dna_string)

print(a_count, c_count, g_count, t_count)
