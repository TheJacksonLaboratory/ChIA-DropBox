import os,sys
IN=sys.argv[1]
FIN=open(IN,"r")
FOUT=open(IN+".bsv","w")
#M-H-E-A;fragnumH7F5-fragnumH7-chrnum6-subGEM4;SHG0008H-BX-TTAGTTCCACTTCTTA;chr12	67753344	67753972	1	SHG0008H-BX-TTAGTTCCACTTCTTA-FRAG0006;chr12	116755692	116756445	4	SHG0008H-BX-TTAGTTCCACTTCTTA-FRAG0009
while True:
	line=FIN.readline()
	if not line:
		break
	word=line.rstrip("\n").split(";")
	T1=word[0]
	T2=word[1]
	BC=word[2]
	FRAGS=""
	for i in range(3,len(word)):
		#print word[i]
		if FRAGS=="":
			FRAGS=word[i]
		else:
			FRAGS=FRAGS+"|"+word[i]
	#print FRAGS
	########################### 
	FINAL_TYPE="" 

	if T1.endswith("-A"):
		#print "INTRA",line
		FINAL_TYPE="INTRACHROM"
	elif T1.endswith("-S"):    
                #print "SINGLE",line
		FINAL_TYPE="SINGLEFRAG"	
	#print FINAL_TYPE,FRAGS
	########################### 
	MIN_START=9999999999999999
	MAX_END=0
	GEM_REGION=""
	GEM_COV=0
	FRAG_NUM=0
	STR_READ_COUNT=""
	GAP=""
	FIN_GENOME=""
	L_GAP=[]
	L_READ_COUNT=[]
	frag=FRAGS.split("|")
	FRAG_LEN=""
	NEW_FRAGS=""
	for i in range(len(frag)):
		C=frag[i].split("\t")[0]
		S=int(frag[i].split("\t")[1])
		E=int(frag[i].split("\t")[2])
		READ_COUNT=frag[i].split("\t")[3]
		FRAG_NAME=frag[i].split("\t")[4]
		newfrag=C+":"+str(S)+"-"+str(E)+";"+READ_COUNT+";"+FRAG_NAME
		if NEW_FRAGS=="":
			NEW_FRAGS=newfrag
		else:
			NEW_FRAGS=NEW_FRAGS+"|"+newfrag


		L_READ_COUNT.append(READ_COUNT)
		if FRAG_LEN=="":
			FRAG_LEN=str(E-S)
		else:
			FRAG_LEN=FRAG_LEN+";"+str(E-S)
		MIN_START=min(MIN_START,S)
		MAX_END=max(MAX_END,E)
		if C.startswith("XXXXchr"):
			FIN_GENOME="HUMAN"
		elif C.startswith("chr"):
			FIN_GENOME="FLY"
		else:
			print "ERROR ON SPE",FIN_GENOME
			break
		if i == len(frag)-1:
			L_GAP.append("0")
		else:
			S_NEXT=int(frag[i+1].split("\t")[1])
			gap=str(S_NEXT-E)
			L_GAP.append(gap)
		
	for i in range(len(L_GAP)):
		if GAP=="":
			GAP=L_GAP[i]
		else:
			GAP=GAP+";"+L_GAP[i]
	
	#print MIN_START,MAX_END,FRAGS
	GEM_REGION=C+":"+str(MIN_START)+"-"+str(MAX_END)
	GEM_COV=str(MAX_END-MIN_START)
	FRAG_NUM=str(len(frag))
	GEM_READ_NUM=0
	for i in range(len(L_READ_COUNT)):
		GEM_READ_NUM=GEM_READ_NUM+int(L_READ_COUNT[i])
		if STR_READ_COUNT=="":
			STR_READ_COUNT=L_READ_COUNT[i]
		else:
			STR_READ_COUNT=STR_READ_COUNT+";"+L_READ_COUNT[i]
	#print  GEM_REGION,GEM_COV,FRAG_NUM,STR_READ_COUNT,GAP,line
	########################### 
	
	newline="|".join([BC,FIN_GENOME,FINAL_TYPE,T1,T2,"GEM_REGION",GEM_REGION,"GEM_COV",GEM_COV,"GEM_FRAG_NUM",FRAG_NUM,"GEM_READ_NUM",str(GEM_READ_NUM),"FRAG_LEN",FRAG_LEN,"READ_COUNT",STR_READ_COUNT,"F2F_DISTANCE",GAP,"FRAGMENTS",NEW_FRAGS])	

	FOUT.write(newline+"\n")		


"""
$head TEST300.combined.TOTAL_GEM.sorted
M-F-E-A:fragnumH7F5-fragnumF5-chrnum3-subGEM0;SHG0007H-BX-TTTGTGTAGGCGTAGT;dchr2R	3984111	3984696	2	SHG0007H-BX-TTTGTGTAGGCGTAGT-FRAG0000;dchr2R	4298792	4299378	3	SHG0007H-BX-TTTGTGTAGGCGTAGT-FRAG0001;dchr2R	17203924	17204510	1	SHG0007H-BX-TTTGTGTAGGCGTAGT-FRAG0003
M-F-E-S:fragnumH7F5-fragnumF5-chrnum3-subGEM1;SHG0007H-BX-TTTGTGTAGGCGTAGT;dchr2L	5604950	5605578	2	SHG0007H-BX-TTTGTGTAGGCGTAGT-FRAG0002
M-F-E-S:fragnumH7F5-fragnumF5-chrnum3-subGEM2;SHG0007H-BX-TTTGTGTAGGCGTAGT;dchr3L	17971377	17971947	1	SHG0007H-BX-TTTGTGTAGGCGTAGT-FRAG0004
M-H-E-A:fragnumH7F5-fragnumH7-chrnum4-subGEM0;SHG0007H-BX-TTTGTGTAGGCGTAGT;chr7	65480595	65481223	2	SHG0007H-BX-TTTGTGTAGGCGTAGT-FRAG0005;chr7	100002309	100002937	SHG0007H-BX-TTTGTGTAGGCGTAGT-FRAG0009
M-H-E-A:fragnumH7F5-fragnumH7-chrnum4-subGEM2;SHG0007H-BX-TTTGTGTAGGCGTAGT;chr3	134770390	134770975	1	SHG0007H-BX-TTTGTGTAGGCGTAGT-FRAG0010;chr3	183334179	183334765	SHG0007H-BX-TTTGTGTAGGCGTAGT-FRAG0011
"""

