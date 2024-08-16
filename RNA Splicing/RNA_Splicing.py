def read_fasta(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    sequences = []
    current_sequence = []
    
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            if current_sequence:
                sequences.append(''.join(current_sequence))
                current_sequence = []
        else:
            current_sequence.append(line)
    
    if current_sequence:
        sequences.append(''.join(current_sequence))
    
    return sequences

def remove_introns(dna_string, introns):
    exon_string = dna_string
    for intron in introns:
        exon_string = exon_string.replace(intron, '')
    return exon_string

def transcribe_dna(dna):
    return dna.replace('T', 'U')

def translate_rna(rna):
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 
        'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop', 
        'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W', 'CUU': 'L', 'CUC': 'L', 
        'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 
        'CGA': 'R', 'CGG': 'R', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAU': 'N', 'AAC': 'N', 
        'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 
        'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    protein = []
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        amino_acid = codon_table.get(codon, '')
        if amino_acid == 'Stop':
            break
        protein.append(amino_acid)
    
    return ''.join(protein)

def main():
    input_filename = 'rosalind_splc.txt'  
    sequences = read_fasta(input_filename)
    
    dna_string = sequences[0]  
    introns = sequences[1:]   
    
    exon_string = remove_introns(dna_string, introns)
    rna_string = transcribe_dna(exon_string)
    protein_string = translate_rna(rna_string)
    
    print(protein_string)

if __name__ == "__main__":
    main()
