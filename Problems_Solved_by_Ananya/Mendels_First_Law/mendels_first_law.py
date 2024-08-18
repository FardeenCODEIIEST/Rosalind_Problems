def calculate_dominant_probability(k, m, n):
    total_population = k + m + n
    total_pairs = total_population * (total_population - 1) / 2
    
    kk_pairs = k * (k - 1) / 2
    km_pairs = k * m
    kn_pairs = k * n
    mm_pairs = m * (m - 1) / 2
    mn_pairs = m * n
    nn_pairs = n * (n - 1) / 2

    dominant_prob = (kk_pairs * 1 +
                     km_pairs * 1 +
                     kn_pairs * 1 +
                     mm_pairs * (3/4) +
                     mn_pairs * (1/2) +
                     nn_pairs * 0) / total_pairs

    return dominant_prob

with open('rosalind_iprb.txt', 'r') as file:
    k, m, n = map(int, file.readline().strip().split())

probability = calculate_dominant_probability(k, m, n)
print(f"{probability:.5f}")
