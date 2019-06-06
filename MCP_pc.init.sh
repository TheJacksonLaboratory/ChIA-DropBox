echo "################"
DF_LIB=$(pwd | rev|cut -d"/" -f1|rev|xargs) ## SHG0019H
read -e -i "$DF_LIB" -p "LIB: " RD_LIB
LIB="${LIB:-$DF_LIB}"
echo "~~~~~~~~~~"
echo $LIB
echo "################"
DF_QSUB_ID=$(echo $LIB|cut -c 6-)
read -e -i "$DF_QSUB_ID" -p "QSUB_ID: " RD_QSUB_ID
QSUB_ID="${QSUB_ID:-$RD_QSUB_ID}"
echo "~~~~~~~~~~"
echo $QSUB_ID
echo "##################"
DF_MRO_ID=$(echo $LIB|cut -c 6-)
read -e -i "$DF_MRO_ID" -p "MRO_ID (must all digits): " RD_MRO_ID
MRO_ID="${MRO_ID:-$RD_MRO_ID}"
echo "~~~~~~~~~~"
echo $MRO_ID
echo "##################"
DF_FASTQ_DIR=$(ls -d /projects/ruan-lab/FASTQ/multi_chia/*${LIB}-*)
read -e -i "$DF_FASTQ_DIR" -p "FASTQ_DIR: " RD_FASTQ_DIR
FASTQ_DIR="${FASTQ_DIR:-$RD_FASTQ_DIR}"
ls -R $FASTQ_DIR/$LIB*
echo "~~~~~~~~~~"
echo $FASTQ_DIR
ls $FASTQ_DIR
echo "###################"
DF_FASTQ_PREFIX=$(ls $FASTQ_DIR/${LIB}*|rev|cut -d"/" -f1|rev|cut -d"_" -f1,2,3|uniq)
echo "EXAMPLE:  SHG0066_GT18-06593_SI-GA-A1_S5_L001_I1_001.fastq.gz"
read -e -i "$DF_FASTQ_PREFIX" -p "FASTQ_PREFIX: " RD_FASTQ_PREFIX
FASTQ_PREFIX="${FASTQ_PREFIX:-$RD_FASTQ_PREFIX}"
ls -l $FASTQ_DIR/$FASTQ_PREFIX*
echo "~~~~~~~~~~"
echo $FASTQ_PREFIX
echo "###################"
#DF_PC_CPU_NUM=$(cat /proc/cpuinfo | awk '/^processor/{print $3}' | wc -l)
DF_PC_CPU_NUM=16
read -e -i "$DF_PC_CPU_NUM" -p "PC_CPU_NUM: " RD_PC_CPU_NUM
PC_CPU_NUM="${PC_CPU_NUM:-$RD_PC_CPU_NUM}"
echo "~~~~~~~~~~"
echo $PC_CPU_NUM
echo "###################"

DF_MEM=150gb
read -e -i "$DF_MEM" -p "PC_MEM: " RD_MEM
MEM="${MEM:-$RD_MEM}"
echo "~~~~~~~~~~"
echo $MEM
echo "###################"


DF_WALLTIME=10
read -e -i "$DF_WALLTIME" -p "WALLTIME: " RD_WALLTIME
WALLTIME="${WALLTIME:-$RD_WALLTIME}"
echo "~~~~~~~~~~"
echo $WALLTIME
echo "###################"



DF_GAPEXT=0
read -e -i "$DF_GAPEXT" -p "$GAPEXT (0, 3000, 5000 ...): " RD_GAPEXT
GAPEXT="${GAPEXT:-$RD_GAPEXT}"
echo "~~~~~~~~~~"
echo $GAPEXT
echo "###################"
DF_TIME=`date +%Y%m%d-%H%M%S`
read -e -i "$DF_TIME" -p "$TIME: " RD_TIME
TIME="${TIME:-$RD_TIME}"
echo "~~~~~~~~~~"
echo $TIME
echo "###################"
while [ -z "$GENDER" ];do  read -p "GENDER (m=male; f=female) : " GENDER;done
echo "~~~~~~~~~~"
echo $GENDER
echo "###################"



while [ -z "$SPE_TYPE" ];do  read -p "SPE_TYPE (H=hg19, F=dm3, FH=dm3+hg19, HF=hg19+dm3) : " SPE_TYPE;done
echo "~~~~~~~~~~"
echo $SPE_TYPE
echo "###################"
CURRENTDIR=`pwd`
FUNDIR=${CURRENTDIR}/MCP.pc/ #function path
case $SPE_TYPE in
	"H")
		GENOME_SIZE=$FUNDIR/hg19.txt
		DF_HIC_GENOME_SIZE=$GENOME_SIZE
		read -e -i "$DF_HIC_GENOME_SIZE" -p "HIC_GENOME_SIZE: " RD_HIC_GENOME_SIZE
                HIC_GENOME_SIZE="${HIC_GENOME_SIZE:-$RD_HIC_GENOME_SIZE}"
                echo "~~~~~~~~~~"
                echo $HIC_GENOME_SIZE
                echo "###################"
		DF_REF_PATH="/projects/ruan-lab/Sequence_pool/10X/REFGNM10X/refdata-hg19-2.1.0"
		ls -d $DF_REF_PATH
		read -e -i "$DF_REF_PATH" -p "REF_PATH: " RD_REF_PATH
		REF_PATH="${REF_PATH:-$RD_REF_PATH}"
		echo "~~~~~~~~~~"
		echo $REF_PATH
		echo "###################";;
	"F")
		GENOME_SIZE=$FUNDIR/dm3.txt
         	DF_HIC_GENOME_SIZE=$FUNDIR/dm3_len_6CHROM.txt
                read -e -i "$DF_HIC_GENOME_SIZE" -p "HIC_GENOME_SIZE: " RD_HIC_GENOME_SIZE
                HIC_GENOME_SIZE="${HIC_GENOME_SIZE:-$RD_HIC_GENOME_SIZE}"
                echo "~~~~~~~~~~"
                echo $HIC_GENOME_SIZE
                echo "###################"
                DF_REF_PATH="/projects/ruan-lab/Sequence_pool/10X/REFGNM10X/refdata-dm3"
		ls -d $DF_REF_PATH
                read -e -i "$DF_REF_PATH" -p "REF_PATH: " RD_REF_PATH
                REF_PATH="${REF_PATH:-$RD_REF_PATH}"
                echo "~~~~~~~~~~"
                echo $REF_PATH
                echo "###################";;
	"HF")
		GENOME_SIZE=$FUNDIR/hg19_dm3.txt
		DF_HIC_GENOME_SIZE=$GENOME_SIZE
                read -e -i "$DF_HIC_GENOME_SIZE" -p "HIC_GENOME_SIZE: " RD_HIC_GENOME_SIZE
                HIC_GENOME_SIZE="${HIC_GENOME_SIZE:-$RD_HIC_GENOME_SIZE}"
                echo "~~~~~~~~~~"
                echo $HIC_GENOME_SIZE
                echo "###################"
                DF_REF_PATH="/projects/ruan-lab/Sequence_pool/10X/REFGNM10X/refdata-hg19_dm3"
                ls -d $DF_REF_PATH
                read -e -i "$DF_REF_PATH" -p "REF_PATH: " RD_REF_PATH
                REF_PATH="${REF_PATH:-$RD_REF_PATH}"
                echo "~~~~~~~~~~"
                echo $REF_PATH
                echo "###################";;
        "FH")
                GENOME_SIZE=$FUNDIR/dm3_hg19.txt
		DF_HIC_GENOME_SIZE=$GENOME_SIZE
                read -e -i "$DF_HIC_GENOME_SIZE" -p "HIC_GENOME_SIZE: " RD_HIC_GENOME_SIZE
                HIC_GENOME_SIZE="${HIC_GENOME_SIZE:-$RD_HIC_GENOME_SIZE}"
                echo "~~~~~~~~~~"
                echo $HIC_GENOME_SIZE
                echo "###################"
                DF_REF_PATH="/projects/ruan-lab/Sequence_pool/10X/REFGNM10X/refdata-dm3_hg19"
                ls -d $DF_REF_PATH
                read -e -i "$DF_REF_PATH" -p "REF_PATH: " RD_REF_PATH
                REF_PATH="${REF_PATH:-$RD_REF_PATH}"
                echo "~~~~~~~~~~"
                echo $REF_PATH
                echo "###################";;
esac


#############
#OUTPUT >> MCP.conf
CONF=${CURRENTDIR}/MCP.conf.head
rm -rf $CONF
echo "#TIME=$TIME" >>  $CONF
echo "PC_CPU_NUM=${PC_CPU_NUM}" >> $CONF
# echo "=${}" >> $CONF
echo 'LIB="'${LIB}'"' >> $CONF
echo "QSUB_ID=${QSUB_ID}" >> $CONF

echo "GAPEXT=${GAPEXT}" >> $CONF
echo "CURRENTDIR=`pwd`" >> $CONF
echo "FUNDIR=${CURRENTDIR}/MCP.pc/" >>  $CONF
echo "MRO=${CURRENTDIR}/MCP.mro" >>  $CONF

echo "SPE_TYPE=${SPE_TYPE}" >> $CONF
echo "GENOME_SIZE=${GENOME_SIZE}" >> $CONF
echo "HIC_GENOME_SIZE=${HIC_GENOME_SIZE}" >> $CONF

#cat $CONF MCP.conf.tail > MCP.conf 
cp $CONF MCP.conf
#############
cp MCP.mro.SAMPLE MCP.mro

sed -i 's/MRO_LIB/'$LIB'/g' MCP.mro
sed -i 's/MRO_ID/'$MRO_ID'/g' MCP.mro
sed -i 's|MRO/READ/PATH|'$FASTQ_DIR'|g' MCP.mro
sed -i 's/MRO_NAME/'$FASTQ_PREFIX'/g' MCP.mro
sed -i 's|MRO_REF|'$REF_PATH'|g' MCP.mro
sed -i 's/MRO_GENDER/'$GENDER'/g' MCP.mro


#############
cp MCPPC.qsub.SAMPLE MCPPC.qsub
sed -i 's/QSUBLIBNAME/'$LIB'/g' MCPPC.qsub
sed -i 's/ppn=16/ppn='${PC_CPU_NUM}'/g' MCPPC.qsub
sed -i 's/mem=150gb,/mem='${MEM}',/g' MCPPC.qsub   
sed -i 's/walltime=2/walltime='${WALLTIME}'/g' MCPPC.qsub   

############
MAPPING=MCP.pc/STEP0000_MAPPING.run
sed -i 's/CPUNUM/'${PC_CPU_NUM}'/g' MCP.pc/STEP0000_MAPPING.run
sed -i 's/MEMSIZE/'${MEM}',/g' MCP.pc/STEP0000_MAPPING.run
#longranger wgs  $LIB $MRO  --jobmode=local  --localcores=CPUNUM --localmem=MEMSIZE

