def HammingDistance(string1, string2):
    result = 0
    for i in range(0, len(string1)):
        if(string1[i] != string2[i]):
            result += 1
    return result

def FastaReaderStringsOnly(strFileName):
    resultList = []
    resultString = ''
    with open(strFileName) as f:
        for line in f:
            if ('>' in line):
                if (resultString != ''):
                    resultList.append(resultString)
                    resultString = ''
            else:
                resultString = resultString + line.strip()
        if (resultString != ''):
            resultList.append(resultString)
    return resultList

def ReverseComplement (strDNA):
    result = ""
    for i in range(len(strDNA)-1, -1, -1):
        if (strDNA[i] == "A"):
            result += "T"
        elif (strDNA[i] == "T"):
            result += "A"
        elif (strDNA[i] == "C"):
            result += "G"
        else:

            result += "C" 
    return result

strings = list(FastaReaderStringsOnly("rosalind_corr.txt"))
stringsReverseComplement = list(map(ReverseComplement, strings))
stringsReverseComplement.extend(strings)

result = []
for oldRead in strings:
    if stringsReverseComplement.count(oldRead) == 1:
        for newRead in stringsReverseComplement:
            if(HammingDistance(oldRead, newRead) == 1):
                if(stringsReverseComplement.count(newRead) > 1):
                    result.append(oldRead + '->' + newRead)

result = list(set(result))
for string in result:
     print(string)





