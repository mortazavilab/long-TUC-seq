#!/bin/bash
#$ -q sam
#$ -pe one-node-mpi 1
#$ -m ea
#$ -ckpt restart


ample_dir=$1
sample_name=$2

repo_path="/share/crsp/lab/seyedam/sorenar/"
data_path=${repo_path}'data/'${sample_dir}
result_path=${repo_path}'results/'${sample_dir}

python substitution_annotator.py -i ${result_path}${sample_name}_cs.sam -o ${result_path}${sample_name}

isamtools view -bh ${result_path}${sample_name}_6.sam | samtools sort > ${result_path}${sample_name}_6_sorted.bam
samtools index ${result_path}${sample_name}_6_sorted.bam
bamCoverage -b ${result_path}${sample_name}_6_sorted.bam -o ${result_path}${sample_name}_6.bw

samtools view -bh ${result_path}${sample_name}_20.sam | samtools sort > ${result_path}${sample_name}_20_sorted.bam
samtools index ${result_path}${sample_name}_20_sorted.bam
bamCoverage -b ${result_path}${sample_name}_20_sorted.bam -o ${result_path}${sample_name}_20.bw

samtools view -bh ${result_path}${sample_name}_30.sam | samtools sort > ${result_path}${sample_name}_30_sorted.bam
samtools index ${result_path}${sample_name}_30_sorted.bam
bamCoverage -b ${result_path}${sample_name}_30_sorted.bam -o ${result_path}${sample_name}_30.bw

samtools view -bh ${result_path}${sample_name}_0.sam | samtools sort > ${result_path}${sample_name}_0_sorted.bam
samtools index ${result_path}${sample_name}_0_sorted.bam
bamCoverage -b ${result_path}${sample_name}_0_sorted.bam -o ${result_path}${sample_name}_0.bw




