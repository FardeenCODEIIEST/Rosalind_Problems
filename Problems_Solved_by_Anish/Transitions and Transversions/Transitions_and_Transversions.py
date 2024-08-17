def calculate_ratio(s1, s2):
    transitions = 0
    transversions = 0
    
    transitions_set = {'AG', 'GA', 'CT', 'TC'}
    
    for a, b in zip(s1, s2):
        if a != b:  
            pair = a + b
            if pair in transitions_set:
                transitions += 1
            else:
                transversions += 1
    
    if transversions == 0:
        ratio = float('inf')  
    else:
        ratio = transitions / transversions
    return ratio

def read_fasta(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    dna_strings = []
    current_string = []
    
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            if current_string:
                dna_strings.append(''.join(current_string))
                current_string = []
        else:
            current_string.append(line)
    
    if current_string:
        dna_strings.append(''.join(current_string))
    
    return dna_strings

def main():
    input_filename = 'rosalind_tran.txt'
    
    dna_strings = read_fasta(input_filename)
    
    s1, s2 = dna_strings[0], dna_strings[1]
    
    ratio = calculate_ratio(s1, s2)
    
    print(f"{ratio:.11f}")

if __name__ == "__main__":
    main()
