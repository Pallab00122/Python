# import threading
#  class Mythread(threading.Thread)


# from threading import *
# def display():
#     for i in range(5):
#         print("Child Thread")
# t=Thread(target=display)
# t.start()
# for i in range(5):
#     print("Main Thread")



from threading import *
import time

class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("Child Thread")
            time.sleep(1)
# class ThreadDemo:
#     def main():
t=MyThread()
t.start()
for i in range(5):
    print("Main Thread")
    time.sleep(2)
#         t.join()
# if __name__=="__main__":
#     ThreadDemo.main()

# ----------------------------------------------------------------------------------------------------------

# import threading
# import time

# shared_count=0

# # Create a Lock object
# counter_lock = threading.Lock()

# class MyThread(threading.Thread):
#     def run(self):
#         global shared_count
#         for i in range(5):
#             print("Child Thread ..")
#             time.sleep(0.02)
#             counter_lock.acquire()
#             try:
#                 shared_count +=1
#             finally:
#                 counter_lock.release()
# class ThreadDemo:
#     def main():
#         global shared_count
#         t=MyThread()
#         t.start()
#         t.join()
#         for i in range(5):
#             print("Main Thread ..")
#             time.sleep(0.03)
#             counter_lock.acquire()
#             try:
#                 shared_count += 1
#             finally:
#                 counter_lock.release()
#         # t.join()

# if __name__ == "__main__":
#     ThreadDemo.main()