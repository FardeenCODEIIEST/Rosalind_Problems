def parse_set(input_str):
    return set(map(int, input_str.strip('{}').split(', ')))

def compute_set_operations(n, A, B):
    U = set(range(1, n + 1))
    
    union = A.union(B)
    intersection = A.intersection(B)
    difference_A_B = A.difference(B)
    difference_B_A = B.difference(A)
    complement_A = U.difference(A)
    complement_B = U.difference(B)
    
    return (union, intersection, difference_A_B, difference_B_A, complement_A, complement_B)

def format_set(s):
    return '{' + ', '.join(map(str, sorted(s))) + '}'

file_path = 'rosalind_seto.txt'
with open(file_path, 'r') as file:
    n = int(file.readline().strip())
    A = parse_set(file.readline().strip())
    B = parse_set(file.readline().strip())

union, intersection, difference_A_B, difference_B_A, complement_A, complement_B = compute_set_operations(n, A, B)

with open('output.txt', 'w') as file:
    file.write(f"{format_set(union)}\n")
    file.write(f"{format_set(intersection)}\n")
    file.write(f"{format_set(difference_A_B)}\n")
    file.write(f"{format_set(difference_B_A)}\n")
    file.write(f"{format_set(complement_A)}\n")
    file.write(f"{format_set(complement_B)}\n")
