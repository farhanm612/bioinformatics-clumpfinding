import FrequentWordsBySorting as fwsort


def clump_finding(genome, k, t, l):
    frequentPatterns = ['']
    clump = [0] * (4**k)
    print len(genome) - l
    #for i in range(0,(4**k)-1):
    #    clump[i] = 0
    for i in range(0, len(genome)-l+1):
        text = genome[i:i + l]
        frequentArray = fwsort.computing_freq(text,k)
        for index in range(0,(4**k)):
            if frequentArray[index] >= t:
                clump[index] = 1
        print i
    for i in range(0, (4 ** k)):
        if clump[i] == 1:
            pattern = fwsort.number_to_pattern(i,k)[::-1]
            frequentPatterns.append(pattern)
    return frequentPatterns[1:]


if __name__ == "__main__":
    f = open('genome.txt')
    genome = f.read()
    print clump_finding(genome,11,18,566)
