from kafka import KafkaProducer
import json
import time
import random

BROKER_LIST = ["localhost:9092", "localhost:9094", "localhost:9095"]
TOPIC = "task6"


producer = KafkaProducer(
    bootstrap_servers=BROKER_LIST,
    security_protocol='SASL_PLAINTEXT',
    sasl_mechanism='PLAIN',
    sasl_plain_username='admin',
    sasl_plain_password='admin-secret',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    retries=5
)


def send_message():
    try:
        while True:
            message = {"key": random.randint(0, 100), "value": random.random()}
            producer.send(TOPIC, value=message)
            print(f"Sent: {message}")
            
            time.sleep(1)
    except Exception as e:
        print(f"Producer error: {e}")
    finally:
        producer.close()

if __name__ == "__main__":
    send_message()

