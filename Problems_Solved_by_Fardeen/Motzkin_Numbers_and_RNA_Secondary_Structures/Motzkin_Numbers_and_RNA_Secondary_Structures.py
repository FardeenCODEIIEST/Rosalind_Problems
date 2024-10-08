f = open('rosalind_motz.txt', 'r')
next(f)
mat = f.read().replace('\n', '')
s = {}

def motz(mat):
    lib = {'A':'U','U':'A', 'C':'G', 'G':'C'}

    if (len(mat) <= 1):
        return 1
    
    elif (mat in s):
        return s[mat]

    else: 
        s[mat] = motz(mat[1:])
        
        for i in range(1, len(mat)):
            if (mat[i] == lib[mat[0]]):
                s[mat] = s[mat] + motz(mat[1:i]) * motz(mat[i+1:])
    
    return s[mat]
        
print(motz(mat) % 1000000)
