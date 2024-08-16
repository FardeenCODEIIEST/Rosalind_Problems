import itertools

def generate_permutations(n):
    numbers = list(range(1, n + 1))
    permutations = list(itertools.permutations(numbers))
    return permutations

def read_integer_from_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
    return n

def write_permutations_to_file(filename, permutations):
    with open(filename, 'w') as file:
        file.write(f"{len(permutations)}\n")
        for perm in permutations:
            file.write(" ".join(map(str, perm)) + "\n")

def main():
    input_filename = 'rosalind_perm.txt'  
    output_filename = 'permutations_output.txt'  
    
    n = read_integer_from_file(input_filename)
    
    permutations = generate_permutations(n)
    
    write_permutations_to_file(output_filename, permutations)

if __name__ == "__main__":
    main()
