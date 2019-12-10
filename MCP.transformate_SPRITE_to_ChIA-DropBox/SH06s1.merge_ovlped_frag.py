import os,sys

IN=sys.argv[1]
FIN=open(IN,"r")
FOUT=open(IN+".OvlpMerg","w")
LASTID=""
lastline=""
while True:
	line=FIN.readline()
	if not line:
		FOUT.write(lastline)		
		break
	word=line.rstrip("\n").split("\t")
	C=word[0]
	S=int(word[1])
	E=int(word[2])
	ID=word[3]
	if LASTID == "":
		LASTID=ID
		lastline=line
		continue
	if LASTID != ID:
		FOUT.write(lastline)
		LASTID=ID
		lastline=line
		continue
	if LASTID == ID:
		lastword=lastline.rstrip("\n").split("\t")
                LASTC=lastword[0]
                LASTS=int(lastword[1])
                LASTE=int(lastword[2])	
		if LASTE < S:
			FOUT.write(lastline)
                	LASTID=ID
                	lastline=line
                	continue
		elif LASTE >= S:
			lastline="\t".join([LASTC,str(LASTS),str(E),ID,"\n"])	
			LASTID=ID
