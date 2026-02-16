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
#regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

#import re
#x = "CDXXI"
#print(str(bool(re.match(regex_pattern, x))))
#----------------------------------------------------------------------------------------------------------------------------------
#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true
#output: DEXTER <dexter@hotmail.com>

#import email.utils
#import re

# Define a function to validate and print valid email lines
#def check(checking, numero):
    # Compile a regular expression to validate email format:
    # - Starts with a letter
    # - Followed by alphanumeric characters, dot, dash, or underscore
    # - Contains one '@' symbol
    # - Followed by domain (letters only)
    # - Followed by '.' and an extension of 1 to 3 letters
#    pattern = re.compile(r'^[a-zA-Z][\w\.\-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')

    # 'n' stores the number of lines to check
#    n = numero

    # Loop through each input line
#    for i in range(n):
#        line = checking[i]

        # Use parseaddr to extract the name and email address from the line
        # Example: "dheeraj <dheeraj-234@gmail.com>" => name='dheeraj', addr='dheeraj-234@gmail.com'
#        name, addr = email.utils.parseaddr(line)

        # Check if the extracted email address matches the regex pattern
#        if pattern.match(addr):
            # If valid, print the original input line
#            print(line)

# Main execution block
#if __name__ == '__main__':
    # Number of entries
#    n = 7

    # Input list of strings in format "name <email>"
#    inputs = [
#        "dheeraj <dheeraj-234@gmail.com>",
#        "crap <itsallcrap>",
#        "harsh <harsh_1234@rediff.in>",
#        "kumal <kunal_shin@iop.az>",
#        "mattp <matt23@@india.in>",
#        "harsh <.harsh_1234@rediff.in>",
#        "harsh <-harsh_1234@rediff.in>"
#    ]

    # Call the check function with the input list and count
#    check(inputs, n)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#You are given 0-50 lines of css code and you need to print out the colors with the "#" symbol in the order they are given. 
#https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true
#import re
#n = 5
#lines = [
    #"#.shadow {",
#    "{",
#    "       -moz-box-shadow:    inset 0 0 10px #000000;",
#    "       -webkit-box-shadow: inset 0 0 10px #000000;",
#    "       box-shadow:         inset 0 0 10px #0z00G0;",
#    "}"
#]

#pattern = r'#[a-zA-Z0-9]{3,6}[;|\)|,]'

#for line in lines:
#    matches = re.findall(pattern, line)
#    for match in matches:
#        print(match[:len(match)-1])
# ----------------------------------------------------------------------------------------------------------------------------------
# https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true
# HTML Parser - Part 1
# Goal: Parse a given HTML snippet and print out start tags, end tags, and empty tags along with their attributes and values.
# Note: Do NOT process anything inside comments.
# Sample input:
# <html><head><title>HTML Parser - I</title></head>
# <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
# Sample output:
# Start : html
# Start : head
# Start : title
# End   : title
# End   : head
# Start : body
# -> data-modal-target > None
# -> class > 1
# Start : h1
# End   : h1
# Empty : br
# End   : body
# End   : html
#Code starts here:
#from html.parser import HTMLParser


#n = 2
#input_lines = """<html><head><title>HTML Parser - I</title></head><body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>"""

#class MyHTMLParser(HTMLParser):
#    def handle_starttag(self, tag, attrs):
#        print("Start :", tag)
#        for attr in attrs:
#            name = attr[0]
#            value = attr[1] if attr[1] is not None else "None"
#            print(f"->{name} > {value}")

#    def handle_endtag(self, tag):
#        print("End :", tag)

#    def handle_startendtag(self, tag, attrs):
#        print("Empty :", tag)
#        for attr in attrs:
#            name - attr[0]
#            value = attr[1] if attr[1] is not None else "None"
#            print(f"-> {name} > {value}")

#    def handle_data(self, data):
#        print("Encountered some data  :", data)

#parser = MyHTMLParser()
#parser.feed(input_lines)
#-------------------------------------------------------------------------------------------------------------------------------------------
#Hackerrank practice https://www.hackerrank.com/challenges/html-parser-part-2/problem?isFullScreen=true
#Given N lines print the single line and multi-line comments as well as the data
# Sample Input:
# 4
# <!--[if IE 9]>IE9-specific content
# <![endif]-->
# <div> Welcome to HackerRank</div>
# <!--[if IE 9]>IE9-specific content<![endif]-->

