#!/usr/bin/env python
import os
import sys
import threading
from time import sleep

from dotenv import dotenv_values
from lib.consumer import consumer

config = dotenv_values(".env")

def main():

    t0 = threading.Thread(target=consumer, args=("customer",), daemon=True)
    t1 = threading.Thread(target=consumer, args=("product",), daemon=True)
    t2 = threading.Thread(target=consumer, args=("purchase",), daemon=True)

    t0.start()
    t1.start()
    t2.start()

    try:
        while (t0.is_alive() or t1.is_alive() or t2.is_alive()):
            sleep(1)
        print("Thread finished task, exiting")
    except KeyboardInterrupt:
        print("[X] Closing main-thread.This will also close the background thread because is set as daemon.")
    return 0

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
