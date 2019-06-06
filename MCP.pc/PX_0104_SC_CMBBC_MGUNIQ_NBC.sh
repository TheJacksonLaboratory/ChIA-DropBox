#LIB=$(pwd|rev|cut -d"/" -f1|rev)
LIB=$1
FDR=$2
#FDR=D01_Barcode/DIVBC
cd $FDR
#mkdir  ERR LOG

rm -rf ${LIB}.CMBBC

sort -m *.sN.uniq > ${LIB}.CMBBC

cat ${LIB}.CMBBC|uniq > ${LIB}.CMBBC_MGUNIQ

LEN=$(cat ${LIB}.CMBBC_MGUNIQ|wc -l|awk '{print length($1)}')
NUM=$((10**($LEN+1)))
cat ${LIB}.CMBBC_MGUNIQ|awk -v NM=$LIB -v num=$NUM '{print NM"-"num+NR"-"$0}' > ${LIB}.CMBBC_MGUNIQ_NBC




