def read_input(filename):
    with open(filename, 'r') as file:
        n, k = map(int, file.readline().strip().split())
    return n, k

def calculate_rabbit_pairs(n, k):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    rabbit_pairs = [0] * (n + 1)
    
    rabbit_pairs[1] = 1
    rabbit_pairs[2] = 1
    
    for i in range(3, n + 1):
        rabbit_pairs[i] = rabbit_pairs[i - 1] + k * rabbit_pairs[i - 2]
    
    return rabbit_pairs[n]

def main():
    input_filename = 'rosalind_fib.txt'  
    
    n, k = read_input(input_filename)
    
    result = calculate_rabbit_pairs(n, k)
    
    print(result)

if __name__ == "__main__":
    main()
