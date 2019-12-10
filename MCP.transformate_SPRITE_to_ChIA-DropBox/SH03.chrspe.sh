#F=humadn.combined.mapq-ge30.clusters.gz

CUR=$(pwd)
S="human.combined.mapq-ge30.clusters.gz.SUBLIB.SELECT"
ls $S
echo "input SPRITE .PlinePpos"
read F
D=$F.CHRSUB
rm -rf $S/$D
mkdir $S/$D
cd $S/$D
#h hr1:56293030	DPM6E12.NYBot17_Stg.Odd2Bo88.Even2Bo11.Odd2Bo82
cat ${CUR}/$S/${F}|awk -F"[:\t]" -v OFS="\t" '{print $1,$2,$2+500,$3 >> $1".chrsub"}'
#DPM6D6.NYBot87_Stg.Odd2Bo48.Even2Bo29.Odd2Bo50	chr17:7756055	chr8:76739863	chr1:227403869	chr1:36687903	chr17:78995366	chr1:184906658	chr3:58470873	chr3:58470774	chr3:58472511	chr1:64947407	chr8:36749681

