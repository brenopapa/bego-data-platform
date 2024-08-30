#!/usr/bin/env python
import os
import sys
import argparse
from dotenv import dotenv_values
from utils.entities import entities
from lib.producer import producer

config = dotenv_values(".env")

parser = argparse.ArgumentParser()
parser.add_argument('-s','--size', help='Size of data returned by Faker - 10 equals to 10 records.', required=True, type=int)
parser.add_argument('-e','--entity', help=f'Data Entity - Available: {str(entities())}', required=True, choices=entities())
args = vars(parser.parse_args())

def main():

    p = producer(args['entity'], args['size'])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)