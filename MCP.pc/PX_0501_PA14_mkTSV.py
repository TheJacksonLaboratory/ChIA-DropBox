import os,sys
IN=sys.argv[1]
FIN=open(IN,"r")
FOUT_GEM=open(IN+".GEMLINE_OUT.tsv","w")
FOUT_FRAG=open(IN+".FRAGLINE_OUT.tsv","w")
G_HEAD="\t".join(["GEM_ID","SPECIES","TRACC_BACK","GEM_REGION","GEM_COV","GEM_FRAGNUM","GEM_READNUM","FRAG_LEN_LIST","READ_COUNT_LIST","F2F_DISTANCE_LIST"])
#print G_HEAD
FOUT_GEM.write(G_HEAD+"\n")
F_HEAD="\t".join(["GEM_ID","FREG_ID","FRAG_REGION","FRAG_LEN","READ_COUNT","F2F_DISTANCE","GEM_FRAGNUM"])
FOUT_FRAG.write(F_HEAD+"\n")


while True:
	line=FIN.readline()		
	if not line:
		break
	word=line.rstrip("\n").split("\t")
	GTP=word[2]
	if GTP=="exon":
		#continue
		F_ANNO=word[8].split(";")
		F_LINE="\t".join([F_ANNO[0].split("=")[1],F_ANNO[12].split("=")[1],F_ANNO[13].split("=")[1],F_ANNO[14].split("=")[1],F_ANNO[15].split("=")[1],F_ANNO[16].split("=")[1],F_ANNO[7].split("=")[1]   ])
		#print F_LINE
                FOUT_FRAG.write(F_LINE+"\n")
	elif GTP=="transcript":
		G_ANNO=word[8].split(";")
		G_LINE="\t".join([  G_ANNO[0].split("=")[1],  G_ANNO[2].split("=")[1], G_ANNO[4].split("=")[1], G_ANNO[5].split("=")[1], G_ANNO[6].split("=")[1], G_ANNO[7].split("=")[1],G_ANNO[8].split("=")[1],G_ANNO[9].split("=")[1],G_ANNO[10].split("=")[1],G_ANNO[11].split("=")[1] ])
		#print G_LINE
		FOUT_GEM.write(G_LINE+"\n")
	
"""
$head SHG0008H205.combined.TOTAL_GEM.sorted.bsv.FLY_CHR.gff
chrX	SHG0008H205-FLY_CHR	transcript	7201241	11099851	.	.	.	gene_id=SHG0008H-BX-TTAGTTCCACTTCTTA-MFEA;transcript_id=SHG0008H-BX-TTAGTTCCACTTCTTA-MFEA;SPECIES=FLY;TYPE1=M-F-E-A;TYPE2=fragnumH7F5-fragnumF5-chrnum3-subGEM0;GEM_REGION=chrX:7201241-11099851;GEM_COV=3898610;GEM_FRAGNUM=2;GEM_READNUM=25;FRAG_LEN_LIST=1074,628;READ_COUNT_LIST=24,1;F2F_DISTANCE_LIST=3896908,0	chrX:7201241-7202315-24-SHG0008H-BX-TTAGTTCCACTTCTTA-FRAG0000;chrX:11099223-11099851-1-SHG0008H-BX-TTAGTTCCACTTCTTA-FRAG0003
chrX	SHG0008H205-FLY_CHR	exon	7201241	7202315	.	.	.	gene_id=SHG0008H-BX-TTAGTTCCACTTCTTA-MFEA;transcript_id=SHG0008H-BX-TTAGTTCCACTTCTTA-MFEA;SPECIES=FLY;TYPE1=M-F-E-A;TYPE2=fragnumH7F5-fragnumF5-chrnum3-subGEM0;GEM_REGION=chrX:7201241-11099851;GEM_COV=3898610;GEM_FRAGNUM=2;GEM_READNUM=25;FRAG_LEN_LIST=1074,628;READ_COUNT_LIST=24,1;F2F_DISTANCE_LIST=3896908,0;fragment_id=SHG0008H-BX-TTAGTTCCACTTCTTA-FRAG0000;FRAG_REGION=chrX:7201241-7202315;FRAG_LEN=1074;READ_COUNT=24;F2F_DISTANCE=3896908

"""
