#!/bin/bash
#$ -q sam
#$ -pe openmp 16


sample_dir=$1
sample_name=$2

repo_path="/share/crsp/lab/seyedam/sorenar/"
data_path=${repo_path}'data/'${sample_dir}
result_path=${repo_path}'results/'${sample_dir}
genome_ref=${repo_path}'ref/GRCh38_SIRV_ERCC.fa'


minimap2 -ax splice:hq -t 16 --cs -N 0 -uf ${genome_ref} ${data_path}${sample_name}.fastq > ${result_path}${sample_name}_CS.sam


