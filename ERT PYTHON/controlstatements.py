# control staements
# words=['cat','window','dog']
# for w in words:
#     print(w,len(w))

# create a sample collection
# users={'Mani':'active','sharath':'active','harish':'active','sai':'inactive'}
# # print(users.copy().items())
# for user,status in users.copy().items():
#     print(status)
#     if status=='inactive':
#         del users[user]
#         print(users)
# active_users={}
# for user,status in users.items():
#     if status=='active':
#         active_users[user]=status
#         print(active_users)cls
# range
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#             print(n, 'is a prime number')

# for num in range(2, 10):
#     if num % 2 == 0:
#      print("It is a even number", num)
#      continue
#     print("It is a odd number",num)

# match point:
#     case (0, 0):
#         print("Origin")
#     case (0, y):
#         print(f"Y={y}")
#     case (x, 0):
#         print(f"X={x}")
#     case (x, y):
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not a point")


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# def where_is(point):
#     match point:
#         case Point(x=0, y=0):
#             print("Origin")
#         case Point(x=0, y=y):
#             print(f"Y={y}")
#         case Point(x=x, y=0):
#             print(f"X={x}")
#         case Point():
#             print("Somewhere else")
#         case _:
#             print("Not a point")
# from enum import Enum
# class Color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'

# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")y
#     case Color.BLUE:
#         print("I'm feeling the blues :(")

# def fib(n):
#     a,b=0,1
#     while a<n:
#         print(a,end=" ")
#         a,b=b,a+b
#         print()
# fib(100)
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     # prompt="enter the response:"
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             print(1)
#         if ok in ('n', 'no', 'nop', 'nope'):
#             print(0)
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
        
# ask_ok("are you fine?")

# squares=[]
# for x in range (10):
#     squares.append(x**3)

# print(squares)

# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
# print(combs)

# matrix=[
#     [1,2,3,10],
#     [4,5,6,11],
#     [7,8,9,12]
# ]
# transposed=[]
# for i in range (4):
#     transposed.append([row[i] for row in matrix])
# # print(transposed)

# print(list(zip(*matrix)))


# class Dog:
 
#     # class attribute
#     attr1 = "mammal"
#     attr2="friendly"
 
#     # Instance attribute
#     def __init__(self, name):
#         self.name = name
 
# # Driver code
# # Object instantiation
# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")
 
# # Accessing class attributes
# print("Rodger is a {}".format(Rodger.__class__.attr1))
# print("Rodger is a {} dog".format(Rodger.__class__.attr2))


# print("Tommy is also a {}".format(Tommy.__class__.attr1))
# print("Tommy is also a {} dog".format(Tommy.__class__.attr2))
 
# # Accessing instance attributes
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))



# class Dog:
#     attr1="mammal"
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         # print("My name is {} ".format(self.name))
#         print(f"My name is {self.name}")
# Rodger=Dog("Rodger")
# Tommy=Dog("Tommy")
# Rodger.speak()
# Tommy.speak()

       