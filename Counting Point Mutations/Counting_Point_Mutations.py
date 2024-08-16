def hamming_distance(s, t):
    if len(s) != len(t):
        raise ValueError("Strings must be of equal length")

    distance = sum(1 for x, y in zip(s, t) if x != y)
    return distance

def read_dna_strings_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()       
        s = lines[0].strip()
        t = lines[1].strip()
    return s, t

filename = 'rosalind_hamm.txt'  
s, t = read_dna_strings_from_file(filename)

print(hamming_distance(s, t))
