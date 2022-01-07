from json import dumps
from kafka import KafkaProducer
from data1 import get_data
def main():
	producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
	producer.send('sample',get_data())
	
main()
