if (!require("ggplot2")) install.packages("ggplot2", repos = "http://cran.us.r-project.org")
if (!require("gridExtra")) install.packages("gridExtra", repos = "http://cran.us.r-project.org")
library(ggplot2)
library(gridExtra)
args = commandArgs(trailingOnly=TRUE)
LIB=args[1]
IN=paste0("P04_CMB.",LIB,".R1.q30.lenBE50.MAJOR_CHROM.3E500.bed")
FIN=read.table(IN)
colnames(FIN)<-c("chr","start","end","name","len")
#head(FIN)
#str(FIN)
 MX=round(density(FIN$len)$x[which.max(density(FIN$len)$y)])
MXPOS=paste0("max(density)$x = ",MX)


TITLE=paste0("PLOT.2004.",LIB,".R1.Q30.BE50.MC.3E500.")
PLOTNAME=paste0(TITLE,".png")
png(PLOTNAME, 400,400)

ggplot(FIN,aes(len))+
geom_density(aes(y=..scaled..),size=1)+
  theme_bw(base_size=20)+
  xlab("R1.Q30.BE50.MC.3E500 read size (bp)")+
  ggtitle(paste0(TITLE," \n ",MXPOS))+
  ylab("scaled density")+
  #ggtitle(LIB61)+
  scale_x_continuous(limits=c(0,800))+

  theme(panel.grid = element_blank(),
        legend.position="none",
	plot.title = element_text(size = 13, face = "bold")
  )
dev.off()

