# step1 - install files
## download JRE (java configuration)

## download zookeepr and unzip file using cmd; 
```
tar -xzf apache-zookeeper-3.7.0-bin.tar.gz
```
## move zookeeper directory to C:\

## download kafka and unzip & install using cmd;
- https://www.apache.org/dyn/closer.cgi?path=/kafka/2.7.0/kafka_2.12-2.7.0.tgz
```
tar -xzf kafka_2.12-2.7.0.tgz
```
##  move kafka directory to C:\

# step2 - launch files
## open cmd and move to the directory where kafka is installed
```
c:\ > cd kafka_2.12-2.7.0
```

## run zookeeper & kafka on the seperate cmd
```
bin\windows\zookeeper-server-start.bat config\zookeeper.properties
bin\windows\kafka-server-start.bat config\server.properties
```

# step3 - create contents
(for mac) bin\kafka-topics.sh --create--topic quickstart-events --bootstrap-server localhost:9092

# error from step3 (because step2 didn't open zookeeper and kafka using winodw.bat)
WARN [AdminClient clientId=adminclient-1] Connection to node -1 (localhost/127.0.0.1:9092) could not be established. Broker may not be available. (org.apache.kafka.clients.NetworkClient)

# error from step3 (after opening zoo and kafka, and check localhost number on the log)
ERROR org.apache.kafka.common.errors.TimeoutException: Call(callName=createTopics, deadlineMs=1621338980896, tries=1, nextAllowedTryMs=1621338981014) timed out at 1621338980914 after 1 attempt(s)
Caused by: org.apache.kafka.common.errors.DisconnectException: Cancelled createTopics request with correlation id 3 due to node 0 being disconnected (kafka.admin.TopicCommand$)

# error from step3 solved: keep two prompt open (one for zookeeper, one for kafka)

# create topic
# follow command written here: https://www.javatpoint.com/creating-kafka-topics
kafka-topics --zookeeper localhost:2181 --topic quickstart-event --create --partitions 3 --replication-factor 1

# describe topic
kafka-topics -zookeeper localhost:2181 -describe --topic quickstart-event

# write info into the topic
(mac) bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
(win) kafka-console-producer -broker-list localhost:9092 -topic quickstart-events

# read the topic - from step6 we install pip kafka python
(mac) $ bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
(win) kafka-console-consumer -bootstrap-server localhost:9092 -topic quickstart-events

# in the visual studio code
pip install kafka-python


#===========tips ===============
# how to check global configuation
bin\windows\kafka-topics.bat --list --zookeeper localhost:2181

# kafka listeners
https://rmoff.net/2018/08/02/kafka-listeners-explained/

# error: when broker is 0 
https://stackoverflow.com/questions/33098366/error-creating-kafka-topics-replication-factor-larger-than-available-brokers
