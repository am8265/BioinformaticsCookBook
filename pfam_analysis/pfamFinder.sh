#!/usr/bin/env bash

##This single line will create Index files from PfamA dbase########
#####The Pfam press file would be loacted in the same directory where Pfam-A.hmm reside######################
#/data/home/amalakar/bin/hmmer-3.1b2/binaries/hmmpress /lustre/scratch/amalakar/ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam30.0/Pfam-A.hmm 
#####USing HMMSCAN we get a parsable list of "DOMAINS in the Query sequence"after comapring with Pfam-A database############
#######The file is output1.txt################
hmmscan_path=$(find ./ -name hmmscan)
echo "PATH TO hmmscan:" $hmmscan_path
hmm_path=$(find ./ -name Pfam)/Pfam-A.hmm
echo "PATH to hmm indexed files:" $hmm_path
input_path=$(find ./ -name 'first5seq.fa')
echo "PATH OF THE DEFAULT INPUT FILE:" $input_path
echo "Now Scanning for Pfam domains in the query file..........."
$hmmscan_path --domtblout output1.txt $hmm_path $input_path 
######Use accessions rather than names when generating the output and store it in output3.txt#######
#/data/home/amalakar/bin/hmmer-3.1b2/binaries/hmmscan --acc -o output3.txt /lustre/scratch/amalakar/ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam30.0/Pfam-A.hmm /data/home/amalakar/sep01/first5seq.fa 
$hmmscan_path --acc -o output3.txt $hmm_path $input_path