#Sample Output:
# >>> Multi-line Comment
# [if IE 9]>IE9-specific content
# <![endif]
# >>> Data
#  Welcome to HackerRank
# >>> Single-line Comment
# [if IE 9]>IE9-specific content<![endif]

#Start Code here
#from html.parser import HTMLParser

#class MyHTMLParser(HTMLParser):
#    def handle_comment(self, data):
#        print(">>> Multi-line Comment")
#        print(data)
    
#    def handle_data(self, data):
#        print(">>> Data")
#        print(data)
  
  
#i = 4
#lines = ["<!--[if IE 9]>IE9-specific content"
#'<![endif]-->',
#'<div> Welcome to HackerRank</div>',
#'<!--[if IE 9]>IE9-specific content<![endif]-->']


#html = ""       
#for i in range(int(input())):
#    html += input().rstrip()
#    html += '\n'

#for count in range(0,i-1):
#    line = lines[count] 
#    parser = MyHTMLParser()
#    parser.feed(line)
#    parser.close()
#parser = MyHTMLParser()
#parser.feed(html)
#parser.close()    

#class MyHTMLParser(HTMLParser):
#    def handle_starttag(self, tag, attrs):
#        print("Start :", tag)
#        for attr in attrs:
#            name = attr[0]
#            value = attr[1] if attr[1] is not None else "None"
#            print(f"->{name} > {value}")

#    def handle_endtag(self, tag):
#        print("End :", tag)

#    def handle_startendtag(self, tag, attrs):
#        print("Empty :", tag)
#        for attr in attrs:
#            name - attr[0]
#            value = attr[1] if attr[1] is not None else "None"
#            print(f"-> {name} > {value}")

#    def handle_data(self, data):
#        print("Encountered some data  :", data)


#--------------------------------------------------------------------------------------------------------------------------------------------
#This will be a random test I want to build a script that will go through a txt file and count how many times each word appears. 
#Then print the top five most common words and their counts and for a bonus ignore punctuation
#import re

#my_dict = {}
#pattern = r"[a-zA-Z]"
#with open('example.txt','r') as file:
    #for line in file:
        #for word in line.split():
            #entry = ""
            #for letter in word:
                #x = re.search(pattern, letter)
                #if x:
                    #entry = entry + letter
                #if entry not in my_dict:
                    #my_dict[word] = 1
                #else:
                    #my_dict[word] += 1
#    
 #   sorted_dict = sorted(my_dict.items(), key=lambda item:item[1], reverse=True)
    #first_five = list(my_dict.items())[0:5]
    #for key,value in first_five:
        #print(f"{key}: {value}")
#------------------------------------------------------------------------------------------------------------------------------------------
#Given this input Input: "aabcccccaaa" make it output this Output: "a2b1c5a3"
#entered = "aabcccccaaa"
#entered = entered + "_"

#hold = []
#count = 0
#n = len(entered)-1

#for i in range(n):
    #letter = entered[i]

    #if i < n:
        #count += 1
        #if letter != entered[i+1]:
            #hold.append(letter)
            #hold.append(count)
            #count = 0

#print(hold)
#----------------------------------------------------------------------------------------------------------------------------------------------
#Set up the next challenge
# Input: nums = [2,7,11,15], target = 9 and output: [0,1]
# Given an array of integer nums and an inter target, retrn the indicies of the two numbers such that they add up to the target. 
#nums = [2,7,11,15]
#target = 13


#for first in nums:
#    for second in nums:
#        if first + second == target:
#            UNO = nums.index(first)
#            LAST = nums.index(second)
#            print(f'[{UNO}, {LAST}]')
#            exit()
#------------------------------------------------------------------------------------------------------------------------------------------
# Input: "abcabcbb" Output: 3 #"abc"
# Given a string s, find the length of the longest substring without repeating characters
# import re
# text = [
#     "abcabcbb",     # repeated pattern
#     "bbbbb",        # all same letter
#     "pwwkew",       # repeats but with breaks
#     "abcdefg",      # all unique
#     "dvdf",         # repeat after break
#     "abba",         # palindrome-like with repeats
#    "tmmzuxt",      # repeats mid-string
#     "",             # empty string
#     "a",            # single char
#     "aaabbbccc"     # grouped repeats
# ]

