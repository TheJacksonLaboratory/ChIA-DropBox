"""
$cat TEST.Fragnum_PlinePgem
chr3R:6104253-6104881(0);chr3R:26137613-26138208(1)|SHG0021N-10000-100000001-AAACACCAGAAACCCGBX21N-NS500460-FA-1-0	FLY	fragnumF2-chrnum1	chr3R:6104253-26138208	2003395522	628,595	1,1	20032732,0
chr3R:8397997-8398656(0);chr3R:9204446-9205246(1)|SHG0021N-10000-100000013-AAACACCAGAAGCTCGBX21N-NS500460-FA-1-0	FLY	fragnumF2-chrnum1	chr3R:8397997-9205246	807249	222	659,800	2,20	805790,0
chr2L:6104487-6105062(0);chr2L:16268417-16269037(
"""

import os,sys
IN=sys.argv[1]
FIN=open(IN,"r")
FOUT=open(IN+".PlinePfragWgem","w")
while True:
	line=FIN.readline()
	if not line:
		break
	word=line.rstrip("\n").split("|")
	FRAGS=word[0].split(";")
	GEMINFO=word[1]
#	print line
	for i in range(len(FRAGS)):
		FC=FRAGS[i].split(":")[0]
		FS=FRAGS[i].split(":")[1].split("-")[0]
		FE=FRAGS[i].split(":")[1].split("-")[1].split("(")[0]
		FO=FRAGS[i].split("(")[1].rstrip(")")
		NEWFRAG="\t".join([FC,FS,FE,FO])
		newline="|".join([NEWFRAG,GEMINFO])
		FOUT.write(newline+"\n")



