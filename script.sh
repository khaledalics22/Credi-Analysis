#!/usr/bin/bash
export PDSH_RCMD_TYPE=ssh
stop-all.sh
start-all.sh
/usr/local/hadoop/bin/hadoop dfsadmin -safemode leave
#hadoop fs -mkdir /PyHadoop
#hadoop fs -mkdir /PyHadoop/Input
hdfs dfs -rm -r /PyHadoop/Input/*
hdfs dfs -rm -r /PyHadoop/Output
hdfs dfs -put os_data.csv /PyHadoop/Input
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar -file /home/khalid/Desktop/FY/BDproject/Project/mapper.py -mapper "/home/khalid/Desktop/FY/BDproject/Project/mapper.py 0.3 100" -file ~/Desktop/FY/BDproject/Project/reducer.py -reducer ~/Desktop/FY/BDproject/Project/reducer.py -input /PyHadoop/Input -output /PyHadoop/Output
hdfs dfs -get /PyHadoop/Output/part-00000 ~/Desktop/project/
