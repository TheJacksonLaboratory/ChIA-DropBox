if (!require("ggplot2")) install.packages("ggplot2",repos = "http://cran.us.r-project.org")
if (!require("gridExtra")) install.packages("gridExtra", repos = "http://cran.us.r-project.org")
if (!require("dplyr")) install.packages("dplyr", repos = "http://cran.us.r-project.org")
if (!require("sitools")) install.packages("sitools", repos = "http://cran.us.r-project.org")
if (!require("scales")) install.packages("scales", repos = "http://cran.us.r-project.org")

args = commandArgs(trailingOnly=TRUE)
LIB=args[1]
IN=paste0("P10.",LIB,"_COMBINED_SA.SUBGEM.bsv.gff.FRAGLINE_OUT.tsv")
FIN=read.table(IN,header=TRUE)
FIN$len<-FIN$FRAG_LEN
#colnames(FIN)<-c("chr","start","end","name","len")
#head(FIN)
#str(FIN)
MX=round(density(FIN$len)$x[which.max(density(FIN$len)$y)])
MXPOS=paste0("max(density)$x = ",MX)


TITLE=paste0("PLOT.2011.",LIB,".FRAG.size")
PLOTNAME=paste0(TITLE,".png")
png(PLOTNAME, 400,400)

ggplot(FIN,aes(len))+
	geom_density(aes(y=..scaled..),size=1,color="navy")+
  theme_bw(base_size=20)+
  xlab("fragment size (bp)")+
  ggtitle(paste0(TITLE," \n ",MXPOS))+
  ylab("scaled density")+
  #ggtitle(LIB61)+
  scale_x_continuous(limits=c(0,800))+

  theme(panel.grid = element_blank(),
        legend.position="none",
	plot.title = element_text(size = 15, face = "bold")
  )
dev.off()

