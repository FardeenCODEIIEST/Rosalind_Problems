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

def longest_common_substring(dna_strings):
    def is_common_substring(sub, strings):
        return all(sub in string for string in strings)
    
    if not dna_strings:
        return ''
    
    first_string = dna_strings[0]
    n = len(first_string)
    longest_substr = ""
    
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            substr = first_string[start:start + length]
            if is_common_substring(substr, dna_strings):
                if length > len(longest_substr):
                    longest_substr = substr
    
    return longest_substr

def main():
    input_filename = 'rosalind_lcsm.txt'  
    dna_strings = read_fasta(input_filename)
    result = longest_common_substring(dna_strings)
    print(result)

if __name__ == "__main__":
    main()
