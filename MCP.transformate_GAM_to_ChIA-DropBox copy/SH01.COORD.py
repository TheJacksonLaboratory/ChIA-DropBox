"""
chrom chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 chr1 ch
start 0 1000000 2000000 3000000 4000000 5000000 6000000 7000000 8000000 9000000 10000000 11000000 12000000 13000000 14000000 15000000 16000000 17000000 18000000 1900000
stop 1000000 2000000 3000000 4000000 5000000 6000000 7000000 8000000 9000000 10000000 11000000 12000000 13000000 14000000 15000000 16000000 17000000 18000000 19000000 2
F10A2 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 1 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
F10A3 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 1 1 1 0 0 1 1 1 1 1 1 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
F10A4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
F10A5 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 1 1 0 0 1 1 1
F10A6 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
F10B1 0 0 0 0
"""
IN="GSE64881_segmentation_at_30000bp.passqc.multibam.txt.transposed"
#IN="GSE64881_segmentation_at_1000000bp.passqc.multibam.txt.transposed"
FIN=open(IN,"r")
FOUT=open(IN+".chrcmb","w")
DC={}
DS={}
DE={}
while True:
	line=FIN.readline()
	if not line:
		break
	word=line.rstrip("\n").split(" ")
	#print len(word)
	if word[0]=="chrom":
		for i in range(1,len(word)):
			DC[i]=word[i]
	elif word[0]=="start":
                for i in range(1,len(word)):
                        DS[i]=word[i]
	elif word[0]=="stop":
                for i in range(1,len(word)):
                        DE[i]=word[i]
	
	else:
		ID=word[0]
		for i in range(1,len(word)):
			BIN=int(word[i])
			if BIN==1:
				newline="\t".join([DC[i],DS[i],DE[i],ID])
				#print newline		
				FOUT.write(newline+"\n")
