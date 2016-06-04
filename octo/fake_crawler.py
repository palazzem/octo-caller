import time
import msgpack

from kafka import KafkaProducer


BROKER_ADDRESS = '10.0.30.10:9092'
TOPIC_NAME = 'amazon'


if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers=BROKER_ADDRESS,
        value_serializer=msgpack.dumps,
    )

    print('Start publishing data...')
    for _ in range(100):
        producer.send(TOPIC_NAME, {'data': 'some_data'})
        time.sleep(1)
