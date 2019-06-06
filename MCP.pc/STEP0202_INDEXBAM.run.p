############################
OUTSIDE=`pwd`
source ${OUTSIDE}/MCP.conf
source ${OUTSIDE}/MCP.module
source ${OUTSIDE}/MCP.tools


FDR=$LIB/D02_SNBC_BAM

cd $FDR
mkdir NOBC_BAM/
mv *-00000.SNBC.bam* NOBC_BAM/

for F in *.bam
do

	samtools index $F &
	jobmax $PC_CPU_NUM
done
wait
pwd
echo "BAM   files number = "$(ls *.bam|wc -l )
echo "INDEX files number = "$(ls *.bai|wc -l )
cd $OUTSIDE


