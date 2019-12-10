#$cat human.combined.mapq-ge30.clusters.gz.DPM6E12.sublib.PlinePpos.CHRSUB.chrsub.sNsC.OvlpMerg.chrcmb.BCLCMB|sed 's/;$//'|awk -F"-" '{print >> $2}'|head

#F=humadn.combined.mapq-ge30.clusters.gz

CUR=$(pwd)
S="human.combined.mapq-ge30.clusters.gz.SUBLIB.SELECT"
ls $S
echo "input SPRITE .SUBCL"
read F
ls ${CUR}/${S}/$F


