
############################
OUTSIDE=`pwd`
source ${OUTSIDE}/MCP.conf
source ${OUTSIDE}/MCP.module
source ${OUTSIDE}/MCP.tools

#echo "GENOME_SIZE=="$GENOME_SIZE
cd $LIB/
FDR=D04_SNBC_READ

rm -rf $FDR
mkdir $FDR
cd $FDR

FRR=R00_F2304/
rm -rf $FRR
mkdir $FRR
cd $FRR



for F in ../../D02_SNBC_BAM/${LIB}*.bam
do
file=$(ls $F|rev|cut -d"/" -f1|rev)

	samtools view -h -F 2304 $F|samtools view -hbS - > $file.F2304.bam &
	jobmax $PC_CPU_NUM
done
wait 
pwd
echo "F2304.bam number = " $(ls *.F2304.bam|wc -l )
cd $OUTSIDE


