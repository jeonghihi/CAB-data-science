# pip install kafka-python==1.4.4
#%%
#!/usr/bin/env python
from kafka import KafkaClient
import json,requests
from kafka import SimpleProducer
#from kafka import KafkaProducer

#%%
# # Creating Kafka client
kafka = KafkaClient('localhost:9092')
# #Creating a Kafka producer instance
meetup_producer = SimpleProducer(kafka)

#producer = KafkaProducer(bootstrap_servers='localhost:9092')

r = requests.get("https://stream.meetup.com/2/rsvps",stream=True)
#> response: 200

# Sending messages to Consumer.
for line in r.iter_lines():
    try:
        meetup_producer.send_messages('meetup',line)
        obj = json.loads(line.decode('utf-8'))
    ## printing the cities on console
        rsvps= (obj['group']['group_city'])
        print(rsvps)
    except:
        pass

kafka.close()
