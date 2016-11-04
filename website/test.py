'''

x = int(input("Priority "))

for i in range(0,7):
    # print (i)
    if (x & (x-1)) != 0:
        exit #print("Invalid sequency priority")
    else:
        print("All good")

'''


def TwoPowerPriorityCheck(x,count):
    if x != 0 & x > 2 ** (count-1):
        return ((x & (x - 1)) == 0) # Bitwise AND will indicate if this agrees 2 power x
    else:
        return False

print(TwoPowerPriorityCheck(256,7))


