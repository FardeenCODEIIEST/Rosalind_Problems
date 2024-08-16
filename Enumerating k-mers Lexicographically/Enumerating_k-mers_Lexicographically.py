from itertools import product

def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    alphabet = lines[0].strip().split()
    n = int(lines[1].strip())
    
    return alphabet, n

def generate_lexicographic_strings(alphabet, n):
    return [''.join(p) for p in product(alphabet, repeat=n)]

def write_output(filename, strings):
    with open(filename, 'w') as file:
        for s in strings:
            file.write(s + '\n')

def main():
    input_filename = 'rosalind_lexf.txt'  
    output_filename = 'rosalind_lexf_output.txt'  
    
    alphabet, n = read_input(input_filename)
    
    strings = generate_lexicographic_strings(alphabet, n)
    
    write_output(output_filename, strings)

if __name__ == "__main__":
    main()
