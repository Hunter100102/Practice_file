#Take input string and seperate it based at the , and the . and then print so if its 100,000.000 then print 100 000 and 000 on seperate
#lines
#regex_pattern = r"[,.]"	# Do not delete 'r'.

#import re
#print("\n".join(re.split(regex_pattern, "100,000,000.000")))



#You are given a string and you need to find the first occurance of the repeating alphanumeric character, and if there is not one the print -1.
#import re

#s = "__commit__"

#match = re.search(r'([a-zA-Z0-9])\1', s)

#if match:
    #print(match.group(1))
#else:
    #print(-1)

#You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
#Your task is to find all the substrings of  that contains  or more vowels.
#Also, these substrings must lie in between  consonants and should contain vowels only.


#----------------------------Next task----------------------
#determine how many apples and oranges fall on the house and print that value. 
#The first line is s and t, second is a and b, third, m and n, fourth distances from a, final distances from b

#def countApplesAndOranges(s,t,a,b,apples,oranges):
#    house = []
#    apples_that_landed = 0
#    oranges_that_landed = 0
#    for i in range(s,t+1):
#        house.append(i)
    
#    for num in apples:
#        landed = a + num
#        if landed in house:
#            apples_that_landed += 1

#    for num in oranges:
#        landed = num + b
#        if landed in house:
#            oranges_that_landed += 1

#    print(apples_that_landed)
#    print(oranges_that_landed)


#if __name__ == '__main__':
#    s = 7  # Starting point of Sam's house
#    t = 11  # Ending point of Sam's house
#    a = 5  # Location of the apple tree
#    b = 15  # Location of the orange tree
#    apples = [-2, 2, 1]  # Distances of apples from the apple tree
#    oranges = [5, -6]  # Distances of oranges from the orange tree
#    countApplesAndOranges(s, t, a, b, apples, oranges) 
 #building the house variable is not necessary and creates more latency that is needed, an if statement with a range can be used if speed is needed. 

#---------------------------------------------------------------------------------------------------------------------------------------------------
#Keeping score

#values = {'Alice': 0,'Bob': 0}

#def compareTriplets(a, b):
    # Write your code here
    #for i in range(len(a)):
        #if a[i]>b[i]:
            #print(a[i])
            #values['Alice'] += 1
        #elif a[i]==b[i]:
            #x=0
        #else:
            #print(b[i])
            #values['Bob'] += 1
            
    #print(values['Alice'], values['Bob'])

#if __name__ == '__main__':
    #a=[5,6,7]
    #b=[3,6,10]

    #compareTriplets(a,b)

#def aVeryBigSum(ar):
    #sum = 0
    #for num in ar:
        #sum += int(num)
        
    #print(sum)

#if __name__ == '__main__':
    #x = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    #aVeryBigSum(x)

#Diagnal matrix setup



# def diagonalDifference(arr):
#     # Write your code here
#     sum_1 = 0
#     sum_2 = 0
#     for i in range(len(arr)):
#         sum_1 += arr[i][i] 
#         sum_2 += arr[i][len(arr) - 1 - i] 

#     print(abs(sum_1-sum_2)) 

# if __name__ == '__main__':
#     x = [[1, 2, 3],
#            [4, 5, 6],
#            [9, 8, 9]]

#     diagonalDifference(x)


#Ratio of of neg, pos, and 0
#def plusMinus(arr):
    # Write your code here
#    neg = 0
    #pos = 0
    #zero = 0
    
    #for num in arr:
        #if num < 0:
            #neg += 1
        #elif num > 0:
            #pos += 1
        #else:
            #zero += 1
        
    #print(round(neg/n, 6))
    #print(round(pos/n, 6))
    #print(round(zero/n, 6))


#if __name__ == '__main__':
    #n = 6
    #x = [-4, 3, -9, 0, 4, 1]
    #plusMinus(x)

#---------------------------------------------------------------------------------------------------------------------------

#Runner up
#if __name__ == '__main__':
    #n = 5
    #arr = [2,3,6,6,5]

    #A = []
    #for num in arr:
        #if num not in A:
            #A.append(num)
    
    #A = sorted(A,reverse=True)
    #print(A[1])
#----------------------------------------------------------------------------------------------------------------------------------
# You are given a string .
#  contains alphanumeric characters only.
# Your task is to sort the string  in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

# Input Format
# A single line of input contains the string .

# Constraints

# Output Format
# Output the sorted string .

# Sample Input
# Sorting1234

# Sample Output
# ginortS1324

#s = input()
#def sorting(s):
   # l = ''
  #  u = ''
 #   oddn = ''
#    evenn = ''
    #lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
   # oddnum = ['1','3','5','7','9']
  #  evennum = ['0','2','4','6','8']

 #   for letter in s:
#        if letter in lower:
        #    l = l + letter
       # elif letter in upper:
      #      u = u + letter
     #   elif letter in oddnum:
    #        oddn = oddn + letter
   #     elif letter in evennum:
  #          evenn = evenn + letter

 #   ol = ''.join(sorted(l))
#    ou = ''.join(sorted(u))
    #odn = ''.join(sorted(oddn))
   # oen = ''.join(sorted(evenn))

  #  unsorted_full = ol+ou+odn+oen
 #   print(unsorted_full)

#if __name__ == '__main__':
#    x = '1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM'
    #sorting(x)

#------------------------------------------------------------------------------------------------------------------------------------REGEXS!!!!!!!

# import re

