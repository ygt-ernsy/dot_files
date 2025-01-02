
def çarpan(num):
    çar = []
    for i in range(1,num+1):
        if num % i == 0:
            çar.append(i)
    print(çar)
def is_prime(num):
    if num > 1:
        for i in range(2, int(num ** (1 / 2)) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False

def factor(num):
    fac = 1
    for i in range(1,num+1):
        fac = fac * i
    print(fac)

#################################################################################
#LIST REVERSE# #BAD#
#function that makes a list from input
#and reverses said list
'''def list_Reverse(list):
    list1 = []
    keep = True
    #make a list from input
    while keep == True:
        num = int(input("How many elenents will you add: "))
        for i in range(1,num+1):
            listE = input(f"Add the {i}. element to the list: ")
            list1.append(listE)
        keep_going = input("Do you want to add any more elemets. Write 'yes' if yes")
        if keep_going != "yes":
            break
    #The function that reverses the list
    def listReverse(rev):
        rev2 = []
        for i in range(len(rev)):
            rev2.append(rev[-i-1])
        rev = rev2
        print(rev)
    listReverse(list1)'''
#list[::-1]
#list.reverse()
##########################################
def countNumberOfDtudentsThatFail(file):
    fail = 0
    for line in file:
        if int(line)<50:
            fail += 1
    return fail
#########################################
