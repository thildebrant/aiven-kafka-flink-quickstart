from kafka import KafkaProducer
from time import sleep
import datetime
import uuid
import requests
import json

# Coinbase API endpoint
url = 'https://api.coinbase.com/v2/prices/eth-usd/spot'

# Producing as JSON
producer = KafkaProducer(
 bootstrap_servers=f"kafka-303170d-thildebrant-2fb1.aivencloud.com:13628",
 security_protocol="SSL",
 ssl_cafile="./ca.pem",
 ssl_certfile="./service.cert",
 ssl_keyfile="./service.key",
 value_serializer=lambda v: json.dumps(v).encode('ascii')
)

#either a continuous loop or a small loop for testing
while(True):
#for i in range(3):
    sleep(2)
    price = ((requests.get(url)).json())
    current_date = datetime.datetime.now()
    price["datetime"] = current_date.isoformat()
    uuid_str = '{' + str(uuid.uuid4()) +'}'
    producer.send('ETH-prices',  key=bytes(uuid_str, encoding='UTF-8'), value=price)
    producer.flush()
