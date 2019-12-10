#F=human.combined.mapq-ge30.clusters.gz

ls
echo "input SPRITE .clusters.gz"
read F
mkdir $F.SUBLIB
cd $F.SUBLIB
zcat ../$F|awk -F"." -v NM=$F '{print >> NM"."$1".sublib"}'




