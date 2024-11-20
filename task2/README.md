![image](https://github.com/user-attachments/assets/0f2a8813-abf7-4393-aa3f-ca54a43a344a)

broker properties
```bash
process.roles=broker,controller
metadata.log.dir=/home/azureuser/kafka/metadata/broker1 
listeners=BROKER://:9092,CONTROLLER://:9093
advertised.listeners=BROKER://:9092
listener.security.protocol.map=BROKER:SASL_PLAINTEXT,CONTROLLER:SASL_PLAINTEXT
inter.broker.listener.name=BROKER
controller.listener.names=CONTROLLER
sasl.enabled.mechanisms=PLAIN
sasl.mechanism.controller.protocol=PLAIN
sasl.mechanism.inter.broker.protocol=PLAIN
controller.quorum.voters=1@localhost:9093
```

kafka_server_jaas.conf
```bash
KafkaServer {                                                                            
    org.apache.kafka.common.security.plain.PlainLoginModule required
    username="admin"
    password="admin-secret"
    user_admin="admin-secret"
    user_alice="alice-secret";
};
```

export KAFKA_OPTS="-Djava.security.auth.login.config=/home/azureuser/kafka/kafka_server_jaas.conf"

client properties
```bash
security.protocol=SASL_PLAINTEXT                                                         
sasl.mechanism=PLAIN
 
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required \
    username="alice" \
    password="alice-secret";
```
start broker
```bash
bin/kafka-server-start.sh ssl/brokers/broker1/broker1.properties
```

create topic
```bash
bin/kafka-topics.sh --create \
    --topic my-topic \
    --bootstrap-server localhost:9092 \
    --partitions 3 \
    --replication-factor 1 \
    --command-config /home/azureuser/kafka/ssl/clients/alice/client.properties
```
messages into topic
```bash
bin/kafka-console-producer.sh     --broker-list localhost:9092     --topic my-topic     --producer.config /home/azureuser/kafka/ssl/clients/alice/client.properties
```

read messages
```bash
bin/kafka-console-consumer.sh \h \
    --bootstrap-server localhost:9092 \
    --topic my-topic \
    --from-beginning \
    --consumer.config /home/azureuser/kafka/ssl/clients/alice/client.properties
```
![image](https://github.com/user-attachments/assets/bb018d88-9afc-4d63-ba51-9dfa8b716cd4)
![image](https://github.com/user-attachments/assets/4144bbd1-f937-4dc1-82d1-441b5933e31c)


lets try with invalid data
invalid_client.properties
```bash
security.protocol=SASL_PLAINTEXT
sasl.mechanism=PLAIN
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required \
    username="alice" \
    password="wrong-password";
```

```bash
bin/kafka-console-producer.sh     --broker-list localhost:9092     --topic my-topic     --producer.config /home/azureuser/kafka/ssl/clients/wrong/invalid_client.properties
```

![image](https://github.com/user-attachments/assets/c39ed702-56d8-4ed4-b986-40212840994b)
