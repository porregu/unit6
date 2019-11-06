def get_list():
    '''

    :return:this get a list of number, only the user need to type the higest number
    '''
    number=int(input("what you want to be your maximun number?"))# this line ask the user for a number to be the higest number
    list=[]# this creat a blank list to put the numbers in
    for x in range(2, number+1):# this loop make to put the first number in the blank list
            list.append(x)
    return list

def get_primes(list):
    '''

    :param list:this function show the primes of the list give above by the user
    :return:
    '''
    primes=[]# this creat a blank list to put the numbers in
    while len(list)>0:# this shows all the numbers in the list until the higest number put by the user
        track=list[0]# this is blank list to keep track of numbers
        primes.append(list[0])# this take the list numners and added to primes
        for x in list:# this is a loop for reapeating the proces until is done
            if x%track==0:# this will add all the numbers that divided by "track" are not equal to 0
                list.remove(x)# this will remove all the numbers that divided by track equal 0
    print("this is your prime numbers", primes)
def main():
    list=get_list()
    get_primes(list)

main()