import random
import time

def hello():
    random_num = random.randint(1, 100)
    timestamp = time.time()
    print('Hello world:', random_num, timestamp)

if __name__ == "__main__":
    hello()
