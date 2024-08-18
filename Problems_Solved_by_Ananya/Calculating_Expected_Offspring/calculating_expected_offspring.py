def expected_dominant_offspring(couples):
    AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa = couples
    
    total_dominant_offspring = (
        2 * AA_AA * 1 +                
        2 * AA_Aa * 1 +                
        2 * AA_aa * 1 +                
        2 * Aa_Aa * (3/4) +            
        2 * Aa_aa * (1/2) +            
        2 * aa_aa * 0                  
    )
    
    return total_dominant_offspring

with open('rosalind_iev.txt', 'r') as file:
    couples = list(map(int, file.readline().strip().split()))

result = expected_dominant_offspring(couples)
print(f"{result:.1f}")
