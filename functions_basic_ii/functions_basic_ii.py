#1
def countdown(num):
    list = []
    for x in range (0, num + 1, 1):
        list.append(num - x)
    return list

print(countdown(5))

#2
def pr(list):
    print(list[0])
    return(list[1])

print(pr([6,5]))

#3
def first_plus_len (list):
    sum = list[0] + len(list)
    return sum

print(first_plus_len([6,8,7]))

#4
def values_greater_than_2(list):
    newlist = []
    counter = 0
    if (len(list) < 2):
        return False

    for i in range (0, len(list), 1):
        if (list[i] > list[1]):
            newlist.append(list[i]) 
            counter += 1

    print(counter)

    return newlist

print(values_greater_than_2([5,2,3,2,1,4]))

#5
def size_and_value(size, value):
    list = []
    for i in range(0,size):
        list.append(value)
    return list

print(size_and_value(6,5))

