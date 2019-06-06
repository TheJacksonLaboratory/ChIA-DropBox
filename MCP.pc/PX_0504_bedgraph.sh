## in D05_TABLE/
FUNDIR=$1
LIB=$2
GENOME_SIZE=$3
echo $FUNDIR

cat ../D04_SNBC_READ/R02_BCLINE/*.lenBE50.CHR_CLEAN|sort -k1,1 -k2,2n|awk -v OFS="\t" '{if($6!="+")print $1,$2,$3,$4,$5,"-"; else print $0}' > ${LIB}_COMBINED.R1.lenBE50.CHR_CLEAN.sC.bed
wait
genomeCoverageBed -bg -i ${LIB}_COMBINED.R1.lenBE50.CHR_CLEAN.sC.bed -g ${GENOME_SIZE} > ${LIB}_COMBINED.R1.lenBE50.CHR_CLEAN.sC.rcov.bedgraph

cat ${LIB}_COMBINED_SA.SUBGEM.bsv.gff.GEMLINE_OUT.tsv.BE2_FRAGNUM.Fragnum_PlinePgem.PlinePfrag |sort -k1,1 -k2,2n > ${LIB}_COMBINED_SA.SUBGEM.bsv.gff.GEMLINE_OUT.tsv.BE2_FRAGNUM.Fragnum_PlinePgem.PlinePfrag.bed.sC
wait
genomeCoverageBed -bg -i  ${LIB}_COMBINED_SA.SUBGEM.bsv.gff.GEMLINE_OUT.tsv.BE2_FRAGNUM.Fragnum_PlinePgem.PlinePfrag.bed.sC  -g ${GENOME_SIZE} > ${LIB}_COMBINED_SA.BE2_FRAGNUM.sC.fcov.bedgraph
wait
cat ${LIB}_COMBINED_SA.SUBGEM.bsv.gff.GEMLINE_OUT.tsv.BE2_FRAGNUM.bedpe_PlinePpair|awk -v OFS="\t" '{print $1,$2,$3"\n"$4,$5,$6}'|sort -k1,1 -k2,2n > ${LIB}_COMBINED_SA.SUBGEM.bsv.gff.GEMLINE_OUT.tsv.BE2_FRAGNUM.bedpe_PlinePpair.anchor.sC
wait
genomeCoverageBed -bg -i ${LIB}_COMBINED_SA.SUBGEM.bsv.gff.GEMLINE_OUT.tsv.BE2_FRAGNUM.bedpe_PlinePpair.anchor.sC -g ${GENOME_SIZE} > ${LIB}.SA.BE2_FRAGNUM.bedpe_PlinePpair.acov.bedgraph



