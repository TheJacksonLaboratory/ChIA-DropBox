import os,sys

EXT5=0
EXT3=500
R=sys.argv[1]  ## chrom size  
#R="/Sequence_pool/CTBASIC_DATA/genome/size/dm3.txt"
#R="/Sequence_pool/CTBASIC_DATA/genome/size/hg19_dm3.txt"
D={}
FR=open(R,"r")
while True:
        line=FR.readline()
        if not line:
                break
        word=line.rstrip("\n").split("\t")
	D[word[0]]=word[1]
#print D
IN=sys.argv[2]
FIN=open(IN,"r")
FOUT=open(IN+".5e"+str(EXT5)+"_3e"+str(EXT3)+".EXT","w")
while True:
	line=FIN.readline()
	if not line:
		break
	word=line.rstrip("\n").split("\t")
	S=word[1]
	E=word[2]
	C=word[0]		
	EXTS=int(S)-int(EXT5)
	EXTE=int(E)+int(EXT3)
	if EXTS < 0:
		EXTS=0
	#print EXTS,EXTE,line
	if C not in D:
		print "strang chrom: ",C
		continue
	if EXTE > D[C]:
		EXTE=D[C]

	#print EXTS,EXTE,line
	newline=C+"\t"+str(EXTS)+"\t"+str(EXTE)+"\t"+word[3]+"\t"+word[4]+"\t"+word[5]
	FOUT.write(newline+"\n")


"""
$head SHG0005N_possorted_bam.bam_with_barcode.bam.F2304.sN.bam.bed.R1.rmHETUM.BE50bp
chr2	39942509	39942637	SHG0005N-BX1000000000-AAACACCAGAAACCAT:NS500460:275:HYCVKBGX2:1:12208:25610:13497/1	60	-
chr11	27230402	27230508	SHG0005N-BX1000000000-AAACACCAGAAACCAT:NS500460:275:HYCVKBGX2:4:21605:18907:4780/1	60	+
chr2	33141549	33141600	SHG0005N-BX1000000001-AAACACCAGAAACCCG:NS500460:275:HYCVKBGX2:1:13112:8815:8211/1	1	+
chr2	33141549	33141599	SHG0005N-BX1000000001-AAACACCAGAAACCCG:NS500460:275:HYCVKBGX2:1:13201:8847:19415/1	2	+
chr2	33141552	33141613	SHG0005N-BX1000000001-AAACACCAGAAACCCG:NS500460:275:HYCVKBGX2:1:21101:12733:8624/1	0	+
"""




