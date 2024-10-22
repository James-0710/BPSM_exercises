#!/usr/bin/python
mydna_seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

mydna_seq1 = mydna_seq.replace("A","t")
mydna_seq2 = mydna_seq1.replace("T","a")
mydna_seq3= mydna_seq2.replace("C", "g")
mydna_seq4= mydna_seq3.replace("G", "c")
finaldna_seq=mydna_seq4.upper()
print("The complement of this sequence is",finaldna_seq)
