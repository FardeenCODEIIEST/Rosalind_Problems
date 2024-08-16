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

def build_profile_matrix(dna_strings):
    length = len(dna_strings[0])
    profile_matrix = {'A': [0] * length, 'C': [0] * length, 'G': [0] * length, 'T': [0] * length}
    
    for string in dna_strings:
        for i in range(length):
            profile_matrix[string[i]][i] += 1
    
    return profile_matrix

def build_consensus_string(profile_matrix):
    length = len(profile_matrix['A'])
    consensus = []
    
    for i in range(length):
        counts = {nucleotide: profile_matrix[nucleotide][i] for nucleotide in 'ACGT'}
        consensus.append(max(counts, key=counts.get))
    
    return ''.join(consensus)

def save_results(consensus, profile_matrix, output_filename):
    with open(output_filename, 'w') as file:
        file.write(consensus + '\n')
        for nucleotide in 'ACGT':
            file.write(f"{nucleotide}: {' '.join(map(str, profile_matrix[nucleotide]))}\n")

def main():
    input_filename = 'rosalind_cons.txt'  
    output_filename = 'consensus_output.txt'
    
    dna_strings = read_fasta(input_filename)
    
    profile_matrix = build_profile_matrix(dna_strings)
    
    consensus = build_consensus_string(profile_matrix)
    
    save_results(consensus, profile_matrix, output_filename)

if __name__ == "__main__":
    main()
