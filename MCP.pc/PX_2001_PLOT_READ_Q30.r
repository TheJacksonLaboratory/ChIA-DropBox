if (!require("ggplot2")) install.packages("ggplot2", repos = "http://cran.us.r-project.org")
if (!require("gridExtra")) install.packages("gridExtra", repos = "http://cran.us.r-project.org")
args = commandArgs(trailingOnly=TRUE)
LIB=args[1]
IN=paste0("P01_CMB.",LIB,".R1.q30.bed")
#IN="P01_CMB.SHG0085.R1.q30.bed"
FIN=read.table(IN)
colnames(FIN)<-c("chr","start","end","name","len")
#head(FIN)
MX=round(density(FIN$len)$x[which.max(density(FIN$len)$y)])
MXPOS=paste0("max(density)$x = ",MX)


TITLE=paste0("PLOT.2001.",LIB,".R1.Q30.size")
PLOTNAME=paste0(TITLE,".png")
png(PLOTNAME, 400,400)

ggplot(FIN,aes(len))+
  geom_density(aes(y=..scaled..),size=1)+
  theme_bw(base_size=20)+
  xlab("R1.Q30 read size (bp)")+
  ggtitle(paste0(TITLE," \n ",MXPOS))+
  ylab("scaled density")+
  #ggtitle(LIB61)+
  scale_x_continuous(limits=c(0,800))+
  theme(panel.grid = element_blank(),
        legend.position="none",
	plot.title = element_text(size = 15, face = "bold")
  )
dev.off()

