
import os,sys
IN=sys.argv[1]

#IN="SHG0021N.GAPEXT0.COMBINED_SA.GENSUB.bsv.gff.GEMLINE_OUT.tsv.NEWBC.all_lib.headed.BE2_FRAGNUM.Fragnum_PlinePgem"
FIN=open(IN,"r")
FOUT=open(IN+".PlinePgemSimp","w")
HEAD="\t".join(["GEM_ID","GEM_coordinate","GEM_span","Fragment_number","List_of_fragment_coordinates"])
FOUT.write(HEAD+"\n")
while True:
	line=FIN.readline()
	if not line:
		break
	word=line.rstrip("\n").split("\t")
	OID=word[0].split("|")[1].split("-")
	GEMID="-".join([ OID[0],OID[2],OID[3],OID[5],OID[6],OID[7] ])
	#SHG0022N-1000-10000001-AAACACCAGAAACCCGBX22N-NS500460-FA-1-0		
	#SHG0008H-1000-10006376-AAACGGGAGAGCGAAA-K00384-FA-1-0
	GEM_RGN=word[3]
	GEM_COV=word[4]
	FRAGNUM=word[5]
	READNUM=word[6]
	FRAGLIST=word[0].split("|")[0]
	newline="\t".join([GEMID,GEM_RGN,GEM_COV,FRAGNUM,FRAGLIST])
	#print newline
	FOUT.write(newline+"\n")





