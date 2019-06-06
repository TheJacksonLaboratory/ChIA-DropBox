SC1=$1
GNM_SIZE=$2
SC2=$3
F=$4
	file=$(ls $F|rev|cut -d"/" -f1|rev)
	cat $F|awk '{if($5>=30) print}' > $file.q30
	cat $file.q30|awk '{if($3-$2>=50)print}' > $file.q30.lenBE50
	cat $file.q30.lenBE50 |grep -v "EBV"|grep -v "_random"|grep -v "chrUn"|grep -v "hs"|grep -v "Het"|grep -v "chrU"|grep -v "chrM"|grep -v "extra" > $file.q30.lenBE50.CHR_CLEAN
	python $SC1 $GNM_SIZE $file.q30.lenBE50.CHR_CLEAN
	python $SC2 $file.q30.lenBE50.CHR_CLEAN.5e0_3e500.EXT
	#echo "STEP0403-FINISHED "$F

