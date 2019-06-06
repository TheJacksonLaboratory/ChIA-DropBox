import os,sys
#from collections import OrderedDict
"""
$head SHG0019.COMBINED_SA.GENSUB.bsv.gff.fragB2perGEM.gff
chrX	SHG0019-bsv	transcript	3749796	16231230	.	.	.	gene_id=SHG0019-100-1000140-AAACCCATCCTCCTGA-M03204-FA-1-0;transcript_id=SHG0019-100-1000140-AAACCCATCCTCCTGA-M03204-FA-1-0;SPECIES=FLY;TYPE1=F-A;TYPE2=fragnumF3-chrnum1;GEM_REGION=chrX:3749796-16231230;GEM_COV=12481434;GEM_FRAGNUM=3;GEM_READNUM=11;FRAG_LEN_LIST=607,570,556;READ_COUNT_LIST=1,7,3;F2F_DISTANCE_LIST=6610252,5869449,0	chrX:3749796-3750403-1-SHG0019-100-1000140-AAACCCATCCTCCTGA-M03204-FRAG0000;chrX:10360655-10361225-7-SHG0019-100-1000140-AAACCCATCCTCCTGA-M03204-FRAG0001;chrX:16230674-16231230-3-SHG0019-100-1000140-AAACCCATCCTCCTGA-M03204-FRAG0002

$head /Sequence_pool/CTBASIC_DATA/scratch/dm3_UCSC_known_genes.txt
d.name	d.chrom	d.strand	d.txStart	d.txEnd	d.cdsStart	d.cdsEnd	d.exonCount	d.exonStarts	d.exonEnds	d.score	d.kgXref.geneSymbol	d.cdsStartStat	d.cdsEndStat	d.exonFrames	d.kgXref.mRNA
NR_073624	chr4	+	1048488	1049985	1049985	1049985	2	1048488,1049335,	1048508,1049985,	0	CR44031	unk	unk	-1,-1,	CR44031
"""

#IN="SHG0019.COMBINED_SA.GENSUB.bsv.gff.fragB2perGEM.gff"

IN=sys.argv[1]
FIN=open(IN,"r")
FOUT=open(IN+".BASIC","w")
FOUT.write("d.name\td.chrom\td.strand\td.txStart\td.txEnd\td.cdsStart\td.cdsEnd\td.exonStarts\td.exonEnds\td.kgXref.geneSymbol\td.kgXref.mRNA\td.score\n")
while True:
	line=FIN.readline()
	if not line:
		break
	word=line.rstrip("\n").split("\t")
	if word[2]!="transcript":
		continue
	GA=word[8].split(";")
	FL=word[9].split(";")
	LIB=word[1].split("-")[0]
	NBC=GA[0].split("-")[2]
	FRAGNUM=GA[8].split("=")[1]
	SLIST=""
	ELIST=""
	for i in range(len(FL)):
		FRAG=FL[i]
		FC=FRAG.split(":")[0]
		FS=FRAG.split(":")[1].split("-")[0]
		FE=FRAG.split(":")[1].split("-")[1]
		if SLIST=="":
			SLIST=FS
			ELIST=FE
		else:
			SLIST=SLIST+","+FS
                        ELIST=ELIST+","+FE
	td_name=LIB+"_"+NBC
	td_chrom=word[0]
	td_strand="+"
	td_txStart=word[3]
	td_txEnd=word[4]
	td_cdsStart=td_txStart
	td_cdsEnd=td_txEnd
	td_exonStarts=SLIST
	td_exonEnds=ELIST
	td_kgXref_geneSymbol=td_name
	td_kgXref_mRNA=td_name
	td_score=FRAGNUM
	newline="\t".join([td_name,td_chrom,td_strand,td_txStart,td_txEnd,td_cdsStart,td_cdsEnd,td_exonStarts,td_exonEnds,td_kgXref_geneSymbol,td_kgXref_mRNA,td_score])
	#print line
	#print newline


	FOUT.write(newline+"\n")

"""
$head SHG0019.COMBINED_SA.GENSUB.bsv.gff.fragB2perGEM.gff
chrX    SHG0019-bsv     transcript      3749796 16231230        .       .       .       gene_id=SHG0019-100-1000140-AAACCCATCCTCCTGA-M03204-FA-1-0;transcript_id=SHG0019-100-1000140-AAACCCATCCTCCTGA-M03204-FA-1-0;SPECIES=FLY;TYPE1=F-A;TYPE2=fragnumF3-chrnum1;GEM_REGION=chrX:3749796-16231230;GEM_COV=12481434;GEM_FRAGNUM=3;GEM_READNUM=11;FRAG_LEN_LIST=607,570,556;READ_COUNT_LIST=1,7,3;F2F_DISTANCE_LIST=6610252,5869449,0    chrX:3749796-3750403-1-SHG0019-100-1000140-AAACCCATCCTCCTGA-M03204-FRAG0000;chrX:10360655-10361225-7-SHG0019-100-1000140-AAACCCATCCTCCTGA-M03204-FRAG0001;chrX:16230674-16231230-3-SHG0019-100-1000140-AAACCCATCCTCCTGA-M03204-FRAG0002
"""
