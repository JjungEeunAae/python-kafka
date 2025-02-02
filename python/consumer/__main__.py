from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'my-topic',
    group_id='my-group',
    bootstrap_servers=['localhost:2001']
)


for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
