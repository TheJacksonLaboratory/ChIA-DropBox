

echo "
CDB0 = STEP0000_MAPPING.run
CDB1 = STEP0001_MKDOO.run
CDB2 = STEP0101_GETBC.run
CDB3 = STEP0102_DIVBC.run
CDB4 = STEP0103_UNIQBC.run.p
CDB5 = STEP0104_COMUNIQNBC.run
CDB6 = STEP0105_SNBC.run
CDB7 = STEP0201_SNBCBAM.run
CDB8 = STEP0202_INDEXBAM.run.p
CDB9 = STEP0401_F2304.run.p
CDB10 = STEP0402_bam2bed.run.p
CDB11 = STEP0403_SH_BCLINE.run.p
CDB12 = STEP040401_merge_to_fregment.run.p
CDB13 = STEP040402_output_fragment.run
CDB14 = STEP040501_CLASIFY.run.p
CDB15 = STEP040502_further_extension.run
CDB16 = STEP040503_CLASS_GEM2EAS.run.p
CDB17 = STEP040504_CLASS_E2AS.run.p
CDB18 = STEP040505_COMBINE_SA.run
CDB19 = STEP040506_SUBGEM.run
CDB20 = STEP0501_RESULT.run
CDB21 = STEP050200_data_for_miniloupe_FRAGNUM_BE2.run
CDB22 = STEP050201_4miniloupe_mkdata2_3forms.run
CDB23 = STEP050202_4miniloupe_PlinePfrag.run
CDB24 = STEP050203_4miniloupe_mkregion_file.run
CDB25 = STEP050204_PlinePgemSimp.run
CDB26 = STEP050205_PfragPlineWgem.run
CDB27 = STEP0503_4heatmap.run
CDB28 = STEP0504_bedgraph.run
CDB29 = STEP050501_div_gff.run
CDB30 = STEP050502_mktrack_4basic.run
CDB31 = STEP050601_prepare_for_.hic.run
CDB32 = STEP050602_mk_.hic.run
CDB33 = STEP1001_sta.run
CDB34 = STEP1101_STA2.run
CDB35 = STEP1201_REPORT.run
CDB36 = STEP2000_prepare_data_for_plot.sh
CDB37 = STEP2001_plot.sh
CDB38 = STEP2002_combine_image.run
"
echo "from"
read FROM
echo "TO"
read TO

CUR=$(pwd)
source $CUR/MCP.conf

echo $LIB
echo $CMT
head -n 2 MCPPC.qsub > MCPPC.HEAD.B

wait
cat MCPPC.HEAD.B MCPPC.PART.qsub.SAMPLE > MCPPC.PART.qsub.SAMPLE.HEADED
wait


echo "B/S (B=big resource; S=small resource)"
read BS 

echo $BS
if [[ $BS == "S" ]]
then
	echo $BS
	cat  MCPPC.HEAD.S MCPPC.PART.qsub.SAMPLE  >  MCPPC.PART.qsub.SAMPLE.HEADED
fi


wait
cp MCPPC.PART.qsub.SAMPLE.HEADED MCPPC.PART.${FROM}-${TO}.qsub

sed -i 's/FROM=0/FROM='${FROM}'/g' MCPPC.PART.${FROM}-${TO}.qsub
sed -i 's/TO=38/TO='${TO}'/g' MCPPC.PART.${FROM}-${TO}.qsub
sed -i 's/LIBNAME/'${LIB}.${FROM}.${TO}.${GENOME_VERSION}'/g' MCPPC.PART.${FROM}-${TO}.qsub






head MCPPC.PART.${FROM}-${TO}.qsub
ls MCPPC.PART.${FROM}-${TO}.qsub
echo 'qsub  MCPPC.PART.'${FROM}'-'${TO}'.qsub'








