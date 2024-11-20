### Task #3. Kafka without using Zookeeper
Set up Kafka in Kraft mode, eliminating the need for Zookeeper. Ensure that Kafka
operates as expected by creating topics and verifying that messages can be
produced and consumed successfully.


broker.properties
```bash
#kraft
process.roles=broker,controller
metadata.log.dir=/home/azureuser/kafka/metadata
listeners=PLAINTEXT://:9092,CONTROLLER://:9093
advertised.listeners=PLAINTEXT://localhost:9092
controller.listener.names=CONTROLLER
listener.security.protocol.map=PLAINTEXT:PLAINTEXT,CONTROLLER:PLAINTEXT
controller.quorum.voters=1@localhost:9093
```
```bash
uuidgen
```
kraft metadata
```bash
bin/kafka-storage.sh format -t 1f8427f8-721d-49b6-9c16-7971ac11a667 -c ssl/brokers/broker4/broker4.properties
```
start broker
```bash
bin/kafka-server-start.sh ssl/brokers/broker4/broker4.properties
```
test that Kafka operates as expected by creating topics and verifying that messages can be produced and consumed successfully.r
```bash
bin/kafka-topics.sh --create --topic devops --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
bin/kafka-console-producer.sh --topic devops --bootstrap-server localhost:9092
bin/kafka-console-consumer.sh --topic devops --from-beginning --bootstrap-server localhost:9092
```
![image](https://github.com/user-attachments/assets/91519b35-00cf-4e33-9c7a-0fd9bc65a8f6)
