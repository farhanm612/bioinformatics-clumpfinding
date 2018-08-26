#def immediate_neighbors(pattern = "ads"):
#    neighborhood = []
#    neighborhood.append(pattern)
#    for i in range(0,len(pattern)):
#        nucleotides = ['A', 'C', 'G', 'T']
#        nucleotides.remove(pattern[i])
#        for j in nucleotides:
#            pattern_temp = pattern.replace(pattern[i],j)
#            neighborhood.append(pattern_temp)
#    return neighborhood
import numpy as np
def pattern_to_number(pattern):
    symbolToNumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3};
    if not pattern:
        return 0
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return (symbolToNumber.get(symbol)) + (4*pattern_to_number(prefix))

def number_to_pattern(index, k):
    numberToSymbol = {0:'A',1:'C',2:'G',3:'T'}
    if k == 1:
        return numberToSymbol.get(index)
    #if k > index:
    #    return ""
    prefixIndex = index/4
    r = index % 4
    symbol = numberToSymbol.get(r)
    return symbol + number_to_pattern(prefixIndex,k-1)


def neighbors(pattern, d):
    chars = ['A','C','G','T']
    assert(d <= len(pattern))

    if d == 0:
        return [pattern]

    r2 = neighbors(pattern[1:], d-1)
    r = [c + r3 for r3 in r2 for c in chars if c != pattern[0]]
    if (d < len(pattern)):
        r2 = neighbors(pattern[1:], d)
        r += [pattern[0] + r3 for r3 in r2]
    return r


def computing_freq_mismatch(text,k,d):
    FrequencyArray = range(0, 4 ** k)
    for i in range(0, 4 ** k):
        FrequencyArray[i] = 0
    for i in range(0, len(text) - k + 1):
        Pattern = text[i:i + k]
        Neighborhood = neighbors(Pattern, d)
        for ApproximatePattern in Neighborhood:
            j = pattern_to_number(ApproximatePattern)
            FrequencyArray[j] = FrequencyArray[j] + 1
    return FrequencyArray

if __name__ == "__main__":
    print computing_freq_mismatch("AAGTCAACGGAAATTA", 4,2)
    #print number_to_pattern(13,4)