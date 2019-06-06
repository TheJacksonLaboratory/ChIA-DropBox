############################
OUTSIDE=`pwd`
source ${OUTSIDE}/MCP.conf
source ${OUTSIDE}/MCP.module
source ${OUTSIDE}/MCP.tools

FDR=$LIB/D04_SNBC_READ
cd $FDR
FRR=R04aI_GEMCLASS
cd $FRR



for F in *.FRAGMENT_GEMLINE.${SPE_TYPE}
do

	SC=${FUNDIR}/PX_0405_CLASS_GEM2EAS.py
        module unload python; module unload bedtools;
        module load python/2.7.3;module load bedtools/2.26.0;	
	python $SC $F &
	jobmax $PC_CPU_NUM
done
wait
pwd
SFX="${SPE_TYPE}.E"
echo "$SFX num = "$(ls *.$SFX|wc -l)
SFX="${SPE_TYPE}.A"
echo "$SFX num = "$(ls *.$SFX|wc -l)
SFX="${SPE_TYPE}.S"
echo "$SFX num = "$(ls *.$SFX|wc -l)


cd $OUTSIDE






