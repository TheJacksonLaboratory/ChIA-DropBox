OUTSIDE=`pwd`
source ${OUTSIDE}/MCP.conf
ls -l CLEAN_BOX

read -p "Are you sure want to delete all these middle files? (YES/NO) " AN
if [[ $AN = "YES" ]]
then
	echo 'rm -rf CLEAN_BOX/'|qsub -l mem=120gb -d `pwd` -N "CLEAN"
fi
