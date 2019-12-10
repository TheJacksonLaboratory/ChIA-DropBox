"""
chr10	12874346	12874846	DPM6E4.NYBot10_Stg.Odd2Bo1.Even2Bo10.Odd2Bo86
chr10	35797511	35798011	DPM6E4.NYBot10_Stg.Odd2Bo1.Even2Bo20.Odd2Bo94
chr10	100792799	100793299	DPM6E4.NYBot10_Stg.Odd2Bo1.Even2Bo22.Odd2Bo81
"""
import os,sys
IN=sys.argv[1]
FIN=open(IN,"r")
FOUT=open(IN+".BCLCMB","w")
D={}
while True:
	line=FIN.readline()
	if not line:
		break
	word=line.rstrip("\n").split("\t")
	ID=word[3]
	LIB=ID.split(".")[0]
	RGN=word[0]+"\t"+word[1]+"\t"+word[2]	
	if ID not in D:
		D[ID]={RGN:1}
	elif ID in D:
		D[ID][RGN]=1
#print len(D)
lib=LIB
nid=100000000
for id in D:
	grp=nid/10000
	fid=1
	for f in sorted(D[id]):
		#print lib,f,fid,id ,nid,grp
		newfid=lib+"-"+str(grp)+"-"+str(nid)+"-"+id+":"+"TIAN"+":"+str(nid)+":"+str(fid)
		newfrag=f+"\t"+newfid+"\t"+"519"+"\t"+"+"+";"
		FOUT.write(newfrag)
		fid=fid+1
	FOUT.write("\n")
	nid=nid+1
