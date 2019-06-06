import os,sys
IN=sys.argv[1]
FIN=open(IN,"r")
FOUT=open(IN+".SUBGEM","w")
while True:
	line=FIN.readline()
	if not line:
		break
	word=line.rstrip("\n").split(";")
	T1=word[0].split(":")[0]
	T2=word[0].split(":")[1].split("|")[0]
	Dt2={}
	t2=T2.split("-")
	for i in range(len(t2)):
		Dt2[t2[i]]=1
	t2_cnm=""
	t2_sub=""
	for k in Dt2:
		if k.startswith("chrnum"):
			t2_cnm=k.split("chrnum")[1]
		if k.startswith("subGEM"):
			t2_sub=k.split("subGEM")[1]
	#print t2_cnm,t2_sub,line
	if t2_cnm!="" and t2_sub!="":
		newt2=t2_cnm+"-"+t2_sub
	elif t2_cnm!="" and t2_sub=="":
		newt2=t2_cnm+"-0"
	elif t2_cnm=="" and t2_sub=="":
		newt2="0-0"
	else:
		sys.exit("ERROR at subGEM")	
	BC=word[0].split(":")[1].split("|")[1]
	FRAGS=""
	for i in range(1,len(word)):
		if FRAGS=="":
			FRAGS=word[i]
		else:
			FRAGS=FRAGS+";"+word[i]
	t1=T1.split("-")
	GP=""
	for i in range(len(t1)):
		if GP=="":
			GP=t1[i]	
		else:
			GP=GP+t1[i]
	#print GP,FRAGS
	#print line
	newline=";".join([T1,T2,BC+"-"+GP+"-"+newt2,FRAGS])
	#print newline
	#print line
	#print "##############"
	FOUT.write(newline+"\n")

"""
M-H-E-A:fragnumH7F5-fragnumH7-chrnum6-subGEM4|SHG0008H-BX-TTAGTTCCACTTCTTA;chr12	67753344	67753972	1	SHG0008H-BX-TTAGTTCCACTTCTTA-FRAG0006;chr12	116755692	1
$head SHG0008H205.combined.TOTAL_GEM.sorted
M-F-E-A;fragnumH7F5-fragnumF5-chrnum3-subGEM0;SHG0008H-BX-TTAGTTCCACTTCTTA;dchrX	7201241	7202315	24	SHG0008H-BX-TTAGTTCCACTTCTTA-FRAG0000;dchrX	11099223	11099851	1SHG0008H-BX-TTAGTTCCACTTCTTA-FRAG0003
M-F-E-A;fragnumH7F5-fragnumF5-chrnum3-subGEM1;SHG0008H-BX-TTAGTTCCACTTCTTA;dchr2L	7896024	7896853	78	SHG0008H-BX-TTAGTTCCACTTCTTA-FRAG0001;dchr2L	8030472	8031101	1	SHG0008H-BX-TTAGTTCCACTTCTTA-FRAG0002

"""
