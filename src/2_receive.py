#!/usr/bin/env python
import uuid
import os
import sys
import json
import pika
import pyarrow
import pyarrow.parquet as pq
import pandas

from dotenv import dotenv_values

config = dotenv_values(".env")

def main(entity: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=config["CLOUDAMQP_HOST"], 
                                virtual_host=config["CLOUDAMQP_VHOST"], 
                                credentials=pika.PlainCredentials(username=config["CLOUDAMQP_USERNAME"], password=config["CLOUDAMQP_PASSWORD"])),
    )
    channel = connection.channel()

    channel.queue_declare(queue=f"{entity}")

    def callback(ch, method, properties, body):
        print(body)
        json_object = json.loads(body.decode().replace("\'", "\""))
        print(f" [x] Received {entity} Data!")

        print(json_object)

        table = pyarrow.Table.from_pandas(pandas.DataFrame(json_object, index=list(range(len(json_object)))))
        pq.write_table(table, f'data/bronze/{entity}/{entity}-{uuid.uuid4()}.parquet')

        print(f" [x] Wrote {entity} Data in Parquet!")

    channel.basic_consume(
        queue=f"{entity}",
        on_message_callback=callback,
        auto_ack=True,
    )

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    entity = 'purchase'
    try:
        main(entity)
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
