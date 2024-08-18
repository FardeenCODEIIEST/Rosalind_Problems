def solve(rna):
    return helper(rna, 0, len(rna) - 1, {})


def helper(rna, lo, hi, dp):
    
    mapping = {
    "A" : "U",
    "U" : "A",
    "G" : "C",
    "C" : "G"
    }
    characters = hi - lo + 1
    
    if characters % 2 == 1:
        return 0

    if lo >= hi or lo >= len(rna) or hi < 0:
        return 1

    if (lo, hi) in dp:
        return dp[(lo, hi)]
    else:
        curr = rna[lo]
        target = mapping[curr]
        acc = 0
        for i in range(lo + 1, hi + 1, 2):
            if rna[i] == target:
                left = helper(rna, lo + 1, i - 1, dp)
                right = helper(rna, i + 1, hi, dp)
                acc += (left * right) % 1000000
        dp[(lo, hi)] = acc
        return acc


rna = "UACUCGAUACGGCUCGCGAUACGGUACCGCUAGGGUACGCUAGCUUGAUGCGCGAUAUUACCUAAGCCUAGAUGUAGCUACGGCAUUGUUAGCAGCUGCCCGAUAUUAGAAUCUAUUAAGGCCAUACAUGCUAAUGAUGCAAUUCCAAUUACGUGCGGCCGAGAUACGGCUCUUAACGUUUACUUGCAUAAUAGAUGCGUACGAUAUACGUUACGUAGAUGCCUAUAUGAUCAUACGCGCAGUGACGUUAAAUAUAUUCGGUACAUUACACCGCGGCUAAGCAAUUAUUACG"

print(solve(rna.strip()) % 1000000)
