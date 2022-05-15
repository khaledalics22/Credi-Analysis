#!/usr/bin/bash

hdfs dfs -rm -r /PyHadoop/Input/*
hdfs dfs -rm -r /PyHadoop/Output
hdfs dfs -put os_data.csv /PyHadoop/Input
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar -file /home/khalid/Desktop/FY/BDproject/Project/mapper.py -mapper "/home/khalid/Desktop/FY/BDproject/Project/mapper.py 0.3 100" -file ~/Desktop/FY/BDproject/Project/reducer.py -reducer ~/Desktop/FY/BDproject/Project/reducer.py -input /PyHadoop/Input -output /PyHadoop/Output

