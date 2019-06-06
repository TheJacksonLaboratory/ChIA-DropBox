FUNDIR=$1
GATE=$2 ##200000 == max F2F distance
echo $FUNDIR , $GATE

SC1=${FUNDIR}/PX_050502_mktrack_4basic.py
for F in *_FN.gff
do 
python ${FUNDIR}/PX_050502_mktrack_4basic.py $F
done

#GATE=200000
for F in *_COMBINED_SA.SUBGEM.bsv.gff.BE1_FN.gff.BASIC
do

python ${FUNDIR}/PX_050503_FILTER_GEM_BY_DISTANCE.py $F $GATE

done

for F in *_COMBINED_SA.SUBGEM.bsv.gff.BE1_FN.gff.BASIC.SE200000_F2F
do

for n in 1 2 3 4 5
do
cat $F|awk -v N=$n '{if($12 >= N )print}' >> $F.BE${n}.BASIC

done

done
#d.name	d.chrom	d.strand	d.txStart	d.txEnd	d.cdsStart	d.cdsEnd	d.exonStarts	d.exonEnds	d.kgXref.geneSymbol	d.kgXref.mRNA	d.score
#SHG0031_10010003	chr7	+	69517575	69518151	69517575	69518151	69517575	69518151	SHG0031_10010003	SHG0031_10010003	1



