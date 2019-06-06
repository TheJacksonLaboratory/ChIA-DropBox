
LIB=$1
FUNDIR=$2
D05=$3
SPE=$4
#SHG2122C_COMBINED_SA.SUBGEM
python ${FUNDIR}/PX_0501_PA12_BSC_${SPE}.py ${LIB}_COMBINED_SA.SUBGEM
python ${FUNDIR}/PX_0501_PA13_mkGFF.py ${LIB}_COMBINED_SA.SUBGEM.bsv $LIB
python ${FUNDIR}/PX_0501_PA14_mkTSV.py ${LIB}_COMBINED_SA.SUBGEM.bsv.gff
chmod 755 *_OUT.tsv
mv ${LIB}_COMBINED_SA.SUBGEM.bsv ${LIB}_COMBINED_SA.SUBGEM.bsv.gff ${LIB}_COMBINED_SA.SUBGEM.bsv.gff.FRAGLINE_OUT.tsv ${LIB}_COMBINED_SA.SUBGEM.bsv.gff.GEMLINE_OUT.tsv ${D05}