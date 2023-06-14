# Quickstart Aiven for Kafka and Flink using Python
The ETH-producer.py script was tested on Ubuntu 22.04 running in Windows WSL. 

First, install the dependency:
```
pip install kafka-python
```
Next, create a kafka cluster following the [getting started guide](https://docs.aiven.io/docs/products/kafka/getting-started), take note of the bootstrap server URL and port, and download the required cert files into the same directory as the `ETH-producer.py` script.

The producer script queries the Coinbase public spot price API and receives a json file containing
```
{"data":{"base":"ETH","currency":"USD","amount":"1740.72"}}
```
The script then adds the date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) to the json as a value.
Next a UUID is created as a key and then the message is sent to an existing Kafka topic using an Aiven managed cluster. 
The loop can be run continuously by removing the comment from 
```
while(True):
```
and can then be terminated using `Ctrl+C`.
