from concurrent.futures import ProcessPoolExecutor
import time, os
from multiprocessing import Pool


# 创建一个进程池


def runtest(i):
    print('进程开启' + str(os.getpid()))
    time.sleep(2)
    print('进程关闭' + str(os.getpid()))
    return i

#回调函数示例
def done(data):
    print(data)


#
#
# processPoll = ProcessPoolExecutor(max_workers=4)
# for i in range(0, 50):
#     processPoll.submit(runtest, (i,))
#
# processPoll.shutdown(wait=True)
# ----------------------------------------------------------------------------------------
# 第二种方式构建进程池
p = Pool(4)
for i in range(0, 50):
    p.apply_async(func=runtest, args=(i,), callback=done)
# 表示关闭进程池,不能再添加任务了
p.close()
p.join()
