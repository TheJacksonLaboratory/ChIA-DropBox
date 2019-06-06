import os,sys
#IN="SHG0008H205.combined.TOTAL_GEM.sorted.bsv.fnE5.div"
#LIB="SHG0008H205"
IN=sys.argv[1]
#LIB=sys.argv[2]
#LIB=IN.split(".")[0]+"-"+IN.split(".")[-1]
LIB=sys.argv[2]
FIN=open(IN,"r")
FOUT=open(IN+".gff","w")
while True:
	line=FIN.readline()
	if not line:
		break
	word=line.rstrip("\n").split("|")
	BC=word[0]
	SPE=word[1]
	FTP=word[2]
	T1=word[3]
	T2=word[4]
	GEM_REGION=word[6]
	GEMC=GEM_REGION.split(":")[0]
	GEMS=GEM_REGION.split(":")[1].split("-")[0]
	GEME=GEM_REGION.split(":")[1].split("-")[1]
	GEM_COV=word[8]
	FRAG_NUM=word[10]
	GEM_READ_NUM=word[12]
	FRAG_LEN=word[14]
	READ_COUNT=word[16]
	F2F_DISTANCE=word[18]
	FRAGMENTS=[]
	FRAGLINES=[]
	FRAG_LEN=",".join(FRAG_LEN.split(";"))
	READ_COUNT=",".join(READ_COUNT.split(";"))
	F2F_DISTANCE=",".join(F2F_DISTANCE.split(";"))
	transcript_anno=";".join(["gene_id="+BC,"transcript_id="+BC,"SPECIES="+SPE,"TYPE1="+T1,"TYPE2="+T2,"GEM_REGION="+GEM_REGION,"GEM_COV="+GEM_COV,"GEM_FRAGNUM="+FRAG_NUM,"GEM_READNUM="+GEM_READ_NUM,"FRAG_LEN_LIST="+FRAG_LEN,"READ_COUNT_LIST="+READ_COUNT,"F2F_DISTANCE_LIST="+F2F_DISTANCE])

        for i in range(20,len(word)):
                FRAGMENTS.append(word[i])
		FRAGLINES.append(word[i].replace(";","-"))
	FRAGLINE=";".join(FRAGLINES)

	transcript_line="\t".join([GEMC,LIB,"transcript",GEMS,GEME,".",".",".",transcript_anno,FRAGLINE])
	FOUT.write(transcript_line+"\n")
	#print FRAG_NUM,len(FRAGMENTS)
	for j in range(len(FRAGMENTS)):
		FC=FRAGMENTS[j].split(";")[0].split(":")[0]
		FS=FRAGMENTS[j].split(";")[0].split(":")[1].split("-")[0]
		FE=FRAGMENTS[j].split(";")[0].split(":")[1].split("-")[1]
		FID=FRAGMENTS[j].split(";")[2]
		READCOUNT=FRAGMENTS[j].split(";")[1]
		exon_anno=";".join([transcript_anno,"fragment_id="+FID,"FRAG_REGION="+FC+":"+FS+"-"+FE,"FRAG_LEN="+FRAG_LEN.split(",")[j],"READ_COUNT="+str(READCOUNT),"F2F_DISTANCE="+F2F_DISTANCE.split(",")[j]  ])
		exon_line="\t".join([FC,LIB,"exon",FS,FE,".",".",".",exon_anno])
		FOUT.write(exon_line+"\n")
"""

$head SHG0008H205.combined.TOTAL_GEM.sorted.bsv.fnE4.div
SHG0008H-BX-TTAGTTCCACTTGGAT|FLY|INTRACHROM|M-F-E-A|fragnumH3F8-fragnumF8-chrnum3-subGEM1|GEM_REGION|dchr2R:2879341-14804545|GEM_COV|11925204|GEM_FRAG_NUM|4|GEM_READ_NUM|43|FRAG_LEN|835;628;630;623|READ_COUNT|40;1;1;1|F2F_DISTANCE|5161229;6326111;435148;0|FRAGMENTS|dchr2R:2879341-2880176;40;SHG0008H-BX-TTAGTTCCACTTGGAT-FRAG0001|dchr2R:8041405-8042033;1;SHG0008H-BX-TTAGTTCCACTTGGAT-FRAG0003|dchr2R:14368144-14368774;1;SHG0008H-BX-TTAGTTCCACTTGGAT-FRAG0005|dchr2R:14803922-14804545;1;SHG0008H-BX-TTAGTTCCACTTGGAT-FRAG0006
SHG0008H205.combined.TOTAL_GEM.sorted.bsv.fnE4.div
"""

