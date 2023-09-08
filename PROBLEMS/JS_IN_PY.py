# 1. Create a function that takes two numbers as arguments and returns their sum.
# def sum(a,b):
#     print(a+b)
# sum(1,2)

# 2. Write a function that takes an integer minutes and converts it to seconds.
# def convert(x):
#     print(x*60)
# convert(1)


# #### 3.Create a function that takes a number as an argument, increments the number by +1 and returns the result.
# def inc(a):
#     print(a+1)
# inc(500)

# 4.Create a function that takes the age in years and returns the age in days.
# def age(x):
#     count=x/4
#     print((x*360)+count)
# age(20)

# 5.  Create a function that takes voltage and current and returns the calculated power.
# def power(v,c):
#     print(v*c)
# power(2,5)


# 6.Write a function that returns the string "something" joined with a space " " and the given argument a.
# def string(a):
#     print (a +" something")
#     print (a +" "+ "something")
# string("Hello")

# 7. Create a function that takes two arguments. Both arguments are integers, a and b. Return true if one of them is 10 or if their sum is 10.
# def check_10(a,b):
#     if(a==10 or b==10 or a+b==10):
#         print(True)
# check_10(3,8)

# 8.    Create a function that takes two strings as arguments and returns either true or false depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
# def string_check(a,b):
#     if(len(a)==len(b)):
#         print(True)
#     else:
#         print(False)
# string_check("Hello","World!")


# 9.Create a function that takes a name and returns a greeting in the form of a string. Don't use a normal function, use an arrow function.
# greet=lambda x:"Hello"+" "+x
# print(greet("Mani"))


# 10.Create a function that takes a name and returns a greeting in the form of a string. Don't use a normal function, use an arrow function.
# def phone(x):
#     if(len(x)!=10):
#         print("not valid")
#     else:
#         area_code = ''.join(map(str, x[:3]))
#         first_part = ''.join(map(str,x[3:6]))
#         second_part = ''.join(map(str, x[6:]))
#         print( f"({area_code}) {first_part}-{second_part}")
# phone([0,1,2,3,4,5,6,7,8,9])


# 11.Create a function that returns an array of strings sorted by length in ascending order.
# Example:
# sortByLength(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]

# def len_sort(x):
#     n=len(x)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if (x[j]>x[j+1]):
#                 x[j],x[j+1]=x[j+1],x[j]
# #     print(x)
#     print(sorted(x))
# len_sort(["a","aa", "ccc", "dddd", "bb"])
# len_sort([1,22,200,33,444,2,5555])


# 12.Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each.
# Example:
# findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]) ➞ [7, 90, 2]
# def lrg_arr(x):
#     lrg=[]
#     n=len(x)

#     big=0
#     for i in range(n):

#         m=len(x[i])

#         for j in range(0,m):
#             print(x[i][j+1])
#             # if(x[i][j]>x[i][j+1]):
#             #     big=x[i][j]
#             #     print(big)
#         #     else:
#         #         big=x[i][j+1]
#         # lrg.append(big)
#     print(big)
# lrg_arr([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]])

# def lrg_arr(x):
#     lrg=[]
#     for sub in x:
#         lrgnum=0
#         for num in sub:
#             if num>lrgnum:
#                 lrgnum=num
#         lrg.append(lrgnum)
#     print(lrg)
# lrg_arr([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]])


# 13.Create a function that takes an array of numbers and returns the second largest number.
# Example:
# secondLargest([10, 40, 30, 20, 50]) ➞ 40
# def sec_lrg(x):
#     n=len(x)
#     temp=0
#     sec_lrg=0
#     for i in range(n):
#         for j in range(i+1,n):
#             if x[i]>x[j]:
#              temp=x[i]
#              x[i]=x[j]
#              x[j]=temp
#             #  x[i],x[j]=x[j],x[i]

#     if(x[-1]!=x[-2]):
#       sec_lrg=x[-2]
#       print(sec_lrg)
# sec_lrg([10, 40, 30, 20, 50,50])
# import pdb
# def sec_lrg(x):
#     sec=0
#     lrg=0
#     for i in x:
#         if i>lrg:
#             sec=lrg
#             lrg=i
#         elif i>sec and i != lrg:
#             sec=i
#         pdb.set_trace()
#     print(sec)
# sec_lrg([10, 40, 30, 20, 50])


