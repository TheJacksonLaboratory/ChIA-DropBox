rm -rf MCP.REF
mkdir MCP.REF
cd MCP.REF
echo "input 10X_genome_index located folder"
read REF
for R in $REF/refdata*
do
ln -s $R

done
cd ../


