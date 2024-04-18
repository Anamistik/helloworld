import random
import time

LIMON = True

def hello():
    random_num = random.randint(1, 100)
    timestamp = time.time()
    print('Hello world:', random_num, timestamp)

def random_num_print():
    print('Random num: ', random.randint(20, 200))

if __name__ == "__main__":
    if LIMON:
        hello()
    else:
        random_num_print()
