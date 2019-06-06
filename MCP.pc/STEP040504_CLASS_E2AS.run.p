############################
OUTSIDE=`pwd`
source ${OUTSIDE}/MCP.conf
source ${OUTSIDE}/MCP.module
source ${OUTSIDE}/MCP.tools

FDR=$LIB/D04_SNBC_READ
cd $FDR
FRR=R04aI_GEMCLASS
cd $FRR


for F in ${LIB}*.E
do


	SC=${FUNDIR}/PX_0405_CLASS_E2AS.py
        module unload python; module unload bedtools;
        module load python/2.7.3;module load bedtools/2.26.0;
	python $SC $F	

done
pwd
SFX="E.A"
echo "$SFX num = "$(ls *.$SFX|wc -l)
SFX="E.S"
echo "$SFX num = "$(ls *.$SFX|wc -l)



cd $OUTSIDE
