#!/projects/capurd/chia_pet/chia_pet_tool_2/conda/bin/python
import os
from pyfaidx import Fasta
import numpy as np
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import argparse


def convert_bedpe_to_fastq(ref_file, bedpe_file, prefix, out_dir):
    """
    Convert BEDPE file to FASTQ file.
    """
    linker_seq = 'ACGCGATATCTTATCTGACT'
    
    # Initialize file names
    r1_file = '%s/%s_R1.fastq' % (out_dir, prefix)
    r2_file = '%s/%s_R2.fastq' % (out_dir, prefix)
    
    if os.path.isfile(r1_file):
        os.remove(r1_file)
    
    if os.path.isfile(r2_file):
        os.remove(r2_file)
    
    
    # Read reference genome
    ref = Fasta(ref_file)
    
    with open(bedpe_file, 'r') as f:
        i = 0
        for line in f:
            i += 1
            entry = line.strip().split()
            
            r1_chrom = entry[0] 
            a_start = int(entry[1])
            a_end = int(entry[2])
            
            r2_chrom = entry[3]
            b_start = int(entry[4])
            b_end = int(entry[5])
            
            a_mid = int(np.mean([a_start, a_end]))
            b_mid = int(np.mean([b_start, b_end]))
            
            r1_start = a_mid - 75
            r1_end = a_mid + 75
            
            r2_start = b_mid - 75
            r2_end = b_mid + 75
    
            try:
                r1_seq = ref[r1_chrom][r1_start : r1_end].seq
            except:
                continue
            
            try:
                r2_seq = ref[r2_chrom][r2_start : r2_end].seq
            except:
                continue
            
            if len(r1_seq) < 150 or len(r2_seq) < 150:
                continue
            
            # Add linker to R1 seq
            r1_seq += linker_seq
            
            # Reverse complement R2 seq
            r2_seq = str(Seq(r2_seq).reverse_complement())
            
            
            # Create read IDs
            r1_id = '%s:1:1-A:1:1:%s:%s 1:N:0:A' % (r1_chrom, i, i)
            r2_id = '%s:1:1-A:1:1:%s:%s 2:N:0:A' % (r1_chrom, i, i)
            
            # Create R1 SeqRecord
            r1 = SeqRecord(
                seq=r1_seq,
                id=r1_id, name='', description='',
                letter_annotations={'phred_quality':[40]*len(r1_seq)})
            
            # Create R2 SeqRecord
            r2 = SeqRecord(
                seq=r2_seq,
                id=r2_id, name='', description='',
                letter_annotations={'phred_quality':[40]*len(r2_seq)})
            
            
            with open(r1_file, 'a+') as r1_f:
                SeqIO.write(r1, r1_f, 'fastq')
                
            with open(r2_file, 'a+') as r2_f:
                SeqIO.write(r2, r2_f, 'fastq')


def parse_command_line_args():
	"""
	Parse command-line arguments.
	
	Returns:
		args (class 'argparse.Namespace'):
			An object containing the parsed command-line arguments.
			For every command-line option, the values are stored as follows:
			args.{option} 
	"""
	# Initiate the argument parser
	parser = argparse.ArgumentParser()
	required = parser.add_argument_group('required arguments')
	
	# Indicate the required arguments
	required.add_argument(
		'-r', '--ref', required=True,
		help=('The reference genome FASTA file.'))
	
	required.add_argument(
		'-b', '--bedpe', required=True,
		help=('The chrom-specific BEDPE file of pairwise ChIA-Drop contacts.'))
	
	required.add_argument(
		'-p', '--prefix', required=True,
		help=('The prefix for the output file name.'))
	
	required.add_argument(
		'-o', '--out_dir', required=True,
		help=('The output directory where to write the FASTQ files.'))
	
	# Parse the arguments from the command-line input
	args = parser.parse_args()
	
	return args


if __name__ == '__main__':
    
    #ref_file = 'dm3/dm3.fa'
    # chr2L chr2R chr3L chr3R chr4 chrX
    #bedpe_file = 'P2MC7N8HCE3K_mean-of-mean_FDR_0.1_pseudoGEM_10000_pass_allpairs.bedpe'
    #bedpe_file = 'P2CHIADROPREP2_FDR_0.1_pseudoGEM_10000_enrichTest_PASS_allpairs.bedpe'
    
    args = parse_command_line_args()
    convert_bedpe_to_fastq(args.ref, args.bedpe, args.prefix, args.out_dir)
    