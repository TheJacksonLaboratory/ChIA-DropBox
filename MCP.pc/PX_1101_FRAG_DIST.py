import os,sys
IN=sys.argv[1]
#IN="SHG0021N.COMBINED_SA.GENSUB.bsv.gff.GEMLINE_OUT.tsv"
FIN=open(IN,"r")
D1=0
D2=0
D3=0
D4=0
D5=0
D6=0
D7=0
D8=0
D9=0
D10=0
D11=0
D12=0
D13=0
D14=0
D15t19=0
D20t29=0
D30t39=0
D40t49=0
D50t99=0
D100t199=0
D200t499=0
D500t999=0
D1000up=0
while True:
	line=FIN.readline()
	if not line:
		break
	if line.startswith("GEM_ID"):
	
		continue
	word=line.rstrip("\n").split("\t")
	FN=int(word[5])
	if FN==1:
		D1=D1+1
	elif FN==2:
		D2=D2+1
	elif FN==3:
                D3=D3+1
        elif FN==4:
                D4=D4+1
        elif FN==5:
                D5=D5+1
        elif FN==6:
                D6=D6+1
        elif FN==7:
                D7=D7+1
        elif FN==8:
                D8=D8+1
        elif FN==9:
                D9=D9+1
        elif FN==10:
                D10=D10+1
        elif FN==11:
                D11=D11+1
        elif FN==12:
                D12=D12+1
        elif FN==13:
                D13=D13+1
        elif FN==14:
                D14=D14+1
        elif FN>=15 and FN <=19:
                D15t19=D15t19+1
        elif FN>=20 and FN <=29:
                D20t29=D20t29+1
        elif FN>=30 and FN <=39:
                D30t39=D30t39+1
        elif FN>=40 and FN<=49:
                D40t49=D40t49+1
        elif FN>=50 and FN <=99:
                D50t99=D50t99+1
        elif FN>=100 and FN<=199:
                D100t199=D100t199+1
        elif FN>=200 and FN <=499:
                D200t499=D200t499+1
        elif FN>=500 and FN<=999:
                D500t999=D500t999+1
        elif FN>=1000:
                D1000up=D1000up+1

newline="\n".join([str(D1),str(D2),str(D3),str(D4),str(D5),str(D6),str(D7),str(D8),str(D9),str(D10),str(D11),str(D12),str(D13),str(D14),str(D15t19),str(D20t29),str(D30t39),str(D40t49),str(D50t99),str(D100t199),str(D200t499),str(D500t999,),str(D1000up)])
#print newline
#OUT=sys.argv[2]
FOUT=open("G08_GEM_FRAGNUM_DIST.sta","w")
FOUT.write(newline+"\n")
	

"""
$head SHG0021N.COMBINED_SA.GENSUB.bsv.gff.GEMLINE_OUT.tsv
GEM_ID	SPECIES	TRACC_BACK	GEM_REGION	GEM_COV	GEM_FRAGNUM	GEM_READNUM	FRAG_LEN_LIST	READ_COUNT_LIST	F2F_DISTANCE_LIST
SHG0021N-10000-100000001-AAACACCAGAAACCCG-NS500460-FA-1-0	FLY	fragnumF2-chrnum1	chr3R:6104253-26137708	20033455	2	2	128,95	1,1	20033232,0
SHG0021N-10000-100000013-AAACACCAGAAGCTCG-NS500460-FA-1-0	FLY	fragnumF2-chrnum1	chr3R:8397997-9204746	806749	2	22	159,300	2,20	806290,0
SHG0021N-10000-100000017-AAACACCAGAATATGC-NS500460-FA-1-0	FLY	fragnumF2-chrnum1	chr2L:6104487-16268537	10164050	2	4	75,120	1,3	10163855,0
SHG0021N-10000-100000022-AAACACCAGACAATAC-NS500460-FA-1-0	FLY	fragnumF2-chrnum1	chr3R:629952-17438571	16808619	2	3	56,106	2,1	16808457,0
SHG0021N-10000-100000038-AAACACCAGACTTCTG-NS500460-FA-1-0	FLY	fragnumF2-chrnum1	chrX:12629537-12629742	205	2	3	139,61	2,1	5,0
SHG0021N-10000-100000041-AAACACCAGAGAGCAA-NS500460-FA-1-0	FLY	fragnumF2-chrnum1	chr2L:176210-176380	170	2	2	80,74	1,1	16,0
"""
