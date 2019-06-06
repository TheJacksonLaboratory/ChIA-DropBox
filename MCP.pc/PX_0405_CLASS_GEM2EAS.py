import os,sys
#IN="T20.BCLINE.FRAGMENT_GEMLINE.H"
IN=sys.argv[1]
FIN=open(IN,"r")

FOUTS=open(IN+".S","w")
FOUTA=open(IN+".A","w")
FOUTE=open(IN+".E","w")


while True:
	line=FIN.readline()
	if not line:
		break
	TYPE=line.rstrip("\n").split("|")[0]
	T1=TYPE.split(":")[0]
	T2=TYPE.split(":")[1]
	TAIL=line.rstrip("\n").split("|")[1]
	word=line.rstrip("\n").split("|")[1].split(";")
	D={}
	D2={}
	C=""
	BC=word[0]
	for i in range(1,len(word)):
		C=str(word[i].split("\t")[0])
		if not D.has_key(C):
			D[C]=1
			D2[C]=word[i]
		else:
			D[C]=D[C]+1
			D2[C]=D2[C]+";"+word[i]
	d=len(D)
	#print "d",d,D	
	if d>1: #print "INTER_CHROM",line
		newt1=T1+"-"+"E"
		newt2=T2+"-chrnum"+str(d)
		newtype=newt1+":"+newt2
		
		FOUTE.write(newtype+"|"+TAIL+"\n")
	elif d == 1:
		for k in D:
			if D[k]==1: #print "SINGLETOM",line
				newt1=T1+"-"+"S"
				newt2=T2+"-chrnum"+str(d)
				newtype=newt1+":"+newt2
				FOUTS.write(newtype+"|"+TAIL+"\n")
			elif D[k] > 1: #"INTRA_CHROM"
				USF=D2[k].split(";")
				#print USF
				USFD={}
				SFL=[]
				for u in range(len(USF)):
					S=int(USF[u].split("\t")[1])
					USFD[S]=USF[u]
				for v in sorted(USFD,key=int):
					SFL.append(USFD[v])
				SF=";".join(SFL)
				newline=BC+";"+SF
				newt1=T1+"-"+"A"
                                newt2=T2+"-chrnum"+str(d)
                                newtype=newt1+":"+newt2
				FOUTA.write(newtype+"|"+newline+"\n")
				#print "INTRA_CHROM",line
			else:
				sys.exit("error at div SAE")

"""
$cat T20.BCLINE.FRAGMENT_GEMLINE.H
H:fnH5|SHG0007H-BX-TTTGTGTAGGCGGAAG;chr12	53600655	53601283	1	SHG0007H-BX-TTTGTGTAGGCGGAAG-0000F;chr13	79117155	79117741	1	SHG0007H-BX-TTTGTGTAGGCGGAAG-0001F;chr16	12896577	12897205	2	SHG0007H-BX-TTTGTGTAGGCGGAAG-0002F;chr17	77391668	77392296	1	SHG0007H-BX-TTTGTGTAGGCGGAAG-0003F;chr3	122444907	122445535	4	SHG0007H-BX-TTTGTGTAGGCGGAAG-0004F
M-H|SHG0007H-BX-TTTGTGTAGGCTACGA;chr1	9388807	9389392	2	SHG0007H-BX-TTTGTGTAGGCTACGA-0000F;chr5	116469174	116469802	1	SHG0007H-BX-TTTGTGTAGGCTACGA-0001F

"""

