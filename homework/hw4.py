#2.1
audreylist = []
for x in range(21):
    audreylist = audreylist+[x]
print(audreylist)


  #File "/Users/audreysachs/Desktop/This-is-where-I-ll-put-my-homework/homework/hw4.py", line 4, in <module> audreylist = audreylist+x
  #i had to make x in the list so had to put brackets around it


#2.2
squarelist = []
for i in audreylist:
    squarelist=squarelist+[i**2]
print(squarelist)

  #  File "/Users/audreysachs/Desktop/This-is-where-I-ll-put-my-homework/homework/hw4.py", line 13, in <module>
   # squarelist=audreylist**2
#TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
#i had to do another for loop and make i go through audrey list and square each term

#2.3
slicelist = squarelist[0:15]
print(slicelist)

#2.4
fivelist = squarelist[4:21:5]
print(fivelist)

#2.5
fancylist=squarelist[21:0:-1]
extrafancylist=fancylist[0:21:3]
print(extrafancylist)

#3.1

matrix=[]
for g in range(5):
    smalllist=[]
    for f in range(5):
        smalllist= smalllist+[1+f+g*5]
    matrix= matrix+[smalllist]
print(matrix)

#Traceback (most recent call last): File "/Users/audreysachs/Desktop/This-is-where-I-ll-put-my-homework/homework/hw4.py", line 41, in <module>  matrix = matrix+[f+5*gu] NameError: name 'gu' is not defined
#accidentally added u--had to delete

#3.2
def question3(matrix):
    for i in range(5):
       for g in range(5):
            if matrix[i][g]%3 == 0:
             matrix[i][g] = '?'
    return matrix

print(question3(matrix))
        
#File "/Users/audreysachs/Desktop/This-is-where-I-ll-put-my-homework/homework/hw4.py", line 53, in <module> if matrix[0:i][0:g]%3 == 0:
#had to put only the integer


#3.3


def sumofmatrix(matrix):
    c=0
    for i in range(5):
        for g in range(5):
            if matrix[i][g] != '?':
                c = matrix[i][g]+c 
    return c
print(sumofmatrix(matrix))

