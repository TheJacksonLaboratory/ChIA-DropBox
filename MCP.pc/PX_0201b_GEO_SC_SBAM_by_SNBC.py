import os,sys
R=sys.argv[1]
FR=open(R,"r")
D={}
SIG=""
DSET={}
while True:
	line=FR.readline()
	if not line:
		break
	word=line.rstrip("\n").split("-")
	BC=word[3]
	D[BC]=line.rstrip("\n")
	DSET[int(word[1])]=1
import collections,time,os,sys,pysam
IN=sys.argv[2]
LIB=sys.argv[3]

samfile = pysam.Samfile(IN, "rb")
import glob
F0000=pysam.Samfile(LIB+"-00000.SNBC.bam","wb", template=samfile)
DT=[]


for I in sorted(DSET):
	name=LIB+"-"+str(I)
	globals()[name]=pysam.Samfile('%s.SNBC.bam' % name,"wb", template=samfile)

iter = samfile.fetch()
for x in iter:
	TAG=dict(x.tags)
	if TAG.has_key("BX"):
                KBX=TAG["BX"].split("-")[0]+"BX"+TAG["BX"].split("-")[1]
		if not D.has_key(KBX):
			sys.exit("BC error!!")
		else:
			SNBC=D[KBX].split("-")
			SIG=int(SNBC[1])
			name=LIB+"-"+str(SIG)
	                x.qname=LIB+"-"+str(SIG)+"-"+SNBC[2]+"-"+SNBC[3]+"-M02838:130:000000000-BW88R:1:2114:11429:"+x.qname		
              		globals()[name].write(x)
	elif not TAG.has_key("BX"):
                x.qname=LIB+"-000-"+"00000000-NNNNNNNNNNNNNNNN"+"-M02838:130:000000000-BW88R:1:2114:11429:"+x.qname    
                F0000.write(x)