# if __name__ == '__main__':
#     n = 5
#     test_cases = ["1.414", "+.5486468", "0.5.0", "1+1.0","0"]

#     for test in test_cases:
#         if re.match(r"^(\+|-|.)",test):
#             if re.match(r"^[^.]*\.[^.]*$", test):
#                 print("True")
#             else:
#                 print("False")

# ^[+-]?: Matches an optional + or - at the start.
# \d*: Matches zero or more digits before the decimal point.
# \.: Matches a literal dot (decimal point).
# \d+: Matches one or more digits after the decimal point.
# $: Ensures the match is for the entire string.

# import re

# if __name__ == '__main__':
#     n = int(input())
    
#     for i in range(n):
#         test = input().strip()
#         # Check if the input is a valid decimal number
#         if re.match(r"^[+-]?\d*\.\d+$", test):
#             print("True")
#         else:
#             print("False")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
#Your task is to find all the substrings of  that contains  or more vowels.
#Also, these substrings must lie in between  consonants and should contain vowels only.

#import re
#s = input()
#Expected output: aa
#aa
#aa
#s = "rabcdeefgyYhFjkIoomnpOeorteeeeet"

#x = re.findall(r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])',s)


#if not x:
    #print("-1")
#else:
    #for items in x:
        #print(items)
#-----------------------------------------------------------------------MORE REGEX------------------------------------------------------------------------------------------------
#Expected output
#(0,1)
#(1,2)
#(4,5)
#Print the tuple in and find the indicies of the start and end of string k in s


#import re
#def startnend(a,b):
#    pattern = re.compile(b) #This could create a regular expression object by compiling a regular expression pattern
#    #Output: re.compile('aa')
#    r = pattern.search(a) #This searches through strings and checks the indices 
#    if not r: print("(-1, -1)") #If a [] empty set is returned
#    while r:
#        print("({0}, {1})".format(r.start(), r.end() - 1))
#        r = pattern.search(a,r.start() + 1)


#if __name__ == '__main__':
#    #s = input()
#    #k = input()
#    s = "aaadaa"
#    k = "aa"

#    startnend(s,k)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true
# The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
# The method is called for all matches and can be used to modify strings in different ways.
# The re.sub() method returns the modified string as an output.

# Learn more about .

# Transformation of Strings

# Code

# import re

# # Squaring numbers
# def square(match):
#     number = int(match.group(0))
#     return str(number**2)

# print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))
# Output

# 1 4 9 16 25 36 49 64 81

# Replacements in Strings

# Code

# import re

# html = """
# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash" 
#   data="your-file.swf" 
#   width="0" height="0">
#   <!-- <param name="movie"  value="your-file.swf" /> -->
#   <param name="quality" value="high"/>
# </object>
# """

# print(re.sub("(<!--.*?-->)", "", html)) # remove comment
# Output

# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash" 
#   data="your-file.swf" 
#   width="0" height="0">

#   <param name="quality" value="high"/>
# </object>

# Task

# You are given a text of  lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following:

# && → and
# || → or
# Both && and || should have a space " " on both sides.

# Input Format

# The first line contains the integer, .
# The next  lines each contain a line of the text.

# Constraints

# Neither && nor || occur in the start or end of each line.

# Output Format

# Output the modified text.

# Sample Input

# 11
# a = 1;
# b = input();

# if a + b > 0 && a - b < 0:
#     start()
# elif a*b > 10 || a/b < 1:
#     stop()
# print set(list(a)) | set(list(b)) 
# # Note do not change &&& or ||| or & or |
# # Only change those '&&' which have space on both sides.
# # Only change those '||' which have space on both sides.

# Sample Output

# a = 1;
# b = input();

# if a + b > 0 and a - b < 0:
#     start()
# elif a*b > 10 or a/b < 1:
#     stop()
# print set(list(a)) | set(list(b)) 
# # Note do not change &&& or ||| or & or |
# # Only change those '&&' which have space on both sides.
# # Only change those '||' which have space on both sides.

# Language
# Pypy 3
# More
# 1
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# Line: 1 Col: 70

# Start code here
#import re

#def fix(match):
#    if match.group(0) == '||':
#        return 'or'
#    elif match.group(0) == '&&':
#        return 'and'

#if __name__ == '__main__':
    # num = int(input())
    # lines = input()
    # num = 11  # Number of lines in the input
    # lines = [
    #    "a = 1;",
    #    "b = input();",
    #    "",
    #    "if a + b > 0 && a - b < 0:",
    #    "    start()",
    #    "elif a*b > 10 || a/b < 1:",
    #    "    stop()",
    #    "print set(list(a)) | set(list(b)) ",
    #    "# Note do not change &&& or ||| or & or |",
    #    "# Only change those '&&' which have space on both sides.",
    #    "# Only change those '||' which have space on both sides."
    # ]

    # for item in lines:
    #    text = re.sub(r'\|\||&&', lambda m: fix(m), item)
    #    print(text)
#-----------------------------------------------------------------------------------------------------------------------------------
#https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=true
#There has got to be a better way to do this, its too much repeated stuff. 
regex_pattern = r"(XMMM|XMM|XM|M)(DDD|DD|D)(XCCC|XCC|XC|X)(XLLL|XLL|XL|L)(IXXX|IXX|IX|X)(IVVV|IVV|IV|V)(III|II|I|)"	# Do not delete 'r'.

import re
x = "CDXXI"
print(str(bool(re.match(regex_pattern, x))))
