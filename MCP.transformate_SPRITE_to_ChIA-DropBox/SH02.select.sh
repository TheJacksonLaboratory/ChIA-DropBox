#F=humadn.combined.mapq-ge30.clusters.gz

CUR=$(pwd)
S="human.combined.mapq-ge30.clusters.gz.SUBLIB"
ls $S
echo "input SPRITE .sublib"
read F
D=$S.SELECT
mkdir $D
cd $D
cat ${CUR}/${S}/${F}|awk '{for (i=2;i<=NF;i++) print $i"\t"$1 }' > $F.PlinePpos
#DPM6D6.NYBot87_Stg.Odd2Bo48.Even2Bo29.Odd2Bo50	chr17:7756055	chr8:76739863	chr1:227403869	chr1:36687903	chr17:78995366	chr1:184906658	chr3:58470873	chr3:58470774	chr3:58472511	chr1:64947407	chr8:36749681

