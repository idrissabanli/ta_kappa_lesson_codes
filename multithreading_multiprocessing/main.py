import time
import random
import threading
import multiprocessing
import requests

def download_image():
    res = requests.get('https://picsum.photos/200')
    with open(f'images/image_{random.randint(0,100000)}.png', 'wb') as f:
        f.write(res.content)


# def do_something():
#     print('proccess start')
#     time.sleep(1)
#     print('proccess end')

threads = []
t1 = time.time()

# if __name__ == '__main__':
#     t1 = time.time()
#     proccesses = []
#     for _ in range(100):
#         proccess = multiprocessing.Process(target=download_image)
#         proccess.start()
#         proccesses.append(proccess)


#     for pr in proccesses:
#         pr.join()

#     t2 = time.time()

    # delta_time = t2 - t1

    # print('delta_time', delta_time)

for _ in range(100):
    thread = threading.Thread(target=download_image)
    thread.start()
    threads.append(thread)

# CPU 1

# RAM  7

# HDD 30


for th in threads:
    th.join()

t2 = time.time()

delta_time = t2 - t1

print('delta_time', delta_time)


# for _ in range(10):
#     download_image()




# threads = []

# for _ in range(1000):
#     thread = threading.Thread(target=do_something)
#     thread.start()
#     threads.append(thread)

# for th in threads:
#     th.join()


# for _ in range(10):
#     do_something()


