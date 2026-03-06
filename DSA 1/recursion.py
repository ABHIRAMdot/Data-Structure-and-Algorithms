# def print_numbers(n):
#     if n==0:
#         return
#     print(n, end= " ")
#     print_numbers(n-1)
#     # print(n, end= " ")

# print_numbers(10)

#---------------------------------------------

# #factorial
def factorial(n):
    if n == 0 or n ==1:
        return 1
    
    return n * factorial(n-1)

# print(factorial(4))

#---------------------------------------------

# #fibnlocci
def fib(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

# for i in range(5):
#     print(fib(i), end=" ")

#-----------------------------------------------------

## fib under limit
def fib_under_limit(a, b, limit):
    if a > limit:
        return
    print(a, end=" ")
    fib_under_limit(b, a+b, limit)


# fib_under_limit(0, 1, 20)

#----------------------------------------------

# # sum of an array
def array_sum(arr, index=0):
    if index == len(arr):
        return 0
    
    return arr[index] + array_sum(arr, index + 1)

# arr = [1,2,3,4]
# print(array_sum(arr))

# def sum_of_array(ar):
#     if len(ar) == 0:
#         return 0

#     return ar[0] + sum_of_array(ar[1:])

# print(sum_of_array([1,2,3,4]))

#-------------------------------------------------------

# s = "abcd"

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


# print(reverse_string(s))

#---------------------------------------------

def remove_charector(s, ch):
    if s == "":
        return ""
    
    if s[0] == ch:
        return remove_charector(s[1:], ch)
    else:
        return s[0] + remove_charector(s[1:], ch)
    
# print(remove_charector("banana", "a"))

#-------------------------------------------------------

def sum_of_even(s):
    if len(s) == 0:
        return 0
    if s[0] % 2==0:
        return s[0] + sum_of_even(s[1:])
    else:
        return sum_of_even(s[1:])
    
# print(sum_of_even([1,2,3,4]))


# def sum_of_even(arr, index=0):
#     if index == len(arr):
#         return 0
    
#     if arr[index] %2 ==0:
#         return arr[index] + sum_of_even(arr, index + 1)
#     else:
#         return sum_of_even(arr, index + 1)
    

# print(sum_of_even([1,2,3,4]))

#-----------------------------------------------------------

def removeduplicate(s, seen=None):
    if seen is None:
        seen = set()

    if s == "":
        return ""
    
    if s[0] in seen:
        return removeduplicate(s[1:], seen) 
    
    else:
        seen.add(s[0])
        return s[0] + removeduplicate(s[1:], seen)
    

# print(removeduplicate("banana"))

#--------------------------------------------------------------

def remove_duplicates(s, seen=None):
    if seen is None:
        seen = set()
    
    if s == "":
        return ""
    
    ch = s[0]
    
    if ch in seen:
        return remove_duplicates(s[1:], seen)
    else:
        seen.add(ch)
        return ch + remove_duplicates(s[1:], seen)
    
string = "programming"
    
# print(remove_duplicates(string))

#-----------------------------------------------------------
# back tracking

def subsets(s, current = ""):
    if s == "":
        print(current)
        return 
    
    subsets(s[1:], current + s[0])
    subsets(s[1:], current)
# subsets("ab")
#-------------------------------------------

def call_times(n = 1):
    if n > 5:
        return 
    print("call", n)
    call_times(n+1)

# # call_times()

#-------------------------------------

# def reverse_str(s):
#     if s == "":
#         return ""
#     return reverse_string(s[1:]) + s[0] 

# # print(reverse_str("hello"))

#------------------------------------- 
# def remove_c(s, char):
#     if s == "":
#         return ""
    
#     if s[0] == char:
#         return remove_c(s[1:], char)
#     return s[0] + remove_c(s[1:], char)

# # print(remove_c("axbxcdx", "x"))



# def remove_d(s, seen=None):
#     if seen == None:
#         seen = set()
    
#     if s =="":
#         return ""

#     if s[0] in seen:
#         return remove_d(s[1:], seen)
#     else:
#         seen.add(s[0])
#         return s[0] + remove_d(s[1:], seen)
    
# print(remove_d("mississippi"))


# def digit_sum(n):
#     if n ==0:
#         return 0
#     return n % 10 + digit_sum(n//10)

# print(digit_sum(3))

#------------------------------------------

# arr = [1, [2, 3], [4, [5, 6]], 7]

# def nested_ar_flat(ar):
#     result = []

#     for item in ar:
#         if isinstance(item, list):
#             result.extend(nested_ar_flat(item))
#         else:
#             result.append(item)
    
#     return result

    
# print(nested_ar_flat(arr))

#------------------------------------------------

def reverse_st(s):
    if s == "":
        return ""
    
    return  reverse_st(s[1:]) + s[0]

# print(reverse_st('abhiram'))




s = 'malayadlam'

def is_pal(s, i = 0 ,j = len(s)-1):

    if i >= j:
        return True
    
    if s[i] != s[j]:
        return False
    
    return is_pal(s, i+ 1 , j - 1)

# print(is_pal(s))