https://gitlab.com/mastering-ci-cd/task4

https://gitlab.com/mastering-ci-cd/task4

https://gitlab.com/mastering-ci-cd/task4


![image](https://github.com/user-attachments/assets/af27c52b-174c-4d7d-8ee9-389499ea9f10)


# Instructions

1) clone repo
```bash
git clone git@gitlab.com:mastering-ci-cd/task4.git
cd task4
```
2) create and go to new branch
```bash
git checkout -b feature/update-kafka-config
```
3) change json file
{
  "topics": [
    {
      "action": "create",
      "name": "merge2",
      "partitions": 6,
      "replication_factor": 3,
      "delete_policy": "delete"
    }
  ],
  "permissions": [
    {
      "topic": "new_topic3",
      "user": "alice",
      "access": ["read", "write"]
    }
  ]
}

```bash
4) push changes
git add .
git commit -m "change json"
git push origin "feature/update-kafka-config"
```

5) Create merge request 
![image](https://github.com/user-attachments/assets/22c4bdcc-f9d9-40ad-b819-b756fd29d811)


![image](https://github.com/user-attachments/assets/198bc408-fea2-42d2-b301-42ac8ecc0c55)


![image](https://github.com/user-attachments/assets/7081296e-31ca-46c9-8ba8-b95d42ab69bb)


![image](https://github.com/user-attachments/assets/3ba31d03-07cb-43cb-bd4a-ea87e6bdb171)
