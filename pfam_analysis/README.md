Please the run the scripts in the order provided----, Also make sure clean your working directory of files/directory with atleast 'Name conflicts'
1)download.sh:


./download.sh <url_of_HMMER_binaries>

OUTPUT:

Creates a ./HMMER/ directory and keeps all binaries(for eg. hmmpress and hmmscan ) into it.
Unfortunately, the above wrapper will not work on Mac since it uses 'wget command'.

2)pfamdb.sh

./pfamdb.sh

OUTPUT:

1)Downloads Pfam-A dbase and puts everything into ./Pfam directory and 2)creates an index of .hmm file in ./Pfam/ directory along with original .hmm file

pfamFinder.sh

./pfamFinder.sh

OUTPUT:

Scans for Pfam-A domains in the query file and provides 2 outputs (output1.txt and output3.txt) of different formatting styles.


