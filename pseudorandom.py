from time import sleep

seed = 1;

def random():
    global seed 
    a = 17
    c = 19
    m = 2 ** 24
    seed = (a * seed + c) % m
    return int(seed / m * 10)

while True:
    number = random()
    print(number)
    sleep(1)