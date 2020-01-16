echo "################"
DF_LIB=$(pwd | rev|cut -d"/" -f1|rev|xargs) ## SHG0019H
read -e -i "$DF_LIB" -p "Library name: " RD_LIB
LIB="${LIB:-$DF_LIB}"
echo "~~~~~~~~~~"
echo $LIB
echo "################"
DF_QSUB_ID=$(echo $LIB|cut -c 4-)
read -e -i "$DF_QSUB_ID" -p "qsub ID: " RD_QSUB_ID
QSUB_ID="${QSUB_ID:-$RD_QSUB_ID}"
echo "~~~~~~~~~~"
echo $QSUB_ID
echo "##################"
#DF_MRO_ID=$(echo $LIB|cut -c 4-)i
DF_MRO_ID=$(echo $LIB|cut -c 4-|rev| awk '{if(substr($0,0,1)=="H") print substr($0,2)"1"; if(substr($0,0,1)=="N") print substr($0,2)"2"; if(substr($0,0,1)=="V") print substr($0,2)"3";else print $0}'|rev)
echo $DF_MRO_ID
read -e -i "$DF_MRO_ID" -p "Longranger .mro LIB-ID (must be all digits): " RD_MRO_ID
MRO_ID="${MRO_ID:-$RD_MRO_ID}"
echo $MRO_ID
echo "~~~~~~~~~~"
echo $MRO_ID
echo "##################"
#DF_FASTQ_DIR=$(ls -d /projects/ruan-lab/FASTQ/multi_chia/*${LIB}-*)
CDIR=$(pwd)
DF_FASTQ_DIR=$CDIR/MCP.FASTQ/
read -e -i "$DF_FASTQ_DIR" -p "folder of fastq: " RD_FASTQ_DIR
FASTQ_DIR="${FASTQ_DIR:-$RD_FASTQ_DIR}"
ls  $FASTQ_DIR/$LIB*
echo "~~~~~~~~~~"
echo $FASTQ_DIR
ls $FASTQ_DIR
echo "###################"
DF_FASTQ_PREFIX=$(ls $FASTQ_DIR/${LIB}*|rev|cut -d"/" -f1|rev|cut -d"_" -f1,2,3|uniq)
echo "EXAMPLE:  SHG0066_GT18-06593_SI-GA-A1_S5_L001_I1_001.fastq.gz"
read -e -i "$DF_FASTQ_PREFIX" -p "fastq prefix: " RD_FASTQ_PREFIX
FASTQ_PREFIX="${FASTQ_PREFIX:-$RD_FASTQ_PREFIX}"
ls  $FASTQ_DIR/$FASTQ_PREFIX*
echo "~~~~~~~~~~"
echo $FASTQ_PREFIX
echo "###################"
#DF_PC_CPU_NUM=$(cat /proc/cpuinfo | awk '/^processor/{print $3}' | wc -l)
DF_PC_CPU_NUM=16
read -e -i "$DF_PC_CPU_NUM" -p "cpu number required: " RD_PC_CPU_NUM
PC_CPU_NUM="${PC_CPU_NUM:-$RD_PC_CPU_NUM}"
echo "~~~~~~~~~~"
echo $PC_CPU_NUM
echo "###################"

DF_MEM=150gb
read -e -i "$DF_MEM" -p "memory size required: " RD_MEM
MEM="${MEM:-$RD_MEM}"
echo "~~~~~~~~~~"
echo $MEM
echo "###################"


DF_WALLTIME=36
read -e -i "$DF_WALLTIME" -p "pipeline running time requierd: " RD_WALLTIME
WALLTIME="${WALLTIME:-$RD_WALLTIME}"
echo "~~~~~~~~~~"
echo $WALLTIME
echo "###################"



DF_GAPEXT=3000
read -e -i "$DF_GAPEXT" -p "$GAPEXT fragment extention size (0, 3000, 5000 ...): " RD_GAPEXT
GAPEXT="${GAPEXT:-$RD_GAPEXT}"
echo "~~~~~~~~~~"
echo $GAPEXT
echo "###################"
DF_TIME=`date +%Y%m%d-%H%M%S`
read -e -i "$DF_TIME" -p "execute mark: $TIME" RD_TIME
TIME="${TIME:-$RD_TIME}"
echo "~~~~~~~~~~"
echo $TIME
echo "###################"
while [ -z "$GENDER" ];do  read -p "cell gender (m=male; f=female) : " GENDER;done
echo "~~~~~~~~~~"
echo $GENDER
echo "###################"

