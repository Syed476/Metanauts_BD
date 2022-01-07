import subprocess
from json import  loads
from kafka import KafkaConsumer
import pydoop.hdfs as hdfs
import os
import sys

def main():
	hdfs.mkdir('hdfs://localhost:9000/ApiDataKafka')
	file='/home/maqsood/data.txt'
	args_list=['hdfs','dfs','put',file,'/ApiDataKafka']
	print('Running system command {}'.format(' '.join(args_list)))
	print ('This is data from a new stream')
	proc = subprocess.Popen(args_list,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	proc.communicate()
	hdfs_path='hdfs://localhost:9000/ApiDataKafka/data.txt'
	consumer = KafkaConsumer('sample',bootstrap_servers=['localhost:9092'], value_deserializer=lambda x: loads(x.decode('utf-8')))
	for message in consumer:
		print(message)
		
		with hdfs.open(hdfs_path, 'at') as f:
			f.write(f"{message}\n")
main()
