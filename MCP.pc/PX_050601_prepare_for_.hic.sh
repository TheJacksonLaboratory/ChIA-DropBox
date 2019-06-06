
LIB=$1
F=${LIB}_COMBINED_SA.SUBGEM.bsv.gff.GEMLINE_OUT.tsv.BE2_FRAGNUM.bedpe_PlinePpair
cat $F|awk '{if($3>=$2){pos1=$2+($3-$2)/2;} else{pos1=$3+($2-$3)/2;} if($6>=$5){pos2=$5+($6-$5)/2;} else{pos2=$6+($5-$6)/2;} if($1<=$4){chr1=$1;chr1p=pos1;chr2=$4;chr2p=pos2;} else{chr1=$4;chr1p=pos2;chr2=$1;chr2p=pos1;} printf("%d %s %d %d %d %s %d %d\n",0,chr1,chr1p+0.5,0,0,chr2,chr2p+0.5,1);}'|sort -k2,2d -k6,6d  > $F.MID_LOOP







