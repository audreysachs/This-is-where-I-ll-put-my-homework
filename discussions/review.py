#problem 1
'''
list = [2,3,'hello','six']

dictionary = {
    '2': [1,2,4,8], '3': [1,3,9,27], 'hello': ['hello','hello','hello','hello'], 'six': ['six','six','six','six']
}


print (dictionary)
'''

new_dict = dict()
list = [2,3,'hello','six']

for i in list:
   # print (i) #helps debug
    if type(i) == int:
        new_list = [i**0, i**1, i**2, i**3]
        print(new_list)
    elif isinstance(i, str): #is instance is just another way to say if 
        new_list = [i*4]
        print(new_list)
    new_dict[i] = new_list



'''
#problem 2

num=29

if num == 0 or num == 1: #if it's equal to 1 or zero, it's not prime
    print (num, False)
elif num > 1:
    for i in range(2,num):
        if (num % i) == 0: #if it can be divided, its not prime
            print(num, False)
            print(i, "times", num//i, "is", num) 
    else:
         print (num, True) #if it can't be divided its prime
else:
    print (num, False) #because num must be negative, less than one 

'''


