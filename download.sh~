#!/usr/bin/env bash

####given the download link , the command below would dwnload the required binaries in to 'HMMER directory'
wget -m http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2-linux-intel-x86_64.tar.gz --directory-prefix=HMMER/
path=$(find HMMER/ -name "*.tar.gz")
tar -xzf $path -C ./HMMER/
echo "PATH TO HAMMER IS:"
echo $(pwd)/HMMER