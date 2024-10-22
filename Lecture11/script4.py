#!/usr/bin/python
mydna_seq="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"


firstexon=mydna_seq[0:63]
secondexon=mydna_seq[90:]
joinedexon=str(firstexon)+str(secondexon)
print("### Exon joined ###\n" + joinedexon)


length=len(joinedexon)
percent=length/len(mydna_seq) *100
print("The percentage of the DNA sequence is coding is", percent)

intron=mydna_seq[63:90]
lowercaseintron=intron.lower()

originalseq=str(firstexon)+str(lowercaseintron)+str(secondexon)

print("The concatenate sequence is", originalseq) 
