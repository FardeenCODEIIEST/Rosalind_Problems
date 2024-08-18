def read_fasta(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split('>')
    sequences = {}
    for record in data[1:]:
        lines = record.strip().split('\n')
        header = lines[0]
        sequence = ''.join(lines[1:])
        sequences[header] = sequence
    return list(sequences.values())

def overlap(a, b):
    max_overlap = 0
    len_a, len_b = len(a), len(b)
    for i in range(1, len_a):
        if b.startswith(a[i:]):
            max_overlap = len_a - i
            break
    return max_overlap

def merge(a, b):
    return a + b[overlap(a, b):]

def shortest_superstring(reads):
    while len(reads) > 1:
        max_overlap = -1
        best_pair = (0, 0)
        for i in range(len(reads)):
            for j in range(len(reads)):
                if i != j:
                    o = overlap(reads[i], reads[j])
                    if o > max_overlap:
                        max_overlap = o
                        best_pair = (i, j)
        if max_overlap == 0:
            break
        i, j = best_pair
        new_read = merge(reads[i], reads[j])
        reads[i] = new_read
        del reads[j]
    return reads[0]

fasta_file = 'rosalind_long.txt'
output_file = 'output.txt'

reads = read_fasta(fasta_file)

result = shortest_superstring(reads)

with open(output_file, 'w') as file:
    file.write(result)
