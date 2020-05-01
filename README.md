# long-TUC-seq

## Pipeline description and installation
This repository consists of scripts that were used in our long-TUC-seq pipeline for analysis of long-TUC-seq samples and for generating the graphs used in our paper.

In order to run the pipeline, you need to first place your pre-processed long-TUC-seq fastq files in "data/" directory and ensure that your genome reference and annotation as well as the splice junction reference and VCF file containing the known SNPs for your samples are deposited in the "ref/" directory.

Then, you will need to obtain TranscriptClean code from [mortazavilab](https://github.com/mortazavilab/TranscriptClean) and place it in the "programs/" directory.

Also you need to ensure that you have. the following packages installed:
* [minimap2](https://github.com/lh3/minimap2)
* [TALON](https://github.com/mortazavilab/TALON)

Then correct the path in each script file to. reflect where you have cloned this repository.
Finally run the scripts in the following oreer:

1. Run "alignment_MD.sh" on each fastq file
1. Once you get your aligned bam files, run "transcriptClean.sh" on them.
1. finally after you got all the transcript cleaned sam files, make a config.csv file in the "scripts/" directory containing all the samples for the study according to the sample congig provided. and then run "talon.sh" with that config file.

In parralel to the steps above you may run the  following steps to get the substitution annotations for each sample:

1. Run "alignment_CS.sh" on each fastq file
1. Run "substitution_annotator.sh" on each file.


