"""
$head SHG0026.COMBINED_SA.GENSUB.bsv.gff.fragB2perGEM.gff.BASIC
d.name	d.chrom	d.strand	d.txStart	d.txEnd	d.cdsStart	d.cdsEnd	d.exonStarts	d.exonEnds	d.kgXref.geneSymbol	d.kgXref.mRNA	d.score
SHG0026_10000274	chr2L	+	4316227	18040354	4316227	18040354	4316227,8690145,18039759	4316855,8690770,18040354	SHG0026_10000274	SHG0026_10000274	3
SHG0026_10000991	chr3R	+	4662284	25223448	4662284	25223448	4662284,25219386,25219974,25221671,25222820	4663164,25219954,25221016,25222526,25223448	SHG0026_10000991	SHG0026_10000991	9
SHG0026_10001322	chr3R	+	15436057	15440151	15436057	15440151	15436057,15438339,15439324	15436685,15438919,15440151	SHG0026_10001322	SHG0026_10001322	4
"""

import os,sys
IN=sys.argv[1]
GATE=int(sys.argv[2])
#IN="TEST"
#IN="SHG0026.COMBINED_SA.GENSUB.bsv.gff.fragB2perGEM.gff.BASIC"
FIN=open(IN,"r")
#GATE=2000000
FOUT=open(IN+".SE"+str(GATE)+"_F2F","w")
while True:
	line=FIN.readline()
	if not line:
		break
	word=line.rstrip("\n").split("\t")
	if line.startswith("d.name"):
		newline=line
		FOUT.write(newline)
		continue
	SS=word[7].split(",")
	SE=word[8].split(",")
	NSS=""
	NSE=""
	mm=0
	MM=0
	for i in range(1,len(SS)):
		if int(SS[i])-int(SE[i-1]) > GATE and i == len(SS)-1:
			if NSS=="" and  NSS=="":
                                NSS=SS[i-1];NSE=SE[i-1]
                        else:
                                NSS=NSS+","+SS[i-1];NSE=NSE+","+SE[i-1]
			if "," not in NSS and "," not in NSE:
				mm=NSS; MM=NSE
			else:
				mm=NSS.split(",")[0]
				MM=NSE.split(",")[len(NSE.split(","))-1]
			##print "len(SS)=",len(SS),"i=",i,"SS[i]=",SS[i],"SE[i-1]=",SE[i-1],"DIST=",int(SS[i])-int(SE[i-1]),"BIGEND-BEFORE","NSS=",NSS,"NSE=",NSE,"mm=",mm,"MM=",MM
			if "," not in NSS and "," not in NSE:
				NEWSCORE=1
			else:
				NEWSCORE=len(NSS.split(","))
			newline="\t".join([ word[0],word[1],word[2],mm,MM,mm,MM,NSS,NSE,word[9],word[10],str(NEWSCORE) ])
			FOUT.write(newline+"\n")
                        mm=SS[len(SS)-1]
                        MM=SE[len(SS)-1]
			##print "len(SS)=",len(SS),"i=",i,"SS[i]=",SS[i],"SE[i-1]=",SE[i-1],"DIST=",int(SS[i])-int(SE[i-1]),"BIGEND_END","FINS=",SS[len(SS)-1],"FINE=",SE[len(SS)-1],"mm=",mm,"MM=",MM
			##print line				
			if "," not in SS[len(SS)-1] and "," not in SE[len(SS)-1]:
                                NEWSCORE=1
                        else:
                                NEWSCORE=len(NSS.split(","))
                        newline="\t".join([ word[0],word[1],word[2],mm,MM,mm,MM,SS[len(SS)-1],SE[len(SS)-1],word[9],word[10],str(NEWSCORE) ])
                        FOUT.write(newline+"\n")
		elif int(SS[i])-int(SE[i-1]) > GATE and i != len(SS)-1:
			if NSS=="" and  NSS=="":
                                NSS=SS[i-1];NSE=SE[i-1]
                        else:
                                NSS=NSS+","+SS[i-1];NSE=NSE+","+SE[i-1]
                        if "," not in NSS and "," not in NSE:
                                mm=NSS; MM=NSE
                        else:
                                mm=NSS.split(",")[0]
                                MM=NSE.split(",")[len(NSE.split(","))-1]
			##print "len(SS)=",len(SS),"i=",i,"SS[i]=",SS[i],"SE[i-1]=",SE[i-1],"DIST=",int(SS[i])-int(SE[i-1]),"BIG","NSS=",NSS,"NSE=",NSE,"mm=",mm,"MM=",MM
			if "," not in NSS and "," not in NSE:
                                NEWSCORE=1
                        else:
                                NEWSCORE=len(NSS.split(","))
                        newline="\t".join([ word[0],word[1],word[2],mm,MM,mm,MM,NSS,NSE,word[9],word[10],str(NEWSCORE) ])
                        FOUT.write(newline+"\n")
			NSS=""
		        NSE=""
		elif i == len(SS)-1:
			if NSS=="" and  NSS=="":
                                NSS=SS[i-1];NSE=SE[i-1]
                        else:
                                NSS=NSS+","+SS[i-1];NSE=NSE+","+SE[i-1]
			NSS=NSS+","+SS[i];NSE=NSE+","+SE[i]
			if "," not in NSS and "," not in NSE:
                                mm=NSS; MM=NSE
                        else:
                                mm=NSS.split(",")[0]
                                MM=NSE.split(",")[len(NSE.split(","))-1]
			##print "len(SS)=",len(SS),"i=",i,"SS[i]=",SS[i],"SE[i-1]=",SE[i-1],"DIST=",int(SS[i])-int(SE[i-1]),"END","NSS=",NSS,"NSE=",NSE,"mm=",mm,"MM=",MM
			##print line
			if "," not in NSS and "," not in NSE:
                                NEWSCORE=1
                        else:
                                NEWSCORE=len(NSS.split(","))
                        newline="\t".join([ word[0],word[1],word[2],mm,MM,mm,MM,NSS,NSE,word[9],word[10],str(NEWSCORE) ])
                        FOUT.write(newline+"\n")
		elif i != len(SS)-1:
			if NSS=="" and  NSS=="":
				NSS=SS[i-1];NSE=SE[i-1]
			else:
				NSS=NSS+","+SS[i-1];NSE=NSE+","+SE[i-1]
			###print "len(SS)=",len(SS),"i=",i,"SS[i]=",SS[i],"SE[i-1]=",SE[i-1],"DIST=",int(SS[i])-int(SE[i-1]),"MID","NSS=",NSS,"NSE=",NSE
			###print line
		

	##print "##############################"
