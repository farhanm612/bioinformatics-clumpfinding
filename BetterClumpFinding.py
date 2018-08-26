import FrequentWordsBySorting as fwsort
import numpy as np

def better_clump_finding(genome,k,t,l):
    #print len(genome)-l+1
    frequentPatterns = [0] * (4**k)
    clump = [0] * (4 ** k)
    for i in range(0,4**k):
        clump[i] = 0
    text = genome[0:l]
    frequencyArray = fwsort.computing_freq(text,k)
    for i in range(0, 4 ** k):
        if frequencyArray[i] >= t:
            clump[i] = 1
    for i in range(1,len(genome)-l+1):
        firstPattern = genome[i-1:i-1+k]
        index = fwsort.pattern_to_number(firstPattern)
        frequencyArray[index] = frequencyArray[index] - 1
        lastPattern = genome[i+l-k:i+l]
        index = fwsort.pattern_to_number(lastPattern)
        frequencyArray[index] = frequencyArray[index] + 1
        if frequencyArray[index] >= t:
            clump[index] = 1
    for i in range(0,4**k):
        if clump[i] == 1:
            pattern = fwsort.number_to_pattern(i,k)[::-1]
            frequentPatterns.append(pattern)
    frequentPatterns = np.unique(frequentPatterns)
    return frequentPatterns[1:]


if __name__ == "__main__":
    f = open('genome.txt')
    genome = f.read()
    print better_clump_finding(genome,11,18,566)
    #print fwsort.frequent_words_by_sorting(genome,3)