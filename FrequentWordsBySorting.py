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


def computing_freq(text,k):
    freqArray = [0]*(4**k)
    for i in range(0,len(text)-k+1):
        pattern = text[i:i+k]
        j = pattern_to_number(pattern)
        freqArray[j] = freqArray[j]+1
    return freqArray

def frequent_words_by_sorting(text,k):
    #print "called"
    frequentPatterns = []
    index = [0] * (len(text) - k + 1)
    count = [0] * (len(text) - k + 1)
    for i in range(0,len(text)-k+1):
        pattern = text[i:i+k]
        index[i] = pattern_to_number(pattern)
        count[i] = 1
    sortedIndex = sorted(index)
    for i in range(1,len(text) - k + 1):
        if sortedIndex[i] == sortedIndex[i-1]:
            count[i] = count[i-1]+1
    maxCount = max(count)
    for i in range(0,len(text) - k + 1):
        if count[i] == maxCount:
            pattern = number_to_pattern(sortedIndex[i],k)[::-1]
            frequentPatterns.append(pattern)
    return frequentPatterns
