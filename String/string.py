# def reverse_string(s):
#     ch = list(s)

#     left = 0
#     right = len(ch) -1

#     while left < right:
#         ch[left], ch[right] = ch[right], ch[left]
#         left += 1
#         right -= 1

#     return "".join(ch)

# rev = reverse_string("abhiram")
# print(rev)

#------------------------------------------------------
#reverse each word using a helper function
# s = "hello world"

# lst = s.split()
# res = []
# for i in lst:
#     res.append(reverse_string(i)) # helper function from above

# print(" ".join(res))

#---------------------------------------------------------------------------------
# def reverse_each_word(s):
#     char = list(s)
#     n = len(char)
#     start = 0

#     for i in range(n + 1):
#         if i == n or char[i] == " ":
#             left,right = start , i - 1
#             while left < right:
#                 char[left], char[right] = char[right], char[left]
#                 left += 1
#                 right -= 1
#             start = i + 1
#     return "".join(char)

# print(reverse_each_word("hello world"))

#----------------------------------------------------------------------

# def remove_extra_space(s):
#     result = []
#     prev_space = True   #to treat start as space to avoid starting space

#     for i in s:
#         if i != ' ':
#             result.append(i)
#             prev_space = False
#         else:
#             if not prev_space:
#                 result.append(' ')
#                 prev_space = True

#     if result and result[-1] == ' ':
#         result.pop()

#     return "".join(result)

# print(remove_extra_space("   hello    world   "))

#--------------------------------------------------------------------------------

# def extract_digits(s):
#     res = []

#     for i in s:
#         if '0' <= i <= '9':
#             res.append(i)

#     return "".join(res)

# print(extract_digits("ab12cd034"))

#--------------------------------------------------------------

# def title_case(s):
#     res =[]
#     capitalize = True

#     for i in s:
#         if i ==' ':
#             res.append(i)
#             capitalize = True
#         else:
#             if capitalize and 'a' <= i <= 'z':
#                 res.append(chr(ord(i) - 32))
#             else:
#                 res.append(i)
#             capitalize = False

#     return "".join(res)

# print(title_case("   dsa   is fun"))

#-----------------------------------------------------------

# def is_palindrome(s):
#     l = 0
#     r = len(s) - 1

#     while l < r:
#         if s[l] != s[r]:
#             return False
#         l += 1
#         r -= 1
#     return True

# print(is_palindrome("madam"))

#--------------------------------------------------------------

# def first_non_repeating(s):
#     f = {}

#     for i in s:
#         f[i] = f.get(i, 0) + 1

#     for i in s:
#         if f[i] == 1:
#             return i
#     return None

# print(first_non_repeating("hello"))

# s = "helloho"
# f = {}

# for i in s:
#     f[i] = f.get(i, 0) + 1

# for i in s:
#     if f[i] ==1:
#         print(i)
#         break
#-----------------------------------------------------------------

# def last_non_repeating(s):
#     f = {}

#     for i in s:
#         f[i] = f.get(i, 0) +1

#     for i in range(len(s) - 1, -1, -1):
#         if f[s[i]] ==1:
#             return s[i]
        
#     return None

# print(last_non_repeating("hello"))

#------------------------------------------------------------------

# def check_anagram(s, b):
#     if len(s) != len(b):
#         return False
#     f1 = {}
#     f2 = {}
    
#     for i in s:
#         f1[i] = f1.get(i, 0) +1

#     for i in b:
#         f2[i] = f2.get(i, 0) +1
    
#     return f1 == f2

# print(check_anagram("aabb", "bbea"))


# def check_anagram(s, b):
#     if len(s) != len(b):
#         return False
    
#     f = {}

#     for i in s:
#         f[i] = f.get(i, 0) + 1

#     for i in b:
#         if i not in f:
#             return False
#         f[i] -= 1
#         if f[i] < 0:
#             return False
    
#     return True

# print(check_anagram("aabb", "bba"))

#--------------------------------------------------------

#longest substring without repeating charectors(length)

# def non_repeating_substring(s):
#     seen = set()
#     l = 0
#     max_len = 0

#     for i in range(len(s)):
#         while s[i] in seen:
#             seen.remove(s[l])
#             l += 1

#         seen.add(s[i])
#         max_len = max(max_len, i - l +1)

#     return max_len

# print(non_repeating_substring("abcbadbgh"))

#---------------------------------------------------------------

#  longest substring without vowels 

# def longest_no_vowel_substring(s):
#     vowels = {'a', 'e', 'i', 'o', 'u'}
#     left = 0
#     max_len = 0

#     for i in range(len(s)):
#         if s[i] in vowels:
#           left = i + 1
#         else:
#            max_len = max(max_len, i - left + 1)

#     return max_len

# print(longest_no_vowel_substring("earthproblem"))
#---------------------------------------------------------------

# def is_valid_parantheses(s):
#     stack = []
#     mapping = {
#         ')': '(',
#         '}': '(',
#         ']': '['
#     }

#     for i in s:
#         if i in mapping.values():
#             stack.append(i)

#         elif i in mapping:
#             if not stack or stack[-1] != mapping[i]:
#                 return False
#             stack.pop()

#     return len(stack) == 0

# print(is_valid_parantheses("(([]){}"))
#------------------------------------------------------------

def replace_alphabet(s, n):
    result = ""

    for i in s:
        if i.isalpha():
            pos = ord(i) - ord("a")
            new_pos = (pos + n) % 26
            result += chr(new_pos + ord("a"))
        else:
            result += i
            
    return result

# print(replace_alphabet("abc", 2))


# def replace_charector(string, n):
#     result = ""

#     for i in string:
#         if i.isalpha():
#             pos = ord()


users = [
  { "name":"Ayan", "age" :21 },
  { "name": "Rahul", "age":25 },
  { "name": "Neha","age": 19 }
]




for i in users:
    i["gender"] = "male"
    
# print(users)

s = "hello world"
