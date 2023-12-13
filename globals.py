from ib_insync import *
import random

ib = IB()
random_id = random.randint(0,9999)
# TODO: Make this more robust + reconnect logic wherever we use ib
ib.connect('127.0.0.1', 4001, clientId=random_id)