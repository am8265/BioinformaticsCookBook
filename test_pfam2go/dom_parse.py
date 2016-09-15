#!/usr/bin/env python
import re
import sys
import math
def gid_pfam(fh_1,eval=math.exp(-5)):
    fh=open(fh_1)
    gid_pfam=dict()
    for line in fh:
        line=line.rstrip('\n').strip()
        if re.search('(PF\d+)\.\d+',line)!=None:
            pfam_gid=re.search('(PF\d+)\.\d+\s+(\d+)\s*(\S+)\s+\S+\s+\S+\s+(\S+)',line).groups()
            pfam_id=pfam_gid[0]
        #print(pfam_id)
            gid=pfam_gid[2]
            evalue=float(pfam_gid[3])
            if evalue<=eval:
        #print(gid)
                if gid_pfam.get(gid,'0')=='0':
                    gid_pfam[gid]=[pfam_id]
                else:
                    gid_pfam[gid].append(pfam_id)
    
#print(gid_pfam)
    for ids in gid_pfam.keys():
        gid_pfam[ids]=list(set(gid_pfam[ids]))
    return gid_pfam
    fh.close()
print(gid_pfam(sys.argv[1]))
