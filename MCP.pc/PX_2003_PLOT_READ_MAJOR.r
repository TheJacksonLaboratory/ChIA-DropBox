if (!require("ggplot2")) install.packages("ggplot2")
if (!require("gridExtra")) install.packages("gridExtra")
if (!require("dplyr")) install.packages("dplyr")
if (!require("sitools")) install.packages("sitools")
if (!require("scales")) install.packages("scales")
args = commandArgs(trailingOnly=TRUE)
LIB=args[1]
IN=paste0("P03_CMB.",LIB,".R1.q30.lenBE50.MAJOR_CHROM.bed")
FIN=read.table(IN)
colnames(FIN)<-c("chr","start","end","name","len")
#head(FIN)
MX=round(density(FIN$len)$x[which.max(density(FIN$len)$y)])
MXPOS=paste0("max(density)$x = ",MX)


TITLE=paste0("PLOT.2003.",LIB,".R1.Q30.BE50.MCHR")
PLOTNAME=paste0(TITLE,".png")
png(PLOTNAME, 400,400)

ggplot(FIN,aes(len))+
geom_density(aes(y=..scaled..),size=1)+
  theme_bw(base_size=20)+
  xlab("R1.Q30.BE50.MCHR read size (bp)")+
  ggtitle(paste0(TITLE," \n ",MXPOS))+
  ylab("scaled density")+
  #ggtitle(LIB61)+
  scale_x_continuous(limits=c(0,800))+
  theme(panel.grid = element_blank(),
        legend.position="none",
	plot.title = element_text(size = 15, face = "bold")
  )
dev.off()

