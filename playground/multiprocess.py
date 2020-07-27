from time import sleep
import multiprocessing


def go_to_sleep():
    sleep(5)
    print("Sleep for 5 seconds.")

# go_to_sleep()


for i in range(2):
    p = multiprocessing.Process(target=go_to_sleep)
    p.start()
