#F=humadn.combined.mapq-ge30.clusters.gz

CUR=$(pwd)
S="human.combined.mapq-ge30.clusters.gz.SUBLIB.SELECT"
ls $S
echo "input SPRITE .CHRSUB"
read F

cd ${CUR}/$S/$F
mkdir HETCHR
mv *_* HETCHR


