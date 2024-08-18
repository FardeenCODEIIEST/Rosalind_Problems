from math import factorial

def count_perfect_matchings(s):
    # Count the occurrences of 'A', 'U', 'C', and 'G'
    base_count = {
        'A': s.count('A'),
        'U': s.count('U'),
        'C': s.count('C'),
        'G': s.count('G')
    }

    # Check if the counts of 'A' and 'U', 'C' and 'G' are the same
    if base_count['A'] != base_count['U'] or base_count['C'] != base_count['G']:
        return 0

    # Calculate the number of perfect matchings
    perfect_matchings = factorial(base_count['A']) * factorial(base_count['C'])
    
    return perfect_matchings

def read_rna_from_file(filename):
    with open(filename, 'r') as file:
        rna_string = ''
        for line in file:
            if not line.startswith('>'):
                rna_string += line.strip()
    return rna_string

rna_string = read_rna_from_file("rosalind_pmch.txt")
print(count_perfect_matchings(rna_string))
