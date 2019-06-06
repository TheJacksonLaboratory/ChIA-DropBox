############################
OUTSIDE=`pwd`
source ${OUTSIDE}/MCP.conf
source ${OUTSIDE}/MCP.module
source ${OUTSIDE}/MCP.tools


echo $SPE_TYPE
FDR=$LIB/D04_SNBC_READ
cd $FDR

FRR=R04aI_GEMCLASS
rm -rf $FRR
mkdir $FRR

cd R04a_GEMLINE
for F in ${LIB}*GEMLINE
do
	SC=${FUNDIR}/PX_0405_REFORM_GEM_${SPE_TYPE}.py
	module unload python; module unload bedtools;
	module load python/2.7.3;module load bedtools/2.26.0;
	python $SC $F &
	jobmax $PC_CPU_NUM
done
wait
SFX="H"
echo "$SFX num = "$(ls *.$SFX|wc -l)
SFX="F"
echo "$SFX num = "$(ls *.$SFX|wc -l)
SFX="M"
echo "$SFX num = "$(ls *.$SFX|wc -l)


cd $OUTSIDE


