#$cat human.combined.mapq-ge30.clusters.gz.DPM6E12.sublib.PlinePpos.CHRSUB.chrsub.sNsC.OvlpMerg.chrcmb.BCLCMB|sed 's/;$//'|awk -F"-" '{print >> $2}'|head

#F=humadn.combined.mapq-ge30.clusters.gz

CUR=$(pwd)
ls $CUR
#chrY.chrsub.sNsC.OvlpMerg
echo "input SPRITE .BCLCMB"
read F
#human.combined.mapq-ge30.clusters.gz.DPM6E4.sublib.PlinePpos.CHRSUB.chrsub.sNsC.OvlpMerg.chrcmb
echo "give a name of the lib"
read N

rm -rf $N
mkdir $N
cd $N
rm -rf $N
mkdir $N
cd $N
rm -rf D04_SNBC_READ
mkdir D04_SNBC_READ
cd D04_SNBC_READ
rm -rf R02_BCLINE
mkdir R02_BCLINE
cd R02_BCLINE


cat ${CUR}/$F|sed 's/;$//'|awk -F"-" -v NM=$N '{print >> NM"-"$2".SNBC.bam.F2304.bam.sN.bam.R1.bed.q30.lenBE50.CHR_CLEAN.5e0_3e500.EXT.BCline"}'

