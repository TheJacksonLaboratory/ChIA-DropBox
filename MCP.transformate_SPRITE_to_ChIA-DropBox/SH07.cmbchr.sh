#F=humadn.combined.mapq-ge30.clusters.gz

CUR=$(pwd)
SC=${CUR}"/SH06s1.merge_ovlped_frag.py"
S="human.combined.mapq-ge30.clusters.gz.SUBLIB.SELECT"
ls $S
#chrY.chrsub.sNsC.OvlpMerg
echo "input SPRITE .CHRSUB"
read F

cd ${CUR}/$S/$F
#chrY.chrsub
cat chr*.chrsub.sNsC.OvlpMerg > ../$F.chrsub.sNsC.OvlpMerg.chrcmb