# for words in text:
#     sub = []
#     count = 0
#     for letter in words:
#         if letter not in sub:
#             sub.append(letter)
#             count += 1
#     print(count)
#------------------------------------------------------------------------------------------------------------------------------------------- 
#The goal of this practice will be to find the follow up score. Example n = 5, grades = [2,3,6,6,5] and output will be 5
# def runner_up(num, grades):
#    hold = []
#     for grade in grades:
#         if grade not in hold:
#             hold.append(grade)
#     hold.sort(reverse=True)
#     print(hold[1])
        

# if __name__ == '__main__':
#     n = 5
#     arr = [2,3,6,6,5]
#     runner_up(n, arr)
#-----------------------------------------------------------------------------------------------------------------------------------------
# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem?isFullScreen=true
# Desired output: 7.00+7.00i
# -3.00-5.00i
# 4.00+17.00i
# 0.26-0.11i
# 2.24+0.00i
# 7.81+0.00i
#---------
# import math 
#--------- 
# class Complex(object): 
#     def __init__(self, real, imaginary): 
#         self.real = real 
#         self.imaginary = imaginary 
#---------         
#     def __add__(self, no): 
#         real_sum = self.real + no.real 
#         imaginary_sum = self.imaginary + no.imaginary 
#         return Complex(real_sum, imaginary_sum) 
#---------         
#     def __sub__(self, no): 
#         real_sub = self.real - no.real 
#         imaginary_sub = self.imaginary - no.imaginary 
#         return Complex(real_sub, imaginary_sub) 
#---------         
#     def __mul__(self, no): 
#         a, b = self.real, self.imaginary 
#         c, d = no.real, no.imaginary 
#         return Complex(a*c - b*d, a*d + b*c) 
#---------
#     def __truediv__(self, no): 
#         a, b = self.real, self.imaginary 
#         c, d = no.real, no.imaginary 
#         denom = c*c + d*d 
#         return Complex((a*c + b*d) / denom, (b*c - a*d) / denom) 
#---------
#     def mod(self): 
#         return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0) 
#---------
#     def __str__(self): 
#         if self.imaginary == 0: 
#             result = "%.2f+0.00i" % (self.real) 
#         elif self.real == 0: 
#             if self.imaginary >= 0: 
#                 result = "0.00+%.2fi" % (self.imaginary) 
#             else: 
#                 result = "0.00-%.2fi" % (abs(self.imaginary)) 
#         elif self.imaginary > 0: 
#             result = "%.2f+%.2fi" % (self.real, self.imaginary) 
#         else: 
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary)) 
#         return result 

# if __name__ == '__main__': 
#     # Hard-coded sample input 
#     C = [2.0, 1.0] 
#     D = [5.0, 6.0] 
#     x = Complex(*C) 
#     y = Complex(*D) 
#     print(x + y) 
#     print(x - y) 
#     print(x * y) 
#     print(x / y) 
#     print(x.mod()) 
#     print(y.mod()) 
#-----------------------------------------------------------------------------------------------------------------------------------------
# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem?isFullScreen=true
# Goal: print torsional angle (degrees) correct to 2 decimals
# (Do not solve here yet — just setup)
#import math

#class Points(object):
    # This class is a BLUEPRINT.
    # Nothing runs until an object is created from it.

#    def __init__(self, x, y, z):
        # This method runs AUTOMATICALLY when you create a Points object.
        #
        # Example call:
        #   p = Points(1, 2, 3)
        #
        # Python internally does:
        #   p = Points.__new__(Points)
        #   Points.__init__(p, 1, 2, 3)
        #
        # So:
        #   self -> p   (the newly created object)
        #   x, y, z -> 1, 2, 3
        #
        # These assignments store values INSIDE the object.
#        self.x = float(x)   # p.x now exists
#        self.y = float(y)   # p.y now exists
#        self.z = float(z)   # p.z now exists


#    def __sub__(self, no):
        # This method is called when you use the "-" operator.
        #
        # Example:
        #   v = p2 - p1
        #
        # Python converts that to:
        #   v = Points.__sub__(p2, p1)
        #
        # So:
        #   self -> p2
        #   no   -> p1
        #
        # self.x means "p2.x"
        # no.x   means "p1.x"
        #
        # We CREATE A NEW Points object and RETURN IT.
        # Nothing modifies p1 or p2.
#        return Points(
#            self.x - no.x,   # new object's x
#            self.y - no.y,   # new object's y
#            self.z - no.z    # new object's z
#        )


