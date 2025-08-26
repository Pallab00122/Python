# number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(len(number_list) - 1, -1, -1):
#     if number_list[i] > 50:
#         del number_list[i]
# print(number_list)

# # -----------------------=====---------------====-=-
# def isValidParenthesis(s):
#     stack = []
#     for i in s:
#         if i == '(':
#             stack.append(i)
#         elif i == ')':
#             if not stack:
#                 return False
#             stack.pop()
#     return len(stack) == 0

# if __name__ == "__main__":
#     T = int(input().strip())
#     for _ in range(T):
#         S = input().strip()
#         print(1 if isValidParenthesis(S) else 0)

mystr = "canana"

myit = iter(mystr)
print(type(myit))
print(next(myit))

for x in mystr:
  print(x)
print(type(mystr))


# ----Create an iterator for fibonacci series in such a way that each next returns the next element from fibonacci series.
# -----The iterator should stop when it reaches a limit defined in the constructor.

class Fibonacci:
  def __init__(self,limit):
    self.previous=0
    self.current=1
    self.n=1
    self.limit=limit
  def __iter__(self):
    return self
  def __next__(self):
    if self.n < self.limit:
      result=self.previous+self.current
      self.previous=self.current
      self.current=result
      self.n +=1
      return result
    else:
      raise StopIteration
fib_iterator=iter(Fibonacci(6))
while True:
    try:
        print(next(fib_iterator))
    except StopIteration:
        break

