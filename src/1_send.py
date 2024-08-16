#!/usr/bin/env python
import argparse
import pika
from utils.fakedata import fakedata
from utils.entities import entities

from dotenv import dotenv_values

config = dotenv_values(".env")

parser = argparse.ArgumentParser()
parser.add_argument('-s','--size', help='Size of data returned by Faker - 10 equals to 10 records.', required=True, type=int)
parser.add_argument('-e','--entity', help=f'Data Entity - Available: {str(entities())}', required=True, choices=entities())
args = vars(parser.parse_args())

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=config["CLOUDAMQP_HOST"], 
                              virtual_host=config["CLOUDAMQP_VHOST"], 
                              credentials=pika.PlainCredentials(username=config["CLOUDAMQP_USERNAME"], password=config["CLOUDAMQP_PASSWORD"])),
)

channel = connection.channel()

channel.queue_declare(queue=args['entity'])

channel.basic_publish(exchange="", routing_key=args['entity'], body=fakedata(args['entity'], args['size']))
print(f" [x] Sent {args['entity']} Data!'")

connection.close()
