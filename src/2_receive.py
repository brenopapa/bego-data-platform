#!/usr/bin/env python
import os
import sys
import threading

from dotenv import dotenv_values
from lib.consumer import consumer

config = dotenv_values(".env")

def main():

    t0 = threading.Thread(target=consumer, args=("customer",))
    t1 = threading.Thread(target=consumer, args=("product",))
    t2 = threading.Thread(target=consumer, args=("purchase",))

    t0.start()
    t1.start()
    t2.start()

    t0.join()
    t1.join()
    t2.join()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
