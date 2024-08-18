def total_subsets(n):
    MOD = 1000000
    return pow(2, n, MOD)

file_path = 'rosalind_sset.txt'

with open(file_path, 'r') as file:
    n = int(file.read().strip())

result = total_subsets(n)

with open('output.txt', 'w') as file:
    file.write(f"{result}\n")
