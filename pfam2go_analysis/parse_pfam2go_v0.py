#!/usr/bin/env python
import sys
import re
from dom_parse import gid_pfam 
pfam2go=dict()
def pfam2_go(fh1,fh2):
    fh1=open(fh1)#pfam2GO file
    gid_pfam2=gid_pfam(fh2)#gid_pfam from hmmscan--output1.txt for pfam domains-output files
    for line in fh1:
        if re.search('^Pfam',line)!=None:
            line=line.rstrip('\n').strip()
            parse_line=line.split(':')[1].split(' ')
            pfam=parse_line[0]
            #print(pfam)
            parse_line=':'.join(line.split(':')[2:])
            go=parse_line
            
            #print(go
            if pfam2go.get(pfam,0)==0:#if pfam id doesn't exist then create a new one
                #pfam2go[pfam]=go
                 pfam2go[pfam]=[go]
            #print(pfam2go)
            else:#if the pfam id already exist as a key then append GO Terms to previous list
#pfam2go[pfam]=pfam2go[pfam]+','+go
                pfam2go[pfam].append(go)
    #print(pfam2go)
    fh1.close()
    gid_go=dict()
    #print(gid_pfam2)
    for ids,pfams in gid_pfam2.items():#####we are probing with input file generated gid_PFAM----->this came from hmmscan
#        print(pfams)
        gos=[]
        for pfam in pfams:#pfams would be a list of pfamids for a unique gene_id!
            #gos=[]
            #print(pfams)
            for pfam in pfams:
                #print(pfam)
                gos.extend(pfam2go.get(pfam,' '))
        gos=list(set(gos))#we remove all duplicates
#        print(gos)
            #print(str(ids)+':'+str(gos))
        gid_go[ids]=gos#for a single gid--->all go's in a list
        


    return(gid_go,gid_pfam2)

gid_go_pfam=pfam2_go(sys.argv[1],sys.argv[2])#sys.argv[1] should be the pfam2go file, sys.argv[2] is the output1.txt file from hmmscan 
gid_go=gid_go_pfam[0]
gid_pfam=gid_go_pfam[1]
fh=open('gid_go_pfam.txt','w')
fh.write('peptide_id'+'\t'+'GO'+'\t'+'Pfam_id'+'\n')
for ids in gid_pfam.keys():#####we are probing with input file generated gid_PFAM
    if ' ' in gid_go[ids]:
        if gid_go[ids].count(' ')!=len(gid_go[ids]):#if this ' ' and other valid gos  exist! 
            gid_go[ids].remove(' ')
            go=','.join(gid_go[ids])
#            print(go)
        else:#only ' ' exist
            go=' '.join(gid_go[ids])
    else:
        go=','.join(gid_go[ids])
    pfam=','.join(gid_pfam[ids])
    fh.write(ids+'\t'+go+'\t'+pfam+'\n')
fh.close()

#for pfam in gid_pfam[ids]:
#            if gid_go.get(ids,0)==0:
#                gid_go[ids]=[pfam2go.get(pfam,'none')]#only if the pfam key exist                                                                                                  
#            else:
#                gid_go[ids].append(pfam2go.get(pfam,'none'))



#print(pfam2go)            