# 14.Create a function that takes an array of items, removes all duplicate items and returns a new array in the same sequential order as the old array (minus duplicates).
# Example:

# removeDups([1, 0, 1, 0]) ➞ [1, 0]

# removeDups(["The", "big", "cat"]) ➞ ["The", "big", "cat"]


# def dup(x):
#     unq=[]
#     for item in x:
#         is_duplicate = False
#         for new_item in unq:
#             if item == new_item:
#                 is_duplicate = True
#                 break
#         if not is_duplicate:
#             unq.append(item)

#     print(unq)
# dup(["The", "big", "cat","big"])


# 15.Create a function that takes an array of integers as an argument and returns a unique number from that array. All numbers except unique ones have the same number of occurrences in the array.

# Example:

# findSingleNumber([2, 2, 2, 3, 4, 4, 4]) ➞ 3


# def unq(x):
#     n=len(x)
#     for i in range(0,n):
#         unq=True
#         for j in range(1,n):
#            if(i!=j and x[i]==x[j]):
#                print(i,j)
#                unq=False
#                break
#         if unq==True:
#             print(i,j)
#             print(x[i])
# unq([2, 2, 2, 3, 4, 4, 4,3,1])

# 16.Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string.
# Example:

# charCount("c", "Chamber of secrets") ➞ 1

# def rep(x, y):
#    l = len(y)
#    count = 0
#    for i in range(0, l):
#       if y[i] == x:
#          count += 1
#    return count

# result = rep("c", "Chamber of secrets")
# print(result)


# 17.Create a function that takes a string and returns the number (count) of vowels contained within it.
# Example:

# countVowels("Celebration") ➞ 5


# def vowels(x):
#    b=x.lower()
#    l=len(x)
#    count=0
#    a=["a","e","i","o","u"]
#    for i in range(0,l):
#       for item in a:
#          if (b[i]== item):
#             count+=1
#       return count

# vowels("Celebration")
# def vowels(x):
#    b = x.lower()
#    l = len(x)
#    count = 0
#    a = ["a", "e", "i", "o", "u"]
#    for i in range(0, l):
#       for item in a:
#          if b[i] == item:
#             count += 1
#    return count

# result = vowels("Celebration")
# print(result)


# 18.Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa.
# Example:
# reverseCase("Happy Birthday") ➞ "hAPPY bIRTHDAY"

# def case(x):
#    l=len(x)
#    result=""
#    for i in range(0,l):
#       if x[i]==x[i].lower():
#          result+=x[i].upper()
#       else:
#          result+=x[i].lower()
#    return result
# print(case("Happy Birthday"))


# 19.Take one integer n, loop till n and pass each value to a function, create a function that takes one integer parameter, and multiply with 2 in every integer.

# Input:      n=5
# Output:   2 4 6 8 10

# def multiply_by_two(x):
#     return x * 2

# def main(n):
#     for i in range(1, n + 1):
#         result = multiply_by_two(i)
#         print({result})

# n = int(input("Enter a value for n: "))
# main(n)

# def mul(n):
#    while n>0:
#      for i in range(1,n+1):
#       n-=1
#       i*=2
#       print(i)
# mul(5)


#  20. Create Function that will take one parameter and return type of the data.

# 			Input:       500
# 			Output:     Integer

# 			Input:       Coding
# 			Output:    String


# def typ(x):
#    print(type(x))
# typ("mani")

#  21. Program to find greatest of three numbers(using ternery operator).

# 			Input:  4 8 2
# 			Output: 8 is gretest

# def greatest(x,y,z):
#    large=x if x>y and x>z else( y if y>z else z)
#    print(large)
# greatest(5,6,3)

# 22 . C Program to find factorial of number.

# 			Input: n=5
# 			Output: 120

# 			Explanation: 5 x 4 x 3 x 2 x 1 = 120

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)

# print(fact(5))
# 23. C Program to arrange numbers in ascending order
# Input: [2,3,1,5,4]
# Output: [1,2,3,4,5]

#     Sort the Array using loop only(you can not use predefined function).

# def sortasc(a):

