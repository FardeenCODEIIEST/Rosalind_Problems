def count_nucleotides(dna_string):
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0
    
    for nucleotide in dna_string:
        if nucleotide == 'A':
            count_A += 1
        elif nucleotide == 'C':
            count_C += 1
        elif nucleotide == 'G':
            count_G += 1
        elif nucleotide == 'T':
            count_T += 1
    
    return f"{count_A} {count_C} {count_G} {count_T}"

def read_dna_from_file(file_path):
    with open(file_path, 'r') as file:
        dna_string = file.read().strip() 
    return dna_string

file_path = 'rosalind_ini.txt'

dna_string = read_dna_from_file(file_path)

print(count_nucleotides(dna_string))
