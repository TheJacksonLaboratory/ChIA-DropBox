F=$1 
file=$2

samtools sort -n $F -o $file.sN.bam
bamToBed -i $file.sN.bam|grep "/1" > $file.sN.bam.R1.bed; 
bamToBed -i $file.sN.bam|grep "/2" > $file.sN.bam.R2.bed;

