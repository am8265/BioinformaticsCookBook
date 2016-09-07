#!/usr/bin/env python
#######This script uses a File composed of a LIST OF PROTEIN IDS and uses it parse sequences from protein.fa file!################
import os
import re
import sys
fh=open(sys.argv[1])
fh2=open('first5seq.fa','w')
fh3=open(sys.argv[2])
#for line in fh:
#    line=line.rtsrip('\n').strip()
seq={}    
for line2 in fh3:
    if line2.startswith('>'):
        head=line2.strip('\n').strip()
        seq[head]=''
    else:
        seq[head]+=line2
fh3.close()

for line in fh:                                                                
    line=line.rstrip('\n').strip()
    for k in seq.keys():
        if line in k:
            fh2.write(k+'\n'+seq[k])
        else:
            pass
fh2.close()
fh.close()
