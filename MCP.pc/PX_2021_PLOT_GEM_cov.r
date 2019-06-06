if (!require("ggplot2")) install.packages("ggplot2", repos = "http://cran.us.r-project.org")
if (!require("gridExtra")) install.packages("gridExtra", repos = "http://cran.us.r-project.org")
if (!require("dplyr")) install.packages("dplyr", repos = "http://cran.us.r-project.org")
if (!require("sitools")) install.packages("sitools", repos = "http://cran.us.r-project.org")
if (!require("scales")) install.packages("scales", repos = "http://cran.us.r-project.org")
args = commandArgs(trailingOnly=TRUE)
LIB=args[1]
IN=paste0("P13.",LIB,"_COMBINED_SA.SUBGEM.bsv.gff.GEMLINE_OUT.tsv.BE2_FRAGNUM")
FIN=read.table(IN,header=TRUE)
FIN$len<-FIN$GEM_COV
MX=round(density(FIN$len)$x[which.max(density(FIN$len)$y)])
MXPOS=paste0("max(density)$x = ",MX)

TITLE=paste0("PLOT.2021.",LIB,".GEM_FNBE2.coverage")
PLOTNAME=paste0(TITLE,".png")
png(PLOTNAME, 400,400)

ggplot(FIN,aes(len))+
	geom_density(aes(y=..scaled..),size=1,color="darkgreen")+
	#scale_color_manual(values=c("darkgreen","green"))+
        #geom_density(data=filter(FIN,GEM_FRAGNUM>=2),aes(y=..scaled..),size=1,color="green")+
  theme_bw(base_size=20)+
  xlab("GEM(BE2) coverage size (bp)")+
  ggtitle(paste0(TITLE," \n ",MXPOS))+
  ylab("scaled density")+
  #ggtitle(LIB61)+
  #scale_x_continuous(limits=c(500,700))+
#scale_x_log10(labels=f2si,breaks=c(0,1,100,10000,100000,10000000,1000000,100000000,1000000000))+ 
  scale_x_log10(breaks=c(500,10^seq(0,8,2),10000000),labels=f2si,limits=c(500,1000000000))+
  theme(panel.grid = element_blank(),
        legend.position="bottom",
	plot.title = element_text(size = 15, face = "bold")
  )
dev.off()

