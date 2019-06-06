############################
OUTSIDE=`pwd`
source ${OUTSIDE}/MCP.conf
source ${OUTSIDE}/MCP.module
source ${OUTSIDE}/MCP.tools

FDR=$LIB/D04_SNBC_READ
cd $FDR

FDRa="R04a_GEMLINE"
rm -rf $FDRa
mkdir $FDRa
FDRb="R04b_FRAGLINE"
rm -rf $FDRb
mkdir $FDRb
FDRc="R04c_READLINE"
rm -rf $FDRc
mkdir $FDRc

cd R02_BCLINE
#module unload python
#module load python/2.7.3;
#module load bedtools/2.26.0
SC=${FUNDIR}/PX_0404_FRAGLINE.py




for F in ${LIB}*.BCline
do

	python  $SC  $F  $GAPEXT &
	 jobmax $PC_CPU_NUM

done

wait
pwd
SFX="FRAGMENT_GEMLINE"
echo "$SFX num = "$(ls *.$SFX|wc -l)
SFX="FRAGMENT_FRAGLINE"
echo "$SFX num = "$(ls *.$SFX|wc -l)
SFX="FRAGMENT_READLINE"
echo "$SFX num = "$(ls *.$SFX|wc -l)



cd $OUTSIDE


