#!/usr/bin/env python
import pika
from utils.fakedata import fakedata

from dotenv import dotenv_values

config = dotenv_values(".env")

def producer(entity: str, size: int):

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=config["CLOUDAMQP_HOST"], 
                                virtual_host=config["CLOUDAMQP_VHOST"], 
                                credentials=pika.PlainCredentials(username=config["CLOUDAMQP_USERNAME"], password=config["CLOUDAMQP_PASSWORD"])),
    )

    channel = connection.channel()

    channel.queue_declare(queue=entity)

    channel.basic_publish(exchange="", routing_key=entity, body=fakedata(entity, size))
    print(f" [x] Sent {entity} Data!'")

    connection.close()
