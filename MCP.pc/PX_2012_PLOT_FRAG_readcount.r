if (!require("ggplot2")) install.packages("ggplot2", repos = "http://cran.us.r-project.org")
if (!require("gridExtra")) install.packages("gridExtra", repos = "http://cran.us.r-project.org")
if (!require("dplyr")) install.packages("dplyr", repos = "http://cran.us.r-project.org")
if (!require("sitools")) install.packages("sitools", repos = "http://cran.us.r-project.org")
if (!require("scales")) install.packages("scales", repos = "http://cran.us.r-project.org")
args = commandArgs(trailingOnly=TRUE)
LIB=args[1]
IN=paste0("P10.",LIB,"_COMBINED_SA.SUBGEM.bsv.gff.FRAGLINE_OUT.tsv")
FIN=read.table(IN,header=TRUE)
FIN$len<-FIN$READ_COUNT
MX=round(max(FIN$len))
MXPOS=paste0("max(x) = ",MX)

TITLE=paste0("PLOT.2012.",LIB,".FRAG.readcount")
PLOTNAME=paste0(TITLE,".png")
png(PLOTNAME, 400,400)
ggplot(FIN,aes(len))+
    stat_ecdf(geom = "step",color="navy",size=1)+
#    stat_ecdf(data=filter(FIN,len>1),geom = "step",color="blue",size=1)+
#geom_density(aes(y=..count..),color="navy")+
  theme_bw(base_size=20)+
  xlab("log10(read _count/fragment)")+
  ggtitle(paste0(TITLE," \n ",MXPOS))+
  ylab("Percent of Fragment count")+
	scale_x_continuous(breaks=seq(1,15,1),limits=c(1,15))+
  scale_y_continuous(limits=c(0,1), labels=percent) +
 theme(panel.grid = element_blank(),
        legend.position="none",
	plot.title = element_text(size = 15, face = "bold")
  )
dev.off()

