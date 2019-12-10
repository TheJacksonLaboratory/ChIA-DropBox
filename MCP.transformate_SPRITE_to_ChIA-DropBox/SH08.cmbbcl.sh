#F=humadn.combined.mapq-ge30.clusters.gz

CUR=$(pwd)
SC=${CUR}"/SH08s1_mkBCLINE.py"
S="human.combined.mapq-ge30.clusters.gz.SUBLIB.SELECT"
ls $S
#chrY.chrsub.sNsC.OvlpMerg
echo "input SPRITE .OvlpMerg.chrcmb"
read F
#human.combined.mapq-ge30.clusters.gz.DPM6E4.sublib.PlinePpos.CHRSUB.chrsub.sNsC.OvlpMerg.chrcmb

cd ${CUR}/$S
#chrY.chrsub
echo ' module load python; python '$SC' '$F|qsub -d`pwd` -N $F



