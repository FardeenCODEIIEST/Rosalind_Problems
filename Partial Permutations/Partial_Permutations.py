def partial_permutations(n, k, mod=1000000):
    result = 1
    for i in range(k):
        result = (result * (n - i)) % mod
    return result

def read_input(filename):
    with open(filename, 'r') as file:
        n, k = map(int, file.readline().strip().split())
    return n, k

def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(f"{result}\n")

def main():
    input_filename = 'rosalind_pper.txt'  
    output_filename = 'rosalind_pper_output.txt'

    n, k = read_input(input_filename)
    
    result = partial_permutations(n, k)
    
    write_output(output_filename, result)

if __name__ == "__main__":
    main()
