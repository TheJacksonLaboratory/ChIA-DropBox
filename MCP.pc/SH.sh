rm PLOT.*.png
LIB=SHG0085
Rscript PX_2001_PLOT_READ_Q30.r ${LIB}
Rscript PX_2002_PLOT_READ_BE50.r ${LIB}
Rscript PX_2004_PLOT_READ_3E500.r ${LIB}
Rscript PX_2011_PLOT_FRAG_len.r ${LIB}
Rscript PX_2012_PLOT_FRAG_readcount.r  ${LIB}
Rscript PX_2013_PLOT_FRAG_F2FDIST.r ${LIB}
Rscript PX_2021_PLOT_GEM_cov.r ${LIB}
Rscript PX_2022_PLOT_GEM_fragcount.r  ${LIB}
Rscript PX_2023_PLOT_GEM_readcount.r  ${LIB}
Rscript PX_2031_PLOT_GEM_FNSPC_cov.r ${LIB}
Rscript PX_2032_LOOP_FNSPE_span.r ${LIB}
Rscript PX_2033_PLOT_FRAG_FNSPE_F2FDIST.r ${LIB}
wait
convert PLOT.*.png ${LIB}.QCPLOT.pdf
pwd
ls -l PLOT.*.png ${LIB}.QCPLOT.pdf
