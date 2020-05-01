#!/bin/bash
#$ -q sam
#$ -pe openmp 16


sample_dir=$1
config_file=$2
study_name=$3

repo_path="/share/crsp/lab/seyedam/sorenar/"
result_path=${repo_path}'results/'${sample_dir}
genome_ref=${repo_path}'ref/GRCh38_SIRV_ERCC.fa'
annot_file=${repo_path}'ref/gencode_v29_SIRV_ERCC.gtf'


talon_initialize_database --f ${annot_file} --a GENCODE --g v29 --o ${result_path}${study_name}

talon --f ${config_file} --db ${result_path}${study_name}'.db' --build v29 --t 16 --o ${result_path}${study_name}


