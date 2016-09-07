#!/usr/bin/env bash
wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam30.0/Pfam-A.hmm.gz
pathPFAM=$(pwd)/Pfam/
mkdir $pathPFAM
path=$(find ./ -name "Pfam-A.hmm.gz")
gzip -d $path
mv *.hmm $pathPFAM
echo "PATH TO Pfam DATABASE IS:"
echo $pathPFAM
echo "NOW PRESSING THE .hmm file......."
hmmpress=$(find $HMMER/ -name hmmpress)
$hmmpress $pathPFAM