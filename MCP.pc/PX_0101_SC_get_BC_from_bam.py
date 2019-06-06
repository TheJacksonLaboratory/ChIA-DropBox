import collections,time,os,sys,pysam


#print len(sys.argv)


IN=sys.argv[1]
#IN="TEST.bam"
NAME=sys.argv[2]
###FIN=pysam.Samfile(IN,"rb")
FBARCODE=open(NAME+".BC","w")

#LIB="SHG0007H"
samfile = pysam.Samfile(IN, "rb")



iter = samfile.fetch()
#S=()
#L=[]
#D={}  ##uniq barcode
for x in iter:
	#print x.tags
	TAG=dict(x.tags)
	if TAG.has_key("BX"):
                KBX=TAG["BX"].split("-")[0]+"BX"+TAG["BX"].split("-")[1]
		#print KBX
#		L.append(KBX)
		FBARCODE.write(KBX+"\n")
#BX:Z:ACGATCAAGGTGTAGC-15
#samfile.close()
#print len(L),L
#S=sorted(set(L))
#print len(S),S


#D=dict.fromkeys(S,0)
#print D

"""
TAG=dict(a.tags)
	if TAG.has_key("BX"):
		KBX=TAG["BX"].rstrip("-1")
		if not D.has_key(KBX):
			break
			print "ERROR"
		a.qname=D[KBX]+":"+a.qname
		FWITH.write(a)
	elif not TAG.has_key("BX"):
		new_head=str(lib)+"-"+"BX"+"0"+"-"+"NO10XBARCODE"
		a.qname=new_head+":"+a.qname	
		FWITHOUT.write(a)
TAG=dict(a.tags)
        if TAG.has_key("BX"):
                KBX=TAG["BX"].rstrip("-1")
a = pysam.AlignedSegment()
    a.query_name = "read_28833_29006_6945"
    a.query_sequence="AGCTTAGCTAGCTACCTATATCTTGGTCTTGGCCG"
    a.flag = 99
    a.reference_id = 0
    a.reference_start = 32
    a.mapping_quality = 20
    a.cigar = ((0,10), (2,1), (0,25))
    a.next_reference_id = 0
    a.next_reference_start=199
    a.template_length=167
    a.query_qualities = pysam.qualitystring_to_array("<<<<<<<<<<<<<<<<<<<<<:<9/,&,22;;<<<")
    a.tags = (("NM", 1),
              ("RG", "L1"))
"""
