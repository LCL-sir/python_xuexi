import threading
import time


def sing():
    while True:
        print("唱歌")
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == "__main__":
    # 创建一个唱歌的多线程
    sing_thread = threading.Thread(target=sing)
    # 创建一个跳舞的多线程
    dance_thread = threading.Thread(target=dance, args=("跳舞",))

    # 启动多线程
    sing_thread.start()
    dance_thread.start()
