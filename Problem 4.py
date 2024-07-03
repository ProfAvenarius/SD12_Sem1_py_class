#Description: Program playing with lists of numbers
#Author: DC Elliott
#Date: July 3/2024

#Program Libraies

import random

#Program Constants

Num_List =[]


#Program Functions

def MakeList(length):
    #Makes a list of values as long as entered, values random from 1-100 unless entered manually
    x = 0
    while x in range(0,length):
        y = random.randint(1,100)
        num_choice = input(f"Enter 'return' key to use {y} or enter 'N' to enter your own?").capitalize()
        if num_choice == "N":
            z = int(input("Enter a number from 1 to 100. Enter '-1' to end"))
            if z == -1:
                break
            else:
                Num_List.append(z)
        else:
            Num_List.append(y)
        x += 1
    return Num_List

def SortList(Unsorted):
    #Returns sorted low to high inputed list
    Unsorted.sort()
    return Unsorted

def HighLow(List):
    #Returns high and low value
    length = len(List)
    List.sort()
    low = List[0]
    high = List[length-1]
    return (low,high)

def TotalList(List):
    #Returns total of list
    length = len(List)
    x=0
    total = 0
    while x in range(0,length):
        total += List[x]
        x += 1
    return total

def AveList(List):
    #Returns average value
    length = len(List)
    x=0
    total = 0
    while x in range(0,length):
        total += List[x]
        x += 1
    average =total/length
    return average

def FindDups(List):
    #Returns duplicate values on list if they exist
    Dup_Nums =[]
    length = len(List)
    for x in range(0,length):
        test = List[x]
        reps = List.count(test)
        no_reps =Dup_Nums.count(test)
        if reps != 1 and no_reps == 0:
            Dup_Nums.append(test)
    if len(Dup_Nums) == 0:
        return "NO DUPLICATES"
    else:
        return Dup_Nums

#Program Main
print()
print()

nums = int(input("How long of a list of numbers would you like?  "))

Num_List =MakeList(nums)

Num_Dsp = Num_List.copy()

Num_Sort = SortList(Num_List)

num_total = TotalList(Num_List)

num_ave = AveList(Num_List)

High_Low = HighLow(Num_List)
num_low = High_Low[0]
num_high = High_Low[1]

Num_Dup = FindDups(Num_List)

print()
print()
print (f"YOUR LIST AS ENTERED: {Num_Dsp}")

print()
print()
print (f"YOUR LIST SORTED: {Num_Sort}")
print()
print()
print (f"THE TOTAL VALUE OF YOUR LIST: {num_total}")
print()
print()
print (f"THE AVERAGE VALUE OF YOUR LIST: {num_ave}")
print()
print()
print (f"THE LOW VALUE ON YOUR LIST: {num_low}")
print()
print()
print (f"THE HIGH VALUE ON YOUR LIST: {num_high}")
print()
print()
print (f"THE DUPICATE VALUES ON YOUR LIST: {Num_Dup}")
print()
print()
print()
print()



