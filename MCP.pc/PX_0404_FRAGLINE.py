import os,sys, subprocess,operator
from pybedtools import BedTool
import pybedtools
#IN="TESTBAR.UniqBcRd"
#IN="SHG0008_possorted_bam.bam_with_barcode.bam.F2304.bam.sN.bam.bed.R1.rmHETUM.BCline"
IN=sys.argv[1]
EXT=int(sys.argv[2])
FIN=open(IN,"r")
FOUT=open(IN+".GAPEXT"+str(EXT)+".FRAGMENT_GEMLINE","w")
FOUT2=open(IN+".GAPEXT"+str(EXT)+".FRAGMENT_FRAGLINE","w")

FOUT3=open(IN+".GAPEXT"+str(EXT)+".FRAGMENT_READLINE","w")


#dchrX	7201241	7202315	24	SHG0008H-BX-TTAGTTCCACTTCTTA-FRAG0000	READ-0	dchrX	7201241	7201869	SHG0008H-BX-TTAGTTCCACTTCTTA:K00384:49:HK7T3BBXX:8:1125:31974:26547/1	60	-

READLINE_HEAD="\t".join(["FRAG_CHROM","FRAG_START","FRAG_END","READ_COUNT","FRAG_ID","READ_SERIAL","READ_CHROM","READ_START","READ_END","READ_ID","MAPQ","STRAND"])
FOUT3.write(READLINE_HEAD+"\n")
#SAMPLE="SHG0007-BX1000000000-AAACACCAGAAACCCG"
DRD={}
#EXT=0
while True:
	line=FIN.readline()  ## read in a bar_line
	if not line:
		break
	DID={}
	if ";" not in line: ## if only on BED-READ in the GEM
		#word=line.rstrip("\n")
		word=line.rstrip("\n").split("\t")
		BC=word[3].split(":")[0]
		READ_ID=word[3]
		DID[READ_ID]=line.rstrip("\n")
		MGD=word
		frag_num=BC+"-FRAG0000"
		fragline=MGD[0]+"\t"+str(MGD[1])+"\t"+str(MGD[2])+"\t"+"1"+"\t"+frag_num+"\t"+str(MGD[3])
		newline=BC+";"+MGD[0]+"\t"+str(MGD[1])+"\t"+str(MGD[2])+"\t"+"1"+"\t"+frag_num
		FOUT2.write(fragline+"\n")
		readline=MGD[0]+"\t"+str(MGD[1])+"\t"+str(MGD[2])+"\t"+"1"+"\t"+frag_num+"\tREAD-0\t"+MGD[0]+"\t"+str(MGD[1])+"\t"+str(MGD[3])+"\t"+str(MGD[4])+"\t"+str(MGD[5])
		#print "newline01",newline
		FOUT3.write(readline+"\n")
		FOUT.write(newline+"\n")
		#print "SINGLE_RD/GEM"
	else:  ## ";"in word: if multi-BED-READ in the GEM
		word=line.rstrip("\n").split(";")
		
		BC=word[0].split("\t")[3].split(":")[0]	
		#print "MULTI_RDs/GEM",word
		s=""
		for i in range(len(word)): ## FOR every BED-Read
			KEY=word[i].split("\t")[3]
			DRD[KEY]=word[i]
			DID[KEY]=word[i]
			#print word[i] 
			if s=="":
				s="\t".join(word[i].split(" "))	
			else:
				s=s+"\n"+word[i]
		#print s
		#print len(DRD)
		a=BedTool(s, from_string=True)
		#print a
		#INA=a.sort().intersect(a,wao=True, s=True)
		#print INA
		MGD=a.sort().merge(d=EXT, c=4, o="count,collapse")
		#print "MGD",MGD
		mgdD={}
		#mgd=MGD.split("\n")
		#print "mgd",mgd
		for i in range(len(MGD)):
			C=int(MGD[i][1])
			mgdD[C]=MGD[i]
		mgdL=[]
		for k in sorted(mgdD,key=int):
			mgdL.append(mgdD[k])
		#print mgdL	
		newline=""
		#print len(MGD)	
		for i in range(0,len(mgdL)):
			if i <10:
				I="000"+str(i)
			elif i <100:
				I="00"+str(i)
                        elif i <1000:
                                I="0"+str(i)
			else:
				I=str(i)
			#print I
			frag_num=BC+"-FRAG"+str(I)
			#print "mgdL[i]",mgdL[i]
			d_mdg=mgdL[i][4].split(",")

			READ_LIST=""
			for id in range(len(d_mdg)):
				#print d_mdg[id]
				readline=DID[d_mdg[id]].split("\t")
				newread=readline[0]+":"+readline[1]+"-"+readline[2]+";"+readline[3]+";"+readline[4]+";"+readline[5]
				newreadline="\t".join([readline[0],readline[1],readline[2],readline[3],readline[4],readline[5]])
				#print readline
				if READ_LIST=="":
					READ_LIST=newread
				else:
					READ_LIST=READ_LIST+"\t"+newread					
				readline=mgdL[i][0]+"\t"+str(mgdL[i][1])+"\t"+str(mgdL[i][2])+"\t"+str(mgdL[i][3])+"\t"+frag_num+"\tREAD-"+str(id)+"\t"+newreadline
				FOUT3.write(readline+"\n")
			fragline=mgdL[i][0]+"\t"+str(mgdL[i][1])+"\t"+str(mgdL[i][2])+"\t"+str(mgdL[i][3])+"\t"+frag_num+"\tREADS\t"+READ_LIST
			FOUT2.write(fragline+"\n")
			#print "MGD",MGD[i]	
			if newline=="":
				newline=mgdL[i][0]+"\t"+str(mgdL[i][1])+"\t"+str(mgdL[i][2])+"\t"+str(mgdL[i][3])+"\t"+frag_num
			else:
				newline=newline+";"+mgdL[i][0]+"\t"+str(mgdL[i][1])+"\t"+str(mgdL[i][2])+"\t"+str(mgdL[i][3])+"\t"+frag_num
		#print "newline",BC+";"+newline
		newline=BC+";"+newline
		FOUT.write(newline+"\n")
		DRD={}
		s=""

