### Task #5. Kafka cluster with systemd
Create and configure systemd for Apache Kafka, assigning one unit service per
broker.
Use systemctl commands to stop specific Kafka brokers and verify that the cluster
continues to operate correctly.

```bash
sudo systemctl daemon-reload

sudo systemctl enable kafka-broker1.service
sudo systemctl enable kafka-broker2.service
sudo systemctl enable kafka-broker3.service

sudo systemctl start kafka-broker1.service
sudo systemctl start kafka-broker2.service
sudo systemctl start kafka-broker3.service
```

![image](https://github.com/user-attachments/assets/79c71a70-d696-4da2-ac77-30587d964857)

![image](https://github.com/user-attachments/assets/ad0d78bf-adaa-47dd-9dbd-60256d4f70bc)

![image](https://github.com/user-attachments/assets/41356a6b-eaa8-4d07-bd1d-4bf0f559bd4a)