#    l=len(a)
#    for i in range(0,l):
#       for j in range(i+1,l):
#        if a[i]>a[j]:

#          a[i],a[j]=a[j],a[i]

#    return a
# print(sortasc([2,3,1,5,4]))


# Print Patter using loop.

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# def pattern(n):
#     for i in range(0, n+1):
#         for j in range(1, i+1):
#             print(j,end=" ")
#         print("\r")
# pattern(6)

# 25. C Program to Calculate the Power of a Number(using loop only).

# Input: n=5, p=3
# Output: 5 ^ 3 = 125
# Explanation: 5 x 5 x 5 = 125

# def power(n,p):
#    m=1
#    while p>0:
#       m=m*n
#       p-=1
#    return m
# print(power(5,3))

# 26. Program to Check Whether a Number is Prime or Not

# Input: 9
# Output: 9 is not a prime no

# Input: 7
# Output : 7 is a prime no
# def prime(n):
#    if n>2:
#       for i in range(2,n):
#          if n%i==0:
#             return "It is not a prime"
#          else:
#             return "it is prime"
# print(prime(10))

# 27.Program to find LCM of two numbers using while loop
# Input: 15 50
# Output: Lcm of 15 and 50 is 150.
# def lcm(a, b):
#     def gcd(x, y):
#         while y:
#             x, y = y, x % y
#             print(x,y)

#         return x

#     return (a * b) // gcd(a, b)
# print(lcm(15,50))

# 28. Program to Display Characters from A to Z Using Loop with count.

# Output: A1 B2 C3 D4 E5 F6 ……. Z26
# def alpha():
#    for i in range(26):
#     char = chr(ord('A') + i)
#     count = i + 1
#     print(f"{char}{count}", end=" ")
# alpha()


# 29. Program to find a missing number

# 	Input:  n=5(length of array), arr= [5,3,1,4]
# 	Output: 2 is missing

# Using loop only(you can not use predefined function)
# def find_missing_number(arr, n):
#     total_sum = (n * (n + 1)) // 2  # Sum of first n natural numbers

#     arr_sum = 0
#     for num in arr:
#         arr_sum += num

#     missing_number = total_sum - arr_sum
#     return missing_number
# print(find_missing_number([5,3,1,4],5))

# 30. Program to count vowels and consonants in a given String.

# Input: i am ram
# Output: 3 vowels 3 consonants.
# def count_vowels_consonants(input_string):

#     vowels = "AEIOUaeiou"
#     vowel_count = 0
#     consonant_count = 0

#     for char in input_string:
#         if char.isalpha():
#             if char in vowels:
#                 vowel_count += 1
#             else:
#                 consonant_count += 1

#     return vowel_count, consonant_count
# print(count_vowels_consonants("i am ram"))


# 31. program to insert  the elements of an array for specific index.

# Input: [1,2,3,4,5,7,8,9,10] , index=5
# Output: [1,2,3,4,5,6,78,9,10]

# def insert_element(arr, index, element):
#     arr.insert(index, element)

# input_array = [1, 2, 3, 4, 5, 7, 8, 9, 10]
# insert_index = int(input("Enter the index at which you want to insert: "))
# insert_value = int(input("Enter the value you want to insert: "))

# insert_element(input_array, insert_index, insert_value)
# print("Output:", input_array)

# 32. Reverse a number using while Loop

# Input: 123
# Output: 321
# def reverse_number(number):
#     reversed_num = 0

#     while number > 0:
#         digit = number % 10
#         print(digit)
#         reversed_num = reversed_num * 10 + digit
#         print(reversed_num)
#         number //= 10
#         print(number)

#     return reversed_num

# input_number = int(input("Enter a number: "))
# reversed_result = reverse_number(input_number)
# print("Reversed:", reversed_result)
# 33. Count occurrence of number:

# Input: [1,6,3,1,5,9,7,2,1,9,3,7,8,9,10] , no find=7
# Output: 7 present 2 times.
# def count_occurrence(arr, target):
#     count = 0

#     for num in arr:
#         if num == target:
#             count += 1

#     return count

# input_array = [1, 6, 3, 1, 5, 9, 7, 2, 1, 9, 3, 7, 8, 9, 10]
# target_number = int(input("Enter the number to find: "))

