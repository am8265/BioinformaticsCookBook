#!/usr/bin/env bash

##This single line will create Index files from PfamA dbase########
#####The Pfam press file would be loacted in the same directory where Pfam-A.hmm reside######################
/data/home/amalakar/bin/hmmer-3.1b2/binaries/hmmpress /lustre/scratch/amalakar/ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam30.0/Pfam-A.hmm 
#####USing HMMSCAN we get a parsable list of "DOMAINS in the Query sequence"after comapring with Pfam-A database############
#######The file is output1.txt################
/data/home/amalakar/bin/hmmer-3.1b2/binaries/hmmscan --domtblout output1.txt /lustre/scratch/amalakar/ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam30.0/Pfam-A.hmm /data/home/amalakar/sep01/first5seq.fa
######Use accessions rather than names when generating the output and store it in output3.txt#######
/data/home/amalakar/bin/hmmer-3.1b2/binaries/hmmscan --acc -o output3.txt /lustre/scratch/amalakar/ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam30.0/Pfam-A.hmm /data/home/amalakar/sep01/first5seq.fa 