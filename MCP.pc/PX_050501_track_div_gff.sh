LIB=$1
F=${LIB}_COMBINED_SA.SUBGEM.bsv.gff
for FN in {1..6}
do
cat $F|awk -F"[;=]" -v num=${FN} '{if($16>=num)print}' > $F.BE${FN}_FN.gff

done

