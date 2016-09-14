#!/usr/bin/env python
import re
import sys
def gid_pfam(fh_1):
    fh=open(fh_1)
    gid_pfam=dict()
    for line in fh:
        line=line.rstrip('\n').strip()
        if re.search('(PF\d+)\.\d+',line)!=None:
            pfam_gid=re.search('(PF\d+)\.\d+\s+(\d+)\s*(\S+)',line).groups()
            pfam_id=pfam_gid[0]
        #print(pfam_id)
            gid=pfam_gid[2]
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
