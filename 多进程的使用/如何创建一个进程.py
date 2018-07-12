from multiprocessing import Process
import os


def run(name):
    print(os.getpid())
    while True:
        print('this is' + name)


def main(name):
    print(os.getpgid())
    while True:
        print('this is' + name)


if __name__ == '__main__':
    print('主进程开始')
    p1 = Process(target=run, args=('run',))
    p2 = Process(target=main, args=('main',))

    # Fasle表示，主进程无论是否结束，我的子进程都会执行,
    # True表示，表示同生共死
    p1.daemon = True
    p2.daemon = True
    p1.start()
    p2.start()

    # 告诉主进程必须等子进程结束才能结束
    p1.join()
    p2.join()
    print('主进程结束')
