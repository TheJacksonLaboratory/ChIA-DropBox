#F=humadn.combined.mapq-ge30.clusters.gz

CUR=$(pwd)
SC=${CUR}"/SH06s1.merge_ovlped_frag.py"
S="human.combined.mapq-ge30.clusters.gz.SUBLIB.SELECT"
ls $S
echo "input SPRITE .CHRSUB"
read F

cd ${CUR}/$S/$F
#chrY.chrsub
for F in chr*.chrsub.sNsC
do
echo ' module load python; python '$SC' '$F|qsub -d`pwd` -N $F
done

