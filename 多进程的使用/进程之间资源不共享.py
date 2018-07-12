from queue import Queue
from multiprocessing import Process


def main():
    pageQueue = Queue(50)

    for i in range(0, 30):
        pageQueue.put(i)
    # 进程之间数据不共享


if __name__ == '__main__':
    main()
