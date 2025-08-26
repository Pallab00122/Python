def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
g=mygen()
print(type(g))
print(next(g))
print(next(g))


# import time
# def countdown(num):
#     print("Count down started ")
#     while num>0:
#         yield num
#         num = num-1
# values=countdown(5)
# for i in values:
#     print(i)
#     time.sleep(1)

print("The fibonacci series is : ")
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for n in fib():
    if n > 100:
        break
    print(n)

# import random
# import time

# names=['sunny','bunny']
# subjects=['Python','java']
# def lis(num):
#     result=[]
#     for i in range(num):
#         person={
#             'id':1,
#             'name':random.choice(names),
#             'subject':random.choice(subjects)
#         }
#         result.append(person)
#     return result

print("The square ---")
def square():
  i=1
  while True:
    yield i*i
    i=i+1
for n in square():
    if n>25:
      break
print(n)
  

