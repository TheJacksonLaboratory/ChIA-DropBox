############################
OUTSIDE=`pwd`
source ${OUTSIDE}/MCP.conf
source ${OUTSIDE}/MCP.module
source ${OUTSIDE}/MCP.tools

FDR=${OUTSIDE}/$LIB/D04_SNBC_READ
cd $FDR

FRR=$FDR/R02_BCLINE/
rm -fr $FRR
mkdir $FRR
cd $FRR


SC1="${FUNDIR}/PX_0403_EXT_R1_3e500.py"
SC2="${FUNDIR}/PX_0403_BCLINE.py"

for F in ../R01_PET2R1/*.R1.bed
do
        V=$(ls $F|rev|cut -d"/" -f1|rev|cut -d"-" -f2|cut -d"." -f1)
        if [ $V -ne 0 ]
        then
	        sh ${FUNDIR}/PX_0403_SH_BCLINE.sh $SC1 $GENOME_SIZE $SC2 $F &
	        jobmax $PC_CPU_NUM
        fi
done
wait
cd $FRR
pwd
echo "q30 number = "$(ls *.q30|wc -l )
echo "lenBE50 number = "$(ls *.lenBE50|wc -l )
echo "CHR_CLEAN number = "$(ls *.CHR_CLEAN|wc -l )
echo "5e0_3e500.EXT number = "$(ls *.5e0_3e500.EXT|wc -l )
echo "BCline number = "$(ls *.BCline|wc -l )

cd $OUTSIDE



