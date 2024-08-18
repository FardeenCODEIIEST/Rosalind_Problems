import math


with open("rosalind_prob.txt","r") as f:
    lines=f.readlines()

def RandomString(strRandomString, stringArray):
    strRandomString = strRandomString.upper()
    cg = len(strRandomString.replace('A', '').replace('T', ''))
    at = len(strRandomString.replace('C', '').replace('G', ''))
    inputArray = stringArray.split()
    outputArray = []
    for i in range(0, len(inputArray)):
        prob = cg * math.log10(float(inputArray[i]) / 2) + at * math.log10((1 - float(inputArray[i])) / 2)
        outputArray.append(round(prob, 3))
    return outputArray


result = ' '.join(map(str, RandomString(lines[0].strip(), lines[1].strip())))

print(result)
