import os,sys
IN=sys.argv[1]
FIN=open(IN,"r")

FOUTS=open(IN+".S","w")
FOUTA=open(IN+".A","w")


while True:
	line=FIN.readline()
	if not line:
		break
	word=line.rstrip("\n").split("|")[1].split(";")
	TYPE=line.rstrip("\n").split("|")[0]
	T1=TYPE.split(":")[0]
	T2=TYPE.split(":")[1]

	TAIL=line.rstrip("\n").split("|")[1]
	BC=word[0]
	D={}
	C=""
	for i in range(1,len(word)):
		C=word[i].split("\t")[0]
		if not D.has_key(C):
			D[C]=word[i]
		else:
			D[C]=D[C]+";"+word[i]
	d=len(D)
	#print d
	N=0
	for k in D:
		if ";" not in D[k]:
			newt1=T1+"-"+"S"
			newt2=T2+"-"+"subGEM"+str(N)
			newtype=newt1+":"+newt2
			newline=newtype+"|"+BC+";"+D[k]
			#print newline
	
			FOUTS.write(newline+"\n")
			
		else:
			USF=D[k].split(";")
			USFD={}
			SFL=[]
			for u in range(len(USF)):
				S=int(USF[u].split("\t")[1])
				USFD[S]=USF[u]
			for v in sorted(USFD,key=int):
				SFL.append(USFD[v])
			SF=";".join(SFL)
			newt1=T1+"-"+"A"
                        newt2=T2+"-"+"subGEM"+str(N)
                        newtype=newt1+":"+newt2
                        newline=newtype+"|"+BC+";"+SF
                        FOUTA.write(newline+"\n")
			#print newline
		N=N+1


"""
$head T20.BCLINE.FRAGMENT_GEMLINE.M.F.E
FCLASS_E_split_2_A.py
M-F-E:fragnumH7F5-fragnumF5-chrnum3
M-F-E|SHG0007H-BX-TTTGTGTAGGCGTAGT;dchr2L	5604950	5605578	2	SHG0007H-BX-TTTGTGTAGGCGTAGT-0007F;dchr2R	3984111	3984696	2	SHG0007H-BX-TTTGTGTAGGCGTAGT-0008F;dchr2R	4298792	4299378	3	SHG0007H-BX-TTTGTGTAGGCGTAGT-0009F;dchr2R	17203924	17204510	1	SHG0007H-BX-TTTGTGTAGGCGTAGT-0010F;dchr3L	17971377	17971947	1	SHG0007H-BX-TTTGTGTAGGCGTAGT-0011F
"""

