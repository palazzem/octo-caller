import time
import msgpack

from kafka import KafkaConsumer


BROKER_ADDRESS = '10.0.30.10:9092'
TOPIC_NAME = 'amazon'


if __name__ == '__main__':
    consumer = KafkaConsumer(
        bootstrap_servers=BROKER_ADDRESS,
        auto_offset_reset='earliest',
        value_deserializer=msgpack.unpackb,
    )

    consumer.subscribe([TOPIC_NAME])

    for message in consumer:
        # you'll do the computation here with
        # the deserialized object
        print(message)
