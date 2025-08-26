# In this program clearly see if first i am not mention the join() method then "Total time taken " is printed before the program executed
# After the join() method main thread will wait until the t1.join() method executed

from threading import *
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("Doubles Values :",2*n)
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print("Squares Values :",n*n)

numbers=[1,2,3,4,5,6]
beginTime=time.time()
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()

endTime=time.time()
print("Total time taken:",endTime-beginTime)


