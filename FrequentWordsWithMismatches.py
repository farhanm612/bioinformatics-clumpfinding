from ComputingFrequenciesWithMismatches import neighbors
from FrequentWordsBySorting import pattern_to_number,number_to_pattern
import numpy as np
def frequent_words_withmismatches(text,k,d):
    frequentPatterns = []
    neighborhoods = []
    for i in range(0,len(text)-k+1):
        neighborhoods.append(neighbors(text[i:i+k],d))
    neighborhoods = neighborhoods[0]
    #neighborhoods = np.unique(neighborhoods[0])
    index = [0] * len(neighborhoods)
    count = [0] * len(neighborhoods)
    for i in range(0,len(neighborhoods)):
        pattern =  neighborhoods[i]
        index[i] = pattern_to_number(pattern)
        count[i] = 1
    sortedIndex = sorted(index)
    for i in range(0,len(neighborhoods)-1):
        if sortedIndex[i] == sortedIndex[i+1]:
            count[i+1] = count[i] + 1
    maxCount = max(count)
    for i in range(0,len(neighborhoods)):
        if count[i] == maxCount:
            frequentPatterns.append(number_to_pattern(sortedIndex[i],k))
    return frequentPatterns[0]



if __name__ == "__main__":
    print frequent_words_withmismatches("AAGTCAACGGAAATTA", 4, 2)