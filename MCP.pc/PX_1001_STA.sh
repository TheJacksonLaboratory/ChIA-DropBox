
LIB=$1
FDR="D10_STA"


#rm -rf $FDR
#mkdir $FDR
#cd $FDR
echo $LIB > S00_lib_name.sta
head -n 1 ../D00_outs/summary.csv|sed -e 's/,/\n/g' > temp01
tail -n 1 ../D00_outs/summary.csv|sed -e 's/,/\n/g' > temp02
paste  temp01 temp02 > ${LIB}.summary 
rm -rf temp01 temp02
cd ../


cd $FDR
cat ${LIB}.summary|grep "pcr_duplication"|cut -f2 > S01_PCR.sta
if [ -s "S01_PCR.sta" ]
then
	echo "S01_PCR.sta  OK"
else
	echo 0 > S01_PCR.sta	
fi
cat ${LIB}.summary|grep "number_reads"|cut -f2|awk '{print $1/2}' > S02_TOTAL_PET_NUM.sta
if [ -s "S02_TOTAL_PET_NUM.sta" ]
then
        echo "S02_TOTAL_PET_NUM.sta  OK"
else
        echo 0 > S02_TOTAL_PET_NUM.sta
fi
#number_reads	5429624
#pcr_duplication	0.0068625806353224475
cd ../

#fi

cd $FDR
######
for F in ../D02_SNBC_BAM/*.bam
do
	NAME=$(ls $F|rev|cut -d"/" -f1|rev)
	samtools view $F|cut -f1|sort|uniq|wc -l > SUB.$NAME.PET.sub 

done
cat SUB.*.PET.sub|awk 'BEDGIN{sum=0}{sum=sum+$1}END{print sum}' > S03_PET_withBC.sta
rm -rf SUB_PET
mkdir SUB_PET
mv SUB.*.PET.sub SUB_PET

#{/Sequence_pool/10X/LOUPE/PIPE10X_R1/SHG0023/D02_SNBC_BAM/}{D02_SNBC_BAM}
#$samtools view -c SHG0023-1017.SNBC.bam|head
###########
#D04_SNBC_READ/R01_PET2R1/SHG0023-1000.SNBC.bam.F2304.bam.sN.bam.R1.bed
for F in ../D04_SNBC_READ/R01_PET2R1/*.R1.bed
do
        NAME=$(ls $F|rev|cut -d"/" -f1|rev)
	cat $F|wc -l > SUB.$NAME.R1.sub
done
cat SUB.*.R1.sub|awk 'BEDGIN{sum=0}{sum=sum+$1}END{print sum}' > S04_Uniq_mapped_R1.sta
rm -rf SUB_R1
mkdir SUB_R1
mv SUB.*.R1.sub SUB_R1

########
cd ../


##########
cd $FDR

#-----------------
  K="q30"
  NUM="S05"
  for F in ../D04_SNBC_READ/R02_BCLINE/*.${K}
    do
        NAME=$(ls $F|rev|cut -d"/" -f1|rev)
        cat $F|wc -l > SUB.$NAME.${K}.sub
    done

  cat SUB.*.${K}.sub|awk 'BEDGIN{sum=0}{sum=sum+$1}END{print sum}' > ${NUM}_R1_${K}.sta
  rm -rf SUB_${K}
  mkdir SUB_${K}
  mv SUB.*.${K}.sub SUB_${K}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~

#-----------------
  K="lenBE50"
  NUM="S06"
  for F in ../D04_SNBC_READ/R02_BCLINE/*.${K}
    do
        NAME=$(ls $F|rev|cut -d"/" -f1|rev)
        cat $F|wc -l > SUB.$NAME.${K}.sub
    done

  cat SUB.*.${K}.sub|awk 'BEDGIN{sum=0}{sum=sum+$1}END{print sum}' > ${NUM}_R1_${K}.sta
  rm -rf SUB_${K}
  mkdir SUB_${K}
  mv SUB.*.${K}.sub SUB_${K}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-----------------
  K="EXT"
  NUM="S07"
  for F in ../D04_SNBC_READ/R02_BCLINE/*.${K}
    do
        NAME=$(ls $F|rev|cut -d"/" -f1|rev)
        cat $F|wc -l > SUB.$NAME.${K}.sub
    done

  cat SUB.*.${K}.sub|awk 'BEDGIN{sum=0}{sum=sum+$1}END{print sum}' > ${NUM}_R1_${K}.sta
  rm -rf SUB_${K}
  mkdir SUB_${K}
  mv SUB.*.${K}.sub SUB_${K}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~

#-----------------
  K="CHR_CLEAN"
  NUM="S08"
  for F in ../D04_SNBC_READ/R02_BCLINE/*.${K}
    do
        NAME=$(ls $F|rev|cut -d"/" -f1|rev)
        cat $F|wc -l > SUB.$NAME.${K}.sub
    done

  cat SUB.*.${K}.sub|awk 'BEDGIN{sum=0}{sum=sum+$1}END{print sum}' > ${NUM}_R1_${K}.sta
  rm -rf SUB_${K}
  mkdir SUB_${K}
  mv SUB.*.${K}.sub SUB_${K}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~
cd ../
##########
### BC
#########
cd $FDR
cat ../D01_Barcode/${LIB}.CMBBC_MGUNIQ_NBC.SNBC|wc -l > K01_TOTAL_Barcode_num.sta

K="bam.R1.bed"
  NUM="K02"
  for F in ../D04_SNBC_READ/R01_PET2R1/*.${K}
    do
        NAME=$(ls $F|rev|cut -d"/" -f1|rev)
        cat $F|cut -f4|cut -d":" -f1 > SUB.$NAME.${K}.sub
    done

  cat SUB.*.${K}.sub|sort|uniq|wc -l > ${NUM}_BC_${K}.sta
  rm -rf SUB_${K}
  mkdir SUB_${K}
  mv SUB.*.${K}.sub SUB_${K}

K="CHR_CLEAN"
NUM="K03"
  for F in ../D04_SNBC_READ/R02_BCLINE/*.${K}
    do
        NAME=$(ls $F|rev|cut -d"/" -f1|rev)
        cat $F|cut -f4|cut -d":" -f1 > SUB.$NAME.${NUM}.${K}.sub
    done

  cat SUB.*.${NUM}.${K}.sub|sort|uniq|wc -l > ${NUM}_BC_${NUM}.${K}.sta
  rm -rf SUB_${NUM}_${K}
  mkdir SUB_${NUM}_${K}
  mv SUB.*.${NUM}.${K}.sub SUB_${NUM}_${K}



#{/Sequence_pool/10X/LOUPE/PIPE10X_R1/SHG0023/D04_SNBC_READ/R01_PET2R1/}{R01_PET2R1}
#$cat SHG0023-1031.SNBC.bam.F2304.bam.sN.bam.R1.bed|cut -f4|cut -d":" -f1

cd ../








