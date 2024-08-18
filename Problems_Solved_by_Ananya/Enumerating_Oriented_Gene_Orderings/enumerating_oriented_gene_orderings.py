import itertools

def generate_signed_permutations(n, filename):
    base_permutations = itertools.permutations(range(1, n + 1))
    
    signed_permutations = []
    
    for perm in base_permutations:
        sign_combinations = itertools.product([-1, 1], repeat=n)
        for signs in sign_combinations:
            signed_perm = [perm[i] * signs[i] for i in range(n)]
            signed_permutations.append(signed_perm)
    
    with open(filename, 'w') as file:
        file.write(f"{len(signed_permutations)}\n")
        for sp in signed_permutations:
            file.write(" ".join(map(str, sp)) + "\n")

n = int(input().strip())
filename = "signed_permutations.txt"
generate_signed_permutations(n, filename)
