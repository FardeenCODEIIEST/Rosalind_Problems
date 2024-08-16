def read_fasta(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    dna_string = ''.join(line.strip() for line in lines if not line.startswith('>'))
    
    return dna_string

def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

def find_reverse_palindromes(dna, min_length=4, max_length=12):
    length = len(dna)
    results = []
    
    for size in range(min_length, max_length + 1):
        for i in range(length - size + 1):
            substring = dna[i:i + size]
            if substring == reverse_complement(substring):
                results.append((i + 1, size))
    
    return results

def write_results_to_file(results, output_filename):
    with open(output_filename, 'w') as file:
        for position, length in results:
            file.write(f"{position} {length}\n")

def main():
    input_filename = 'rosalind_revp.txt'  
    output_filename = 'reverse_palindromes.txt'  
    
    dna_string = read_fasta(input_filename)
    
    palindromes = find_reverse_palindromes(dna_string)
    
    write_results_to_file(palindromes, output_filename)

if __name__ == "__main__":
    main()
