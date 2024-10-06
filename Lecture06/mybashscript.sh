#!/bin/bash
cut -f 2 blastoutput2.out
cut -f 3,4 blastoutput2.out
awk 'BEGIN{FS="\t"}{if($5>20){print $5;}}' blastoutput2.out


