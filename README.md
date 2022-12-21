# Mirko Kalezic - BGI Serbia Test
## Introduction

Task was to obtain the gene sequence from FASTA file. Provided Fasta file is contained of two types of lines where the first line is the name of the read and the second line is the nucleotide sequence.

## Getting started

The project was done in Python 3.9 and Windows 11 OS. 
With the following line is for cloning the repo on local machine:
```sh
git clone https://github.com/mlmirko/GeneExtraction.git
```

Change the repo:
```sh
cd GeneExtraction
```

##### 1. Retreiving the gene
This script retrieves gene sequence from readings: 
```sh
python extract_gene.py --input_file "PATH TO FASTA FILE"
```

For additional information type following command:

```sh
python extract_gene.py --h
```

The result will be saved in the same directory under name result.txt


##### 2. Validate gene
This script validate the gene sequence: 
```sh
python validate_gene.py --input_file "PATH TO TXT FILE"
```

For additional information type following command:

```sh
python validate_gene.py --h
```

The result will be shown in command window.
