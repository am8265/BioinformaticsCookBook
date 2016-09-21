#!/usr/bin/env bash
hmmscan_path=$(find ./ -name hmmscan)
echo "PATH TO hmmscan:" $hmmscan_path
tigrfam_path=$(find ./ -name TIGRFAM)/TIGRFAM.HMM
echo "PATH to hmm indexed files:" $tigrfam_path
input_path=$1
echo "PATH OF THE DEFAULT INPUT FILE:" $input_path
echo "Now Scanning for TIGRFAM domains in the query file..........."
$hmmscan_path --domtblout output_dom_tigrfam.txt $tigrfam_path $input_path
$hmmscan_path --acc -o output_acc_tigrfam.txt $tigrfam_path $input_path