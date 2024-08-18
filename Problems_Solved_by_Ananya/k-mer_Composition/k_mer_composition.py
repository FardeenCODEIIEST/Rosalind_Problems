from collections import defaultdict

def read_fasta(fasta_file):
    with open(fasta_file, 'r') as file:
        lines = file.readlines()
        sequence = ''.join(line.strip() for line in lines[1:])
    return sequence

def count_4mers(dna_sequence):
    k = 4
    counts = defaultdict(int)
    for i in range(len(dna_sequence) - k + 1):
        kmer = dna_sequence[i:i + k]
        counts[kmer] += 1
    return counts

def generate_all_kmers(k):
    from itertools import product
    return [''.join(kmer) for kmer in product('ACGT', repeat=k)]

def main(fasta_file):
    dna_sequence = read_fasta(fasta_file)
    
    k = 4
    kmer_counts = count_4mers(dna_sequence)

    all_kmers = generate_all_kmers(k)
    
    result = [str(kmer_counts.get(kmer, 0)) for kmer in all_kmers]
    
    print(" ".join(result))

fasta_file = 'rosalind_kmer.txt'  
main(fasta_file)
