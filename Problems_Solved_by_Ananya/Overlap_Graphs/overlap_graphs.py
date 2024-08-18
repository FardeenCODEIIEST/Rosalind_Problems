def parse_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        label = None
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                label = line[1:]
                sequences[label] = ""
            else:
                if label is not None:
                    sequences[label] += line
    return sequences

def find_overlap_edges(sequences, k):
    edges = []
    labels = list(sequences.keys())
    for i in range(len(labels)):
        s = labels[i]
        s_suffix = sequences[s][-k:]
        for j in range(len(labels)):
            if i == j:
                continue
            t = labels[j]
            t_prefix = sequences[t][:k]
            if s_suffix == t_prefix:
                edges.append((s, t))
    return edges

def save_adjacency_list(edges, output_file):
    with open(output_file, 'w') as file:
        for u, v in edges:
            file.write(f"{u} {v}\n")

file_path = 'rosalind_grph.txt'
output_file = 'output.txt'
sequences = parse_fasta(file_path)
edges = find_overlap_edges(sequences, 3)
save_adjacency_list(edges, output_file)
