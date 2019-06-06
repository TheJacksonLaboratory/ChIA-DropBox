

#PX_0201a_ORI_SC_SBAM_by_SNBC.py  PX_0201b_GEO_SC_SBAM_by_SNBC.py  PX_0201_SC_SBAM_by_SNBC.py


echo "This data is download from GEO (SRR...) or NOT? (SRR/NOT):"
read SRR
if [ $SRR == "SRR" ]
then
cp MPC.pc/PX_0201b_GEO_SC_SBAM_by_SNBC.py  MPC.pc/PX_0201_SC_SBAM_by_SNBC.py
else
cp MPC.pc/PX_0201a_ORI_SC_SBAM_by_SNBC.py  MPC.pc/PX_0201_SC_SBAM_by_SNBC.py
fi 
SHG0051H_GT18-08809_SI-GA-B5_S20_L004_R1_001.fastq.gz


LIB=$(pwd|rev|cut -d"/" -f1|rev)
cd MCP.FASTQ
mv SRR*1.fastq ${LIB}_GT18-08809_SI-GA-B5_S20_L004_R1_001.fastq.gz
mv SRR*2.fastq ${LIB}_GT18-08809_SI-GA-B5_S20_L004_R2_001.fastq.gz
