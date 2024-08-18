from scipy.stats import binom

def probability_at_least_n_organisms(k, N):
    num_organisms = 2**k
    p = 1/4
    prob_at_least_N = 1 - binom.cdf(N-1, num_organisms, p)
    return prob_at_least_N

with open('rosalind_lia.txt', 'r') as file:
    line = file.readline().strip()
    k, N = map(int, line.split())

result = probability_at_least_n_organisms(k, N)
print(f"{result:.3f}")
