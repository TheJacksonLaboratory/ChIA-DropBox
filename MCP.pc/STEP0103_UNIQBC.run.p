OUTSIDE=`pwd`
source ${OUTSIDE}/MCP.conf
source ${OUTSIDE}/MCP.module
source ${OUTSIDE}/MCP.tools


FAT=D01_Barcode
FDR=DIVBC
cd $LIB/$FAT/$FDR

SC=${FUNDIR}/PX_0103_UNIQBC.sh

for F in ${LIB}.BC.[0-9][0-9][0-9][0-9]
do
        sh $SC $F &
	jobmax $PC_CPU_NUM
done
wait
echo "BC.sN.uniq = "$(ls *.sN.uniq|wc -l )
cd $OUTSIDE