#while [ -z "$SPE_TYPE" ];do  read -p "species: H=human/mouse; F=fly; HF=human+fly; FH=fly+human;  " SPE_TYPE;done
#while [ -z "$SPE_TYPE" ];do  read -p "SPE_TYPE (hg19, dm3, dm3hg19, hg19dm3, hg38, dm6) : " SPE_TYPE;done
#echo "~~~~~~~~~~"
#echo $SPE_TYPE
#echo "###################"
#while [ -z "$GENOME_VERSION" ];do  read -p "genome reference (H=hg19,hg38; F=dm3,dm6; FH= dm3hg19; HF=hg19dm3;) : " GENOME_VERSION;done
while [ -z "$GENOME_VERSION" ];do  read -p "genome reference (hg19, hg38, mm9, mm10, dm3, dm6, dm3hg19, hg19dm3) : " GENOME_VERSION;done
CURRENTDIR=`pwd`
FUNDIR=${CURRENTDIR}/MCP.pc/ #function path
case $GENOME_VERSION in
	"hg19")
		SPE_TYPE="H"
		GENOME_SIZE=$FUNDIR/GSIZE/hg19.txt
		DF_HIC_GENOME_SIZE=$GENOME_SIZE
		read -e -i "$DF_HIC_GENOME_SIZE" -p "genome size file: " RD_HIC_GENOME_SIZE
                HIC_GENOME_SIZE="${HIC_GENOME_SIZE:-$RD_HIC_GENOME_SIZE}"
                echo "~~~~~~~~~~"
                echo $HIC_GENOME_SIZE
                echo "###################"
		DF_REF_PATH=$CDIR"/MCP.REF/refdata-hg19-2.1.0"
		ls -d $DF_REF_PATH
		read -e -i "$DF_REF_PATH" -p "genome reference directory: " RD_REF_PATH
		REF_PATH="${REF_PATH:-$RD_REF_PATH}"
		echo "~~~~~~~~~~"
		echo $REF_PATH
		echo "###################";;
        "hg38")
                SPE_TYPE="H"
                GENOME_SIZE=$FUNDIR/GSIZE/hg38.txt
                DF_HIC_GENOME_SIZE=$GENOME_SIZE
                read -e -i "$DF_HIC_GENOME_SIZE" -p "genome size file: " RD_HIC_GENOME_SIZE
                HIC_GENOME_SIZE="${HIC_GENOME_SIZE:-$RD_HIC_GENOME_SIZE}"
                echo "~~~~~~~~~~"
                echo $HIC_GENOME_SIZE
                echo "###################"
                DF_REF_PATH=$CDIR"/MCP.REF/refdata-GRCh38-2.1.0"
                ls -d $DF_REF_PATH
                read -e -i "$DF_REF_PATH" -p "genome reference directory: " RD_REF_PATH
                REF_PATH="${REF_PATH:-$RD_REF_PATH}"
                echo "~~~~~~~~~~"
                echo $REF_PATH
                echo "###################";;
        "mm9")
                SPE_TYPE="H"
                GENOME_SIZE=$FUNDIR/GSIZE/mm9.txt
                DF_HIC_GENOME_SIZE=$GENOME_SIZE
                read -e -i "$DF_HIC_GENOME_SIZE" -p "genome size file: " RD_HIC_GENOME_SIZE
                HIC_GENOME_SIZE="${HIC_GENOME_SIZE:-$RD_HIC_GENOME_SIZE}"
                echo "~~~~~~~~~~"
                echo $HIC_GENOME_SIZE
                echo "###################"
                DF_REF_PATH=$CDIR"/MCP.REF/refdata-mm9"
                ls -d $DF_REF_PATH
                read -e -i "$DF_REF_PATH" -p "genome reference directory: " RD_REF_PATH
                REF_PATH="${REF_PATH:-$RD_REF_PATH}"
                echo "~~~~~~~~~~"
                echo $REF_PATH
                echo "###################";;
        "mm10")
                SPE_TYPE="H"
                GENOME_SIZE=$FUNDIR/GSIZE/mm10.txt
                DF_HIC_GENOME_SIZE=$GENOME_SIZE
                read -e -i "$DF_HIC_GENOME_SIZE" -p "genome size file: " RD_HIC_GENOME_SIZE
                HIC_GENOME_SIZE="${HIC_GENOME_SIZE:-$RD_HIC_GENOME_SIZE}"
                echo "~~~~~~~~~~"
                echo $HIC_GENOME_SIZE
                echo "###################"
                DF_REF_PATH=$CDIR"/MCP.REF/refdata-mm10"
                ls -d $DF_REF_PATH
                read -e -i "$DF_REF_PATH" -p "genome reference directory: " RD_REF_PATH
                REF_PATH="${REF_PATH:-$RD_REF_PATH}"
                echo "~~~~~~~~~~"
                echo $REF_PATH
                echo "###################";;
        "dm6")
                SPE_TYPE="F"
                GENOME_SIZE=$FUNDIR/GSIZE/dm6.txt
                DF_HIC_GENOME_SIZE=$GENOME_SIZE
                read -e -i "$DF_HIC_GENOME_SIZE" -p "genome size file: " RD_HIC_GENOME_SIZE
                HIC_GENOME_SIZE="${HIC_GENOME_SIZE:-$RD_HIC_GENOME_SIZE}"
                echo "~~~~~~~~~~"
                echo $HIC_GENOME_SIZE
                echo "###################"
                DF_REF_PATH=$CDIR"/MCP.REF/refdata-dm6"
                ls -d $DF_REF_PATH
                read -e -i "$DF_REF_PATH" -p "genome reference directory: " RD_REF_PATH
                REF_PATH="${REF_PATH:-$RD_REF_PATH}"
                echo "~~~~~~~~~~"
                echo $REF_PATH
                echo "###################";;
	"dm3")
                SPE_TYPE="F"
		GENOME_SIZE=$FUNDIR/GSIZE/dm3.txt
         	DF_HIC_GENOME_SIZE=$FUNDIR/GSIZE/dm3_len_6CHROM.txt
                read -e -i "$DF_HIC_GENOME_SIZE" -p "genome size file: " RD_HIC_GENOME_SIZE
                HIC_GENOME_SIZE="${HIC_GENOME_SIZE:-$RD_HIC_GENOME_SIZE}"
                echo "~~~~~~~~~~"
                echo $HIC_GENOME_SIZE
                echo "###################"
                DF_REF_PATH=$CDIR"/MCP.REF/refdata-dm3"
		ls -d $DF_REF_PATH
                read -e -i "$DF_REF_PATH" -p "genome reference directory: " RD_REF_PATH
                REF_PATH="${REF_PATH:-$RD_REF_PATH}"
                echo "~~~~~~~~~~"
                echo $REF_PATH
                echo "###################";;
	"hg19dm3")

                SPE_TYPE="HF"
		GENOME_SIZE=$FUNDIR/GSIZE/hg19_dm3.txt
		DF_HIC_GENOME_SIZE=$GENOME_SIZE
                read -e -i "$DF_HIC_GENOME_SIZE" -p "genome size file: " RD_HIC_GENOME_SIZE
                HIC_GENOME_SIZE="${HIC_GENOME_SIZE:-$RD_HIC_GENOME_SIZE}"
                echo "~~~~~~~~~~"
                echo $HIC_GENOME_SIZE
                echo "###################"
                DF_REF_PATH=$CDIR"/MCP.REF/refdata-hg19_dm3"
                ls -d $DF_REF_PATH
                read -e -i "$DF_REF_PATH" -p "genome reference directory: " RD_REF_PATH
                REF_PATH="${REF_PATH:-$RD_REF_PATH}"
                echo "~~~~~~~~~~"
                echo $REF_PATH
                echo "###################";;
        "dm3hg19")
                SPE_TYPE="FH"
                GENOME_SIZE=$FUNDIR/GSIZE/dm3_hg19.txt
		DF_HIC_GENOME_SIZE=$GENOME_SIZE
                read -e -i "$DF_HIC_GENOME_SIZE" -p "genome size file: " RD_HIC_GENOME_SIZE
                HIC_GENOME_SIZE="${HIC_GENOME_SIZE:-$RD_HIC_GENOME_SIZE}"
                echo "~~~~~~~~~~"
                echo $HIC_GENOME_SIZE
                echo "###################"
                DF_REF_PATH=$CDIR"/MCP.REF/refdata-dm3_hg19"
                ls -d $DF_REF_PATH
                read -e -i "$DF_REF_PATH" -p "genome reference directory: " RD_REF_PATH
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
echo "GENOME_VERSION=${GENOME_VERSION}" >> $CONF
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

