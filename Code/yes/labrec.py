def fact(num):
    if num == 0:
        return 1

    return num * fact(num-1)

def sum_list(list_of_numbers,index):
    if index < 0:
        return 0
    return list_of_numbers[index] + sum_list(list_of_numbers,index-1)

list_of_numbers = [1,2,3,4,3]
print(sum_list(list_of_numbers,len(list_of_numbers)-1))
print(fact(5))
