## Description of the scripts and their input and outputs


  
### alignment_with_CS.sh
This is the script to run minimap 2 alignment with the CS tag option.

**Input:** 
  1. The relative path from "data\" directory to the sample
  1. The sample name
  
**Output:**
  1. The aligned sam file including CS tags.
 

### alignment_with_MD.sh
This is the script to run minimap 2 alignment with the MD tag option.

**Input:** 
  1. The relative path from "data\" directory to the sample
  1. The sample name
  
**Output:**
  1. The aligned sam file including MD tags.
 
 
 ### substitution_annotator.py	
This is a python script to  count all the substitution events in each read and to report it as a text file.

**Input:**
  1. The absolute path to the aligned samfile containing the CS tag.
  1. The prefix for the output files
  
**Output:**
  1. A "_SNP.txt" file containing the tally of all possible substitutions for each read.
  
   
### substitution_analyzer.sh
This is the script to tally the number of substitutions in each read and to annotatote  each read with that. In addition this script will divide the sample sam files to multiple samfiles each containing the reads with different thresholds of T to C substitutions.

**Input:**
  1. The relative path from "data\" directory to the sample
  1. The sample name
  
**Output:**
  1. A "_SNP.txt" file containing the tally of all possible substitutions for each read.
  1. 4 sam files each containing a sub-category of reads based on the number of T to C mutations.
  1. bam files, sorted bamfiles and .bw files corresponding to the sub-sam files that can be used in genome browser for further visualiztion.
 

### talon.sh
This is the script to annotate all the aligned and cleaned reads against the appropriate annotation file. It will create a common database for all the runs in the same study.

**Input:**
  1. The relative path from "data\" directory to the sample
  1. The config file (a complete path to the config file containing the names and info on the samples included in this study.)
  1. The. study name used for creating a common database
  
**Output:**
  1. A database containingall the read annotations from different samples in the study.
  1. A annotation file with a complete list of all the reads and their annotations.
  
### transcriptClean.sh
This is the script to transcriptClean on the aligned files with will correct for any microindels interrupting the splice junctions:

**Input:**
  1. The relative path from "data\" directory to the sample
  1. The sample name
  
**Output:**
  1. The cleaned sam file with the suffix of _clean.
  
  
  
  
