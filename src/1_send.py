#!/usr/bin/env python
import argparse
import pika
from utils.fakedata import fakedatacustomer

from dotenv import dotenv_values

config = dotenv_values(".env")

parser = argparse.ArgumentParser()
parser.add_argument('-s','--size', help='Size of data returned by Faker - 10 equals to 10 records.', required=False, type=int)
args = vars(parser.parse_args())

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=config["CLOUDAMQP_HOST"], 
                              virtual_host=config["CLOUDAMQP_VHOST"], 
                              credentials=pika.PlainCredentials(username=config["CLOUDAMQP_USERNAME"], password=config["CLOUDAMQP_PASSWORD"])),
)

channel = connection.channel()

channel.queue_declare(queue="customers")

channel.basic_publish(exchange="", routing_key="customers", body=fakedatacustomer(args['size']))
print(" [x] Sent Customer Data!'")

connection.close()
