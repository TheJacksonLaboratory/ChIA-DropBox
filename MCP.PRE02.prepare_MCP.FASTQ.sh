rm -rf MCP.FASTQ
mkdir MCP.FASTQ
cd MCP.FASTQ
echo "input fastq files located folder )"
read FQS
for F in $FQS/*
do
ln -s $F

done
ls -lrt

cd .. 

