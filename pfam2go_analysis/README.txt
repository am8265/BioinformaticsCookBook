Run the compare.py script like this:

./compare.py <pfam2go_annotation_file>  <output1_hmmscan_output.txt> <suitable_subset_annotation_file> <compare.out>

example of such run, please copy paste the line below for a test run (the input files are in the same folder)
./compare.py pfam2go output1.txt sub.annot.txt compare.out

Result:

a compare.out file would be generated comparing results from PHYTOZOME generated ANNOTATION FILE and OUR WORKFLOW generated annotation file

please note:

compare.py has dependencies 1)dom_parse.py 2)parse_pfam2go.py. The 2 scripts must be in the same directory of that of compare.py. Also provide 1)updated pfam2go annotation file 2)hmmscan output in the prescribed format as that of eg. output1.txt 3) suitable_subset_annotation_file-this would be a SUBSET of ANNOTATION FILE from phytozome website 