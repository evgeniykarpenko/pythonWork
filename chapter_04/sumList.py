def sumList(list):
    if list == []:
        return 0
    return list[0] + sumList(list[1:])


list = [1,2,3,4,5]
print(sumList(list))
