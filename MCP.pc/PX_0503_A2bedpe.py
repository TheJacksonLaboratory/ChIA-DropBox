"""
$head -n 2 P2CHIA10X.INTERandINTRA.F.A P2CHIA10X.INTERandINTRA.F.E
==> P2CHIA10X.INTERandINTRA.F.A <==
F-A:fragnumF2-chrnum1|SHG0021N-10000-100000001-AAACACCAGAAACCCGBX1-NS500460;chr3R	6104253	6104881	1	SHG0021N-10000-100000001-AAACACCAGAAACCCGBX1-NS500460-FRAG0000;chr3R	26137613	26138208	1	SHG0021N-10000-100000001-AAACACCAGAAACCCGBX1-NS500460-FRAG0001
F-A:fragnumF2-chrnum1|SHG0021N-10000-100000013-AAACACCAGAAGCTCGBX1-NS500460;chr3R	8397997	8398656	2	SHG0021N-10000-100000013-AAACACCAGAAGCTCGBX1-NS500460-FRAG0000;chr3R	9204446	9205246	20	SHG0021N-10000-100000013-AAACACCAGAAGCTCGBX1-NS500460-FRAG0001

==> P2CHIA10X.INTERandINTRA.F.E <==
F-E:fragnumF2-chrnum2|SHG0021N-10000-100000009-AAACACCAGAACTCGGBX1-NS500460;chr3L	1969752	1970368	3	SHG0021N-10000-100000009-AAACACCAGAACTCGGBX1-NS500460-FRAG0000;chrX	21834956	21835526	1	SHG0021N-10000-100000009-AAACACCAGAACTCGGBX1-NS500460-FRAG0001
F-E:fragnumF7-chrnum4|SHG0021N-10000-100000016-AAACACCAGAAGTTCABX1-NS500460;chr2R	3615942	3616570	1	SHG0021N-10000-100000016-AAACACCAGAAGTTCABX1-NS500460-FRAG0000;chr2L	9616885	9617646	6	SHG0021N-10000-100000016-AAACACCAGAAGTTCABX1-NS500460-FRAG0001;chr3R	11156292	11156970	4	SHG0021N-10000-100000016-AAACACCAGAAGTTCABX1-NS500460-FRAG0002;chrX	15238819	15239376	1	SHG0021N-10000-100000016-AAACACCAGAAGTTCABX1-NS500460-FRAG0003;chrX	15253053	15254066	2	SHG0021N-10000-100000016-AAACACCAGAAGTTCABX1-NS500460-FRAG0004;chr3R	19699821	19700402	4	SHG0021N-10000-100000016-AAACACCAGAAGTTCABX1-NS500460-FRAG0005;chr3R	27781031	27781636	1	SHG0021N-10000-100000016-AAACACCAGAAGTTCABX1-NS500460-FRAG0006
"""


import os,sys
#IN="P2CHIA10X.INTERandINTRA.F.A"
IN=sys.argv[1]
FIN=open(IN,"r")
FOUT=open(IN+".bedpe_fragnum_gemid","w")
while True:
	line=FIN.readline()
	if not line:
		break
	word=line.rstrip("\n").split(";")
	FN=len(word)-1
#	print line
	FN_POSITION=1
	GEM_ID=word[0].split("|")[1]
	for i in range(FN_POSITION,len(word)):
		##print i, word[i]
		for j in range(FN_POSITION,len(word)):
			if i < j:
				#print i,j,word[i],word[j]
				C1=word[i].split("\t")[0]
				S1=word[i].split("\t")[1]
				E1=word[i].split("\t")[2]
				C2=word[j].split("\t")[0]
                                S2=word[j].split("\t")[1]
                                E2=word[j].split("\t")[2]
				#print C1,S1,E1,C2,S2,E2,FN,GEM_ID
				newline="\t".join([C1,S1,E1,C2,S2,E2,str(FN),GEM_ID])
				#print newline
				FOUT.write(newline+"\n")


