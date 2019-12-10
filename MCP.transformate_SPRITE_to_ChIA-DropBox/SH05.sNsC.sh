#F=humadn.combined.mapq-ge30.clusters.gz

CUR=$(pwd)
S="human.combined.mapq-ge30.clusters.gz.SUBLIB.SELECT"
ls $S
echo "input SPRITE .CHRSUB"
read F

cd ${CUR}/$S/$F
#chrY.chrsub
for F in chr*.chrsub
do
echo 'cat '$F'|sort -k4,4 -k1,1 -k2,2n -k3,3n > '$F'.sNsC'|qsub -d`pwd` -N $F
done

