#!/usr/bin/env python
import sys
import re
import math
from dom_parse import gid_pfam 
pfam2go=dict()
def pfam2_go(fh1,fh2,eval=math.exp(-5)):
    fh1=open(fh1)
    gid_pfam2=gid_pfam(fh2,eval)#gid_pfam from hmmscan for pfam domains-output files
    for line in fh1:
        if re.search('^Pfam',line)!=None:
            line=line.rstrip('\n').strip()
            parse_line=line.split(':')[1].split(' ')
            pfam=parse_line[0]
#        print(pfam)
            parse_line=':'.join(line.split(':')[2:])
            go=parse_line
#        print(go)
            if pfam2go.get(pfam,0)==0:#if pfam id doesn't exist then create a new one
                pfam2go[pfam]=[go]
#            print(pfam2go)
            else:#if the pfam id already exist as a key then append GO Terms to previous list
                pfam2go[pfam].append(go)
    fh1.close()
    gid_go=dict()
    for ids in gid_pfam2.keys():#####we are probing with input file generated gid_PFAM
        for pfam in gid_pfam2[ids]:
            if gid_go.get(ids,0)==0:
                gid_go[ids]=[pfam2go.get(pfam,'none')]#only if the pfam key exist
            else:
                gid_go[ids].append(pfam2go.get(pfam,'none'))

    return(gid_go,gid_pfam2)



#print(pfam2go)            

