def parse_fasta(filename):
    fasta_dict = {}
    with open(filename, 'r') as file:
        id = None
        sequence = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if id:
                    fasta_dict[id] = ''.join(sequence)
                id = line[1:]  
                sequence = []
            else:
                sequence.append(line)
        if id:
            fasta_dict[id] = ''.join(sequence)
    return fasta_dict

def calculate_gc_content(dna_string):
    gc_count = dna_string.count('G') + dna_string.count('C')
    return (gc_count / len(dna_string)) * 100

def main():
    input_filename = 'rosalind_gc.txt'  
    
    fasta_dict = parse_fasta(input_filename)
    
    max_gc_content = -1
    max_gc_id = None
    
    for id, dna_string in fasta_dict.items():
        gc_content = calculate_gc_content(dna_string)
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_id = id
    
    if max_gc_id:
        print(f"{max_gc_id}")
        print(f"{max_gc_content:.6f}")

if __name__ == "__main__":
    main()