# occurrence_count = count_occurrence(input_array, target_number)
# print(f"{target_number} present {occurrence_count} times.")


# ----------------------------Difficulty Level : Medium------------
# 1.Write a function that converts an object into an array, where each element represents a key-value pair in the form of an array.

# Examples :

# toArray({ a: 1, b: 2 }) ➞ [["a", 1], ["b", 2]]

# def to_array(obj):
#     a=[]
#     for key in obj:
#         a.append([key,obj[key]])

#     return a
# print(to_array({'a': 1, 'b': 2}))

# Create a function that takes two numbers as arguments (num, length) and returns an array of multiples of num until the array length reaches length.
# Examples :

# arrayOfMultiples(7, 5) ➞ [7, 14, 21, 28, 35]

# arrayOfMultiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# arrayOfMultiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

# def mul(a, b):
#     c = []
#     for i in range(1, b+1):
#         c.append(a*i)
#     return c
# print(mul(7, 5))


# 3.Create the function that takes an array with objects and returns the sum of people's budgets.

# Examples :

# getBudgets([
#   { name: "John", age: 21, budget: 23000 },
#   { name: "Steve",  age: 32, budget: 40000 },
#   { name: "Martin",  age: 16, budget: 2700 }
# ]) ➞ 65700

# getBudgets([
#   { name: "John",  age: 21, budget: 29000 },
#   { name: "Steve",  age: 32, budget: 32000 },
#   { name: "Martin",  age: 16, budget: 1600 }
# ]) ➞ 62600


# def getBudget(b):
#     sum=0
#     for k in b:
#         sum+=k['budget']
#     return sum

# print(getBudget([
#     { 'name': 'John', 'age': 21, 'budget': 23000 },
#     { 'name': 'Steve', 'age': 32, 'budget': 40000 },
#     { 'name': 'Martin', 'age': 16, 'budget': 2700 }
# ]))


# 4.Create a function that takes an array of objects like { name: "John", notes: [3, 5, 4]} and returns an array of objects like { name: "John", avgNote: 4 }. If a student has no notes (an empty array) then let's assume avgNote: 0.
# 	Example :

# [
#   { name: "John", notes: [3, 5, 4]}
# ] ➞ [
#   { name: "John", avgNote: 4 }
# ]


# def objavg(input):
#     output=[]
#     for k in input:
#         name=k['name']
#         notes=k['notes']
#         avg_note=sum(notes)/len(notes) if notes else 0
#         output.append({'name': name, 'avgNote': avg_note})
#         return output


# print(objavg([
#   { 'name': "John", 'notes': [3, 5, 4]}
# ]
# ))

# 5.Create a function that moves all capital letters to the front of a word.
# def capsmall(s):
#     cap=''
#     small=''
#     for char in s:
#         if char.isupper():
#             cap+=char
#         else:
#             small+=char
#     return cap+small
# print(capsmall('moveMENt'))


# 6.Count each occurrence of number(can not use predefined function).

# Input: [1,6,3,1,5,9,7,2,1,9,3,7,8,9,10] , no find=7
# Output: 1 present 2 times.
# 	   2 present 1 times.
# 	   3 present 2 times.
# 	   5 present 1 times …….  Etc

# def count_occurrences(numbers):

#     counts = {}

#     for num in numbers:
#         count = 0
#         if num not in counts:
#             for n in numbers:
#                 if num == n:
#                     count += 1
#             counts[num] = count
#     for num, count in counts.items():
#         print(f"{num} present {count} times.")
#         print(counts)

# input_list = [1, 6, 3, 1, 5, 9, 7, 2, 1, 9, 3, 7, 8, 9, 10,9,8,7,6,5,4,2,1,3]
# count_occurrences(input_list)


# 7.Write a function that accepts an array of strings. Return the longest string(can not use predefined function).

# Input: [‘nik’, ’mikhil’, ’Cow’,’Elephant’] 							Output: Elephant

# def long(a):
#     longest=""
#     for item in range(0,len(a)):
#         if len(a[item])>len(longest):
#             longest=a[item]
#     return longest
# print(long(['nik', 'mikhil', 'Cow','Elephant',"metamorphosis"]))

