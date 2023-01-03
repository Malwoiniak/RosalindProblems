def count_nuc_freq(seq):
    tmpFreqDict = {'A':0, 'C':0, 'G':0, 'T':0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    # return dict(collections.Counter(seq))

DNAString = 'GAACCTGATCTGTTGCCTCCCCGGCCATGATCTCCCGTTCACTAGAATCACTGTATCAAGTTAGGAACCCCACCGTGGGCACGGGTAGAAGTTCGCGGTGTCAGTAAGGCGGATCCTAGCCCCGCCGAACCGGAATATAGAGTAAGCACGAAAAAAAAGGACTCTTATTGTAATGATGCCGCCTAACTGTTACATTAACGTCCGCCGCATTTATGGGATGGTTAGGGTTAAAAGCCACTTGAGTTGGGGTGATCCGTTGTGACAATCAGTCTGAGACCTCGGACTAGCGTCAAAGTCGTTTCGGCCTGACGCTACGACACCGTTACTGAACGGCGTAGTATAATTTTCCTGAATATCCCGTGGAGGCTTGGGACCTCGGGCACCATGGGAGTTCGAATTATGACGCGTTTTAACATTTAACATACCGCGCGGCATAGGGGCGACCATAAGCCTGGCCGTTGAAAAGGGTGAAAGACTCCGGGGACAGACGCTCAAGCGTTCAAGTACGTTTATAGTGACTAATGAGTACTTAGCGCTCAAAATGCTGCGCACCAGTTTGCCCCGAGCATGAGTTTCCTTGGTGAATTTCCGCGCCCGCCGACGCTGGATGCATTATCTCCTCGTAGAAGAAATCACAATCCAGCGTCAGGTTCCTTTAAGGCACAATGCCATTGAGTGGGAAGAATATGTGTAGCCAGCATACGATCCACTGCTGTTCCCTAGGTAGAATGTCCGGACATTAGTAACTGCCACTCCGGGGACAGTGATTAGGTCATAATTCCGTTTCCTGTCGACAACGGAAATCTGCCAAGTGTCCCGAGCGGGTATCGTCGATGTGACTTCTGTTTGTGCTAAGGAGCCATACGGGGGGGTCTTTATCGATACAACGAGTCGCAAAACCACACGCAAATAAGTGGCGTTAAGGTGCTCGAACCCTTTATCATTC'

result = count_nuc_freq(DNAString)
print(' '.join([str(val) for key,val in result.items()]))