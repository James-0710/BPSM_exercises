#!/usr/bin/python
#Q1
mydna_seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A_seq=mydna_seq.count("A")
T_seq=mydna_seq.count("T")
length=len(mydna_seq)
totalAT=int(A_seq)+int(T_seq)
at_content=totalAT/len(mydna_seq)
print("A+T content is",str(int(100*at_content)),"percent")