# 8.Most Commonly Used two Character in String(can not use predefined function)

# 				Input: ‘Hii i am ram’
# Output; i, a
# def find_most_common_bigrams(input_str):
#     # Remove spaces and convert the string to lowercase
#     input_str = input_str.replace(" ", "").lower()

#     # Create a dictionary to store bigram counts
#     bigram_counts = {}

#     # Iterate through the string to count bigrams
#     for i in range(len(input_str) - 1):
#         bigram = input_str[i:i + 2]
#         if len(bigram) == 2:  # Check if it's a valid bigram
#             if bigram in bigram_counts:
#                 bigram_counts[bigram] += 1
#             else:
#                 bigram_counts[bigram] = 1

#     # Find the most common bigrams
#     most_common_bigrams = []
#     max_count = 0

#     for bigram, count in bigram_counts.items():
#         if count > max_count:
#             most_common_bigrams = [bigram]
#             max_count = count
#         elif count == max_count:
#             most_common_bigrams.append(bigram)

#     return most_common_bigrams

# # Test the function with the given input
# input_str = 'Hii i am ram'
# result = find_most_common_bigrams(input_str)
# print(", ".join(result))


# 9.Write Program to remove duplicate elements in an array and sort it in descending order(can not use predefined function).

# Input: [5,3,5,2,1,1,7,3,5,6]
# Output: [7,6,5,32,1]

# def dupdec(input):
#     out = []
#     for item in input:
#         if item not in out:
#             out.append(item)
#     n = len(out)
#     for i in range(0, n-1):
#         for j in range(1, n-i-1):
#             if (out[j] < out[j+1]):
#                 out[j], out[j+1] = out[j+1], out[j]
#     return out


# print(dupdec([5, 3, 5, 2, 1, 1, 7, 3, 5, 6]))


####10.Write a Program to Remove brackets from an algebraic expression(can not use predefined function).

			# Input: a + b-(9+c)=3
			# Output: a + b- 9+c=3

# def remove_brackets(expression):
#     result = ""
#     n=len(expression)
#     for i in range(0,n):
#         if(expression[i]!="(" and expression[i]!=")"):
#             print(expression[i])
#             result+=expression[i]
    
  

#     return result

# # # Example usage
# input_expression = "a + b-(9+c)=3"
# output_expression = remove_brackets(input_expression)

# print(output_expression)


####11.Write Program to remove duplicate elements in an array and sort it in Accending order(can not use predefined function).

			# Input: [Z, A, P, C, A, Z , K, N, C]
			# Output: [A, C, K,N, P, Z]

# def alpha(a):
#     b=[]
#     for char in a:
#         if char not in b:
#             b.append(char)
    
#     n=len(b)
#     for i in range(0,n):
#         for j in range(0,n-i-1):
#             if b[j]>b[j+1]:
#                 b[j],b[j+1]=b[j+1],b[j]
                
    
#         return b
# print(alpha(['Z', 'A', 'P', 'C', 'A', 'Z' , 'K', 'N', 'C']))

# def remove_duplicates_and_sort(input_list):
#     # Remove duplicates
#     unique_elements = []
#     for element in input_list:
#         if element not in unique_elements:
#             unique_elements.append(element)
    
#     # Sort the list in ascending order (you can use any sorting algorithm)
#     n = len(unique_elements)
#     for i in range(n-1):
#         for j in range(0, n-i-1):
#             if unique_elements[j] > unique_elements[j+1]:
#                 unique_elements[j], unique_elements[j+1] = unique_elements[j+1], unique_elements[j]
    
#     return unique_elements

# # Example usage
# input_list = ['Z', 'A', 'P', 'C', 'A', 'Z', 'K', 'N', 'C']
# output_list = remove_duplicates_and_sort(input_list)

# print(output_list)
####12. If subseq's  array  sequence is present in the array, returns true or else returns false.                                                    
# Let arr = [5, 7, 3, 2, 2, 7,-1, 5, -3, 13, 4]
# Example: 
#            Input : Subseq1 = [7, -1, 5, -3] Output:  true
#                       Subseq2 = [7, -1, 4, -3]            : false
#            Subseq3 = [ -1]                        : true
#                       Subseq4 = [13, -3, 4, 1]           : false

