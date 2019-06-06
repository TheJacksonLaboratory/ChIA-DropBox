if (!require("ggplot2")) install.packages("ggplot2", repos = "http://cran.us.r-project.org")
if (!require("gridExtra")) install.packages("gridExtra", repos = "http://cran.us.r-project.org")
if (!require("dplyr")) install.packages("dplyr", repos = "http://cran.us.r-project.org")
if (!require("sitools")) install.packages("sitools", repos = "http://cran.us.r-project.org")
if (!require("scales")) install.packages("scales", repos = "http://cran.us.r-project.org")
args = commandArgs(trailingOnly=TRUE)
LIB=args[1]
IN=paste0("P11.",LIB,"_COMBINED_SA.SUBGEM.bsv.gff.GEMLINE_OUT.tsv")
FIN=read.table(IN,header=TRUE)
FIN$len<-FIN$GEM_FRAGNUM
SIN<-FIN%>%filter(len>1)
MX=round(max(FIN$len))
MXPOS=paste0("max(x) = ",MX)
TITLE=paste0("PLOT.2022.",LIB,".GEM.fragment")
PLOTNAME=paste0(TITLE,".png")
png(PLOTNAME, 400,400)
ggplot(FIN,aes(len))+
    stat_ecdf(geom = "step",color="darkgreen",size=1)+
#    stat_ecdf(data=SIN,geom = "step",color="green",size=1)+
  theme_bw(base_size=20)+
  xlab("fragment_count/GEM")+
  ggtitle(paste0(TITLE," \n ",MXPOS))+
  ylab("Percent of GEM count")+
  scale_x_continuous(breaks=seq(1,15,1),limits=c(1,15))+

  scale_y_continuous(labels=percent) +
 theme(panel.grid = element_blank(),
        legend.position="none",
	plot.title = element_text(size = 15, face = "bold")
  )

dev.off()

