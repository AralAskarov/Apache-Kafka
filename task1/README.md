# Task #1. Kafka cluster
Set up and configure an Apache Kafka cluster comprising three brokers named
broker01, broker02, and broker03. Ensure that the brokers start successfully and
operate together as a unified cluster.
Create topic with multiple partitions and verify the distribution of these partitions
across the brokers

# prerequisites
```bash
sudo apt update
sudo apt install openjdk-11-jre-headless -y
wget https://downloads.apache.org/kafka/3.8.1/kafka_2.13-3.8.1.tgz
tar -xzf kafka_2.13-3.8.1.tgz
mv kafka_2.13-3.8.1 kafka
cd kafka
```

# 1) Zookeeper
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties &
```
# 2) Brokers
```bash
cp config/server.properties config/broker01.properties
cp config/server.properties config/broker02.properties
cp config/server.properties config/broker03.properties
```
need to change their configuration
```bash
cd config
vim broker01.properties
broker.id=1  
listeners=PLAINTEXT://0.0.0.0:9092 
advertised.listeners=PLAINTEXT://<REMOTE_SERVER_IP>:9092  # localhost
vim broker02.properties
broker.id=2
listeners=PLAINTEXT://0.0.0.0:9093 
advertised.listeners=PLAINTEXT://<REMOTE_SERVER_IP>:9093  # localhost
vim broker03.properties
broker.id=3 
listeners=PLAINTEXT://0.0.0.0:9094 
advertised.listeners=PLAINTEXT://<REMOTE_SERVER_IP>:9094  # localhost
```
Launch of brokers
```bash
bin/kafka-server-start.sh config/broker01.properties &
bin/kafka-server-start.sh config/broker02.properties &
bin/kafka-server-start.sh config/broker03.properties &
```

# 3) Creating a topic
```bash
bin/kafka-topics.sh --create --topic devops --bootstrap-server localhost:9092 \
  --partitions 6 --replication-factor 3
```
replication factor = 3
partitions = 6
![image](https://github.com/user-attachments/assets/693e88b8-6263-4b01-b37a-3081802e3e60)

# 4) Add data 
```bash
bin/kafka-console-producer.sh --topic devops --bootstrap-server localhost:9092
>First message
>Hi everyone
```
# 5) Read messages
```bash
bin/kafka-console-consumer.sh --topic devops --bootstrap-server localhost:9092 --consumer-property auto.offset.reset=earliest
```
![image](https://github.com/user-attachments/assets/d5be7441-7dd0-4636-adcc-8fa3aae4ffa0)

if we run bin/kafka-console-producer.sh --topic devops --bootstrap-server localhost:9092 all messages will go into one partition, its because of default configuration UniformStickyPartitioner. without keys messages will go into one partition, until the partition is full or the time threshold expires. To to distribute messages need to use keys
```bash
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic devops --property "parse.key=true" --property "key.separator=:"
```
![image](https://github.com/user-attachments/assets/31021342-42dc-48a2-88d7-b812dd3dfab8)

![image](https://github.com/user-attachments/assets/6e1336f8-0463-4769-8519-7873850c595a)
