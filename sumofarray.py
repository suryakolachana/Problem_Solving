import os
import sys

def sumofarray(n):
    var = 0

    for i in n:
        var += i
    return var

if __name__ == '__main__':
    
    ar_count = int(input())
    ar = list(map(int,input().rstrip().split()))
    print(ar)
    #ar = [1,2,3,4]
    #result = sumofarray(ar)
    #print(result)
