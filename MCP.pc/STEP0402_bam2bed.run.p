
############################
OUTSIDE=`pwd`
source ${OUTSIDE}/MCP.conf
source ${OUTSIDE}/MCP.module
source ${OUTSIDE}/MCP.tools

FDR=$LIB/D04_SNBC_READ
cd $FDR

FRR=R01_PET2R1/
rm -rf $FRR
mkdir $FRR
cd $FRR

for F in ../R00_F2304/${LIB}*.F2304.bam
do


	file=$(ls $F|rev|cut -d"/" -f1|rev)
	sh ${FUNDIR}/PX_0402_BAMtoBED.sh $F $file  &
	jobmax $PC_CPU_NUM
done
wait
pwd
echo "R1.bed number = "$(ls *.R1.bed|wc -l )
echo "R2.bed number = "$(ls *.R2.bed|wc -l )
cd $OUTSIDE


