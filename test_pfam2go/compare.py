#!/usr/bin/env python


######run this script like : ./compare.py <pfam2go_annotation_file>  <output1_hmmscan output.txt> <suitable_subset_annotation_file> <compare.ouput.txt>######
#######Please note about the dependencies of the above script###########

import os
import sys
import re
import parse_pfam2go
import math
#try:
#    eval=float(sys.argv[5])

result_ppfam=parse_pfam2go.pfam2_go(sys.argv[1],sys.argv[2],eval=math.exp(-5))#return type is null but we will use some of the objects defined within the module
print(result_ppfam)
fh3=open(sys.argv[3])
fh4=open(sys.argv[4],'w')
fh4.write('peptide_id_phytozome'+'\t'+'pfam_id_phytozome'+'\t'+'go_id_phytozome'+'\t'+'pfam_id_wflow'+'\t'+'go_id_wflw'+'\n')
for line in fh3:
    line=line.rstrip('\n').strip()
    #parse=re.search('(E\w+\.\w+\.\d*\.p)\s+(PF\d)\s+.+(GO:\d+)\s+',line).groups()
    parse2=line.split('\t')
    #print(parse2)
    peptide_id=parse2[3]
    print(peptide_id)
    pfam_id=parse2[4]
    print(pfam_id)
    go_id=parse2[9]
    print(go_id)
    go_id_wflw=str(result_ppfam[0].get(peptide_id,'--'))#using peptide_id from phytozome file
    print(go_id_wflw)
    pfam_id_wflw=str(result_ppfam[1].get(peptide_id,'--'))
    print(pfam_id_wflw)
    fh4.write(peptide_id+'\t'+pfam_id+'\t'+go_id+'\t'+pfam_id_wflw+'\t'+go_id_wflw+'\n')
fh4.close()
fh3.close()
