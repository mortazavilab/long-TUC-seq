#!/bin/bash
#$ -q sam
#$ -pe openmp 16


sample_dir=$1
sample_name=$2

repo_path="/share/crsp/lab/seyedam/sorenar/"
result_path=${repo_path}'results/'${sample_dir}
transcriptClean_path=${repo_path}'programs/TranscriptClean/'
genome_ref=${repo_path}'ref/GRCh38_SIRV_ERCC.fa'
splice_file=${repo_path}'ref/gencode_v29_SJs.tsv'
variant_file=${repo_path}'ref/NA12878.vcf'



python ${transcriptClean_path}TranscriptClean.py -t 16 --sam ${result_path}${sample_name}_MD.sam --genome ${genome_ref} --spliceJns ${splice_file} --variants ${variant_file} -m False --outprefix ${result_path}${sample_name} --primaryOnly