"""
for j in range(len(INA)): ## for every INTERSECTED_BED-PAIR
			#print "INA",int(INA[j][2])-int(INA[j][1]),int(INA[j][8])-int(INA[j][7]),INA[j][12]
>>> import operator
>>> stats = {'a':1000, 'b':3000, 'c': 100, 'd':3000}
>>> max(stats.iteritems(), key=operator.itemgetter(1))[0]
if 'key' in myDict: del myDict['key']
INA[1] dchrX	19800673	19800800	SHG0007-BX1000000125-AAACACCAGTAGATGT:M03204:199:000000000-B5HRF:1:1101:12400:13288/1	60	+	dchrX	19800559	19800686	SHG0007-BX1000000125-AAACACCAGTAGATGT:M03204:199:000000000-B5HRF:1:1106:25163:11649/1	60	+	13

INA dchrX	19800673	19800800	SHG0007-BX1000000125-AAACACCAGTAGATGT:M03204:199:000000000-B5HRF:1:1101:12400:13288/1	60	+	dchrX	19800673	19800800	SHG0007-BX1000000125-AAACACCAGTAGATGT:M03204:199:000000000-B5HRF:1:1101:12400:13288/1	60	+	127

#a= BedTool(IN)	
#print a.sort()
#print a.sort().merge()
#print a.intersect(a,wao=True)

s='''chr1\t1\t100\nchr1\t25\t800\n'''
a=BedTool(s, from_string=True)
print a.intersect(a,wao=True)

$cat TEST
chr2	48277985	48278086	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:1102:14842:6812/1	60	-
dchr3R	21322589	21322644	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:1106:15591:6869/1	60	+
chr2	48278034	48278139	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:1109:21875:8393/1	60	+
chr2	48277904	48278002	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:1113:15719:22669/1	60	-
chr2	48277894	48277990	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:1114:17462:14190/1	60	-
chr2	48277990	48278118	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:2104:23105:24251/1	60	+
chr2	48277982	48278086	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:2106:25737:8338/1	60	+
chr2	48277983	48278086	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:2106:26884:21549/1	60	+

$head TESTBAR
chr2	48277985	48278086	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:1102:14842:6812/1	60	-;dchr3R	21322589	21322644	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:1106:15591:6869/1	60	+;chr2	48278034	48278139	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:1109:21875:8393/1	60	+;chr2	48277904	48278002	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:1113:15719:22669/1	60	-;chr2	48277894	48277990	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:1114:17462:14190/1	60	-;chr2	48277990	48278118	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:2104:23105:24251/1	60	+;chr2	48277982	48278086	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:2106:25737:8338/1	60	+;chr2	48277983	48278086	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:2106:26884:21549/1	60	+;chr2	48277894	48277993	SHG0007-BX1000000000-AAACACCAGAAACCCG:M03204:199:000000000-B5HRF:1:2111:13155:9548/1	60	+
"""