#    def dot(self, no):
        # This method is called when you do:
        #   a.dot(b)
        #
        # Python converts that to:
        #   Points.dot(a, b)
        #
        # So:
        #   self -> a
        #   no   -> b
        #
        # This method RETURNS A NUMBER (float).
        # It does NOT create a new Points object.
        #
        # The returned value is sent back to the caller.
#        return (self.x * no.x + self.y * no.y + self.z * no.z)


#    def cross(self, no):
        # This method is called when you do:
        #   a.cross(b)
        #
        # Python converts that to:
        #   Points.cross(a, b)
        #
        # So:
        #   self -> a
        #   no   -> b
        #
        # This method CREATES AND RETURNS A NEW Points object.
        #
        # That returned object can be stored in a variable:
        #   c = a.cross(b)
        #
        # c is now a completely separate Points instance.
#        return Points(self.y * no.z - self.z * no.y, self.z * no.x - self.x * no.z, self.x * no.y - self.y * no.x)


#    def absolute(self):
        # This method is called when you do:
        #   length = v.absolute()
        #
        # Python converts that to:
        #   Points.absolute(v)
        #
        # So:
        #   self -> v
        #
        # This method uses ONLY data stored INSIDE self.
        # It RETURNS A NUMBER.
        #
        # No new Points object is created.
#        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)



#if __name__ == '__main__':
#    p1 = Points(0, 4, 5)
#    p2 = Points(1, 7, 6)
#    p3 = Points(0, 5, 9)
#    p4 = Points(1, 7, 2)


#    a = p2 - p1  
#    b = p3 - p2  
#    c = p4 - p3  

#    x = a.cross(b)  
#    y = b.cross(c)  

#    denom = x.absolute() * y.absolute()  
#    cos_theta = x.dot(y) / denom  

    # Clamp for numeric stability (avoid acos domain errors)  
#    cos_theta = max(-1.0, min(1.0, cos_theta))  

#    angle = math.degrees(math.acos(cos_theta))  
#    print(f"{angle:.2f}")
# =================================================================================================
# ORIGINAL PRACTICE (COMMENTED OUT)
# HackerRank: XML2 - Find the Maximum Depth
# =================================================================================================

# import xml.etree.ElementTree as etree
#
# # This will store the maximum depth found during recursion
# maxdepth = 0
#
# def depth(elem, level):
#     """
#     elem  -> current XML element (node) being processed
#     level -> current depth in the XML tree
#     """
#
#     global maxdepth
#
#     # Increase the current level
#     level += 1
#
#     # Update maxdepth if needed
#     if level > maxdepth:
#         maxdepth = level
#
#     # Recurse through children
#     for child in elem:
#         depth(child, level)
#
#
# if __name__ == '__main__':
#     # Hardcoded sample input (XML with depth = 6)
#     n = 13
#     xml = (
#         "<root>\n"
#         "    <a>\n"
#         "        <b>\n"
#         "            <c>\n"
#         "                <d>\n"
#         "                    <e>\n"
#         "                        <f>Deep</f>\n"
#         "                    </e>\n"
#         "                </d>\n"
#         "            </c>\n"
#         "        </b>\n"
#         "    </a>\n"
#         "</root>\n"
#     )
#
#     tree = etree.ElementTree(etree.fromstring(xml))
#     depth(tree.getroot(), -1)
#     print(maxdepth)


# =================================================================================================
# NEW PRACTICE SETUP
# HackerRank: Piling Up!
#Learn how to work with Deque popleft, pop, etc. 
# =================================================================================================

from collections import deque

def can_stack_cubes(blocks):
    m = len(blocks)
    middle = 0

    if m%2==0:
        middle = (m-1)//2
    else:
        middle = m//2
    #print(middle)
    
    left = blocks[0]
    right = blocks[-1]

    if left >= right:
        print(left)
        if blocks.index(left) == middle:
            blocks = blocks.popleft()
            return True
    elif left <= right:
        print(right)
        if blocks.index(right) == middle:
            return True
    else:
        #return False
        pass



if __name__ == '__main__':
    # Hardcoded sample input (mirrors HackerRank format)

    T = 2  # number of test cases

    test_cases = [
        [4, 3, 2, 1, 3, 4],  # Expected: Yes
        [1, 3, 2]           # Expected: No
    ]

    for blocks in test_cases:
        # Convert list to deque for efficient pops from both ends
        cube_deque = deque(blocks)

        # Run your logic
        result = can_stack_cubes(cube_deque)

        # Print result in HackerRank format
        print("Yes" if result else "No")
