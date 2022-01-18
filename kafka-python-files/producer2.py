from json import dumps
from kafka import KafkaProducer
from data2 import get_data
def main():
	producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
	producer.send('topic-name',get_data())
	
main()


