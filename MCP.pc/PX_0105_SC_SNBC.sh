import os,sys
#P="../"
IN=sys.argv[1]
#IN="SHG0008H.BC.uniq.nbc"
#SHG0008H-10000001-AAACACCAGAAACCCG
#SHG0008H-10000002-AAACACCAGAAACCGC
FOUT=open(IN+".SNBC","w")
FIN=open(IN,"r")
while True:
	line=FIN.readline()
	if not line:
		break
	word=line.rstrip("\n").split("-")
	LIB=word[0]
	BC=word[2]
	NUM=word[1]
	SUB=str(int(NUM)/10000)
	newline="-".join([LIB,SUB,NUM,BC])
	FOUT.write(newline+"\n")

