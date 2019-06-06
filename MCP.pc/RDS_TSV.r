args=commandArgs(trailingOnly=TRUE)
IN=args[1]
FIN=read.table(IN,header=FALSE,sep="\t")
saveRDS(FIN,paste0(IN,".rds"))


