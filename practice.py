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
