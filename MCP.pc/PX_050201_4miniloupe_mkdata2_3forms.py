"""
$head P2CHIA10.GAPEXT3000.COMBINED_SA.GENSUB.bsv.gff.GEMLINE_OUT.tsv.NEWBC.all_lib.headed
GEM_ID	SPECIES	TRACC_BACK	GEM_REGION	GEM_COV	GEM_FRAGNUM	GEM_READNUM	FRAG_LEN_LIST	READ_COUNT_LIST	F2F_DISTANCE_LIST
SHG0021N-10000-100000001-AAACACCAGAAACCCGBX21N-NS500460-FA-1-0	FLY	fragnumF2-chrnum1	chr3R:6104253-26138208	20033955	2	2	628,595	1,1	20032732,0
SHG0021N-10000-100000050-AAACACCAGAGCTATABX21N-NS500460-FA-1-0	FLY	fragnumF2-chrnum1	chr2L:5189877-12474432	7284555	2	10	773,581	9,1	7283201,0
SHG0021N-10000-100000057-AAACACCAGAGGTTATBX21N-NS500460-FA-1-0	FLY	fragnumF3-chrnum1	chr2L:2060859-17682166	15621307	3	11	731,644,745	4,2,5	4170247,11448940,0
"""

import os,sys
#IN="TEST100"
IN=sys.argv[1]
FIN=open(IN,"r")
FOUT01=open(IN+".Fragnum_PlinePgem","w")
FOUT=open(IN+".F2FPAIR_PlinePpair","w")
FOUT03=open(IN+".bedpe_PlinePpair","w")
while True:
	line=FIN.readline()
	if not line:
		break
	if line.startswith("GEM_ID"):
		continue
	word=line.rstrip("\n").split("\t")
	GEM_ID=word[0]
	SPECIES=word[1]
	TRACC_BACK=word[2]
	GEM_REGION=word[3]
	GEM_COV=word[4]
	GEM_FRAGNUM=word[5]
	GEM_READNUM=word[6]
	FRAG_LEN_LIST=word[7]
	READ_COUNT_LIST=word[8]
	F2F_DISTANCE_LIST=word[9]
	
	GEMCHR=GEM_REGION.split(":")[0]
	GEMSTART=GEM_REGION.split(":")[1].split("-")[0]
	GEMEND=GEM_REGION.split(":")[1].split("-")[1]
	FRAGS=FRAG_LEN_LIST.split(",")
	GAPS=F2F_DISTANCE_LIST.split(",")	
	FRAGNUM=len(FRAGS)
	GAPNUM=len(GAPS)
	if FRAGNUM != GAPNUM:
		##print "FRAGNUM != GAPNUM"
		break
	LASTEND=int(GEMSTART)
	##print line
	FRAGLINE=""
	for i in range(FRAGNUM):
		FRAGSTART=int(LASTEND)
		FRAGEND=int(LASTEND)+int(FRAGS[i])
		LASTEND=FRAGEND+int(GAPS[i])
		##print i,FRAGSTART,FRAGEND
		newline=GEMCHR+"\t"+str(FRAGSTART)+"\t"+str(FRAGEND)
		newline04=GEMCHR+":"+str(FRAGSTART)+"-"+str(FRAGEND)
		if FRAGLINE=="":
			FRAGLINE=newline
			NUMFRAGLINE=newline04+"("+str(i)+")"
		else:
			FRAGLINE=FRAGLINE+";"+newline
			NUMFRAGLINE=NUMFRAGLINE+";"+newline04+"("+str(i)+")"
	##print NUMFRAGLINE
	FOUT01.write(NUMFRAGLINE+"|"+line)	
	FRS=FRAGLINE.split(";")
	for i in range(len(FRS)):
		for j in  range(len(FRS)):
			if i < j : 
				newline02="\t".join([FRS[i],FRS[j],GEM_FRAGNUM])+"|"+str(i)+"-"+str(j)+"|"+line.rstrip("\n")
				##print newline02
				FOUT.write(newline02+"\n")
				newline03="\t".join([FRS[i],FRS[j],GEM_FRAGNUM,GEM_ID])
				FOUT03.write(newline03+"\n")


