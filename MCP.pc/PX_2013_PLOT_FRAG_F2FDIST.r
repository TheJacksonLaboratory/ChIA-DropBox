if (!require("ggplot2")) install.packages("ggplot2", repos = "http://cran.us.r-project.org")
if (!require("gridExtra")) install.packages("gridExtra", repos = "http://cran.us.r-project.org")
if (!require("dplyr")) install.packages("dplyr", repos = "http://cran.us.r-project.org")
if (!require("sitools")) install.packages("sitools", repos = "http://cran.us.r-project.org")
if (!require("scales")) install.packages("scales", repos = "http://cran.us.r-project.org")
args = commandArgs(trailingOnly=TRUE)
LIB=args[1]
IN=paste0("P10.",LIB,"_COMBINED_SA.SUBGEM.bsv.gff.FRAGLINE_OUT.tsv")
FIN=read.table(IN,header=TRUE)
FIN$len<-FIN$F2F_DISTANCE
FIN<-FIN%>%filter(FIN$len>0)
#colnames(FIN)<-c("chr","start","end","name","len")
#head(FIN)
#str(FIN)
    MX=round(density(FIN$len)$x[which.max(density(FIN$len)$y)])
MXPOS=paste0("max(density)$x = ",MX)


TITLE=paste0("PLOT.2013.",LIB,".FRAG.F2FDIST")
PLOTNAME=paste0(TITLE,".png")
png(PLOTNAME, 400,400)
ggplot(FIN,aes(len))+
  geom_density(aes(y=..scaled..),size=1,color="navy")+
  theme_bw(base_size=20)+
  xlab("log10 FRAG.F2FDIST  (bp))")+
  ggtitle(paste0(TITLE))+
  ylab("scaled density")+
#  scale_x_continuous(limits=c(0,10000000),breaks=c(100,10000,100000,10000000,1000000,MXPOS))+  
#scale_x_log10(labels=f2si,breaks=c(0,1,100,10000,100000,10000000,1000000,100000000,1000000000))+
  scale_x_log10(breaks=c(500,10^seq(0,8,2),10000000),labels=f2si,limits=c(500,1000000000))+
  theme(panel.grid = element_blank(),
        legend.position="none",
	plot.title = element_text(size = 15, face = "bold")
  )
dev.off()

