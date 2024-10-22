#!/usr/bin/python
mydna_seq="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

fragment1=mydna_seq.find("GAATTC")+1
fragment2= len(mydna_seq) - fragment1
print("The First fraggment length is",fragment1, "while second fragment is ",fragment2)
