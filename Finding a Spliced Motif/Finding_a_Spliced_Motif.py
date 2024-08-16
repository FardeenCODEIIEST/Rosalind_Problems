def read_fasta(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    strings = []
    current_string = []
    
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            if current_string:
                strings.append(''.join(current_string))
                current_string = []
        else:
            current_string.append(line)
    
    if current_string:
        strings.append(''.join(current_string))
    
    return strings

def find_subsequence_indices(s, t):
    indices = []
    s_len = len(s)
    t_len = len(t)
    j = 0
    
    for i in range(s_len):
        if j < t_len and s[i] == t[j]:
            indices.append(i + 1) 
            j += 1
        if j == t_len:
            break
    
    return indices

def main():
    import sys
    input_filename = 'rosalind_sseq.txt'
    
    strings = read_fasta(input_filename)
    s = strings[0]
    t = strings[1]
    
    indices = find_subsequence_indices(s, t)
    
    print(' '.join(map(str, indices)))

if __name__ == "__main__":
    main()
