
#problem 1

#x**y is the same as x*x*x... y amount of times
#so have to use a loop
#also must have a defined function for multiplication 

x=2
y=3

def power(base,exponent):
    result = 1 #result=1 because we need 2**1=2 which is new result which loops to result*base (2*2)=4 when y=2
    for i in range(exponent):
        result = result * base 
    return result
print(power(x,y))



#problem 2

readings = [15, 14, 17, 20, 23, 28, 20]
#print(readings)

min_readings = min(readings)
max_readings = max(readings)
temperatureRange = (min_readings,max_readings)
print (temperatureRange)

print(type(temperatureRange))



#problem 3




def isWeekend(day):
    if (day == 6 or day == 7):
        return True
    else:
        return False

day = 3
print(isWeekend(day))

#problem 4

distance = 70
fuel = 21.5

def fuel_efficiency(distance,fuel):
    result = distance/fuel 
    result = round(result, 2) #can make result= two seperate things
    return result
print(fuel_efficiency(distance,fuel))

#problem 5


def firstDigit(n):
    c = 0
    firstdigs = n // 10
    lastdig = n%10

    while n >= 10:
     n=n/10
     c += 1
    
    return (lastdig * (10 ** c)) + firstdigs

print(firstDigit(12345))

#6.1

nums = [2024, 98, 131, 2, 3, 72]

def find_min_with_for_loop(nums):
    min_value = nums[0]
    for i in nums:
        if i<=min_value:
            min_value=i
    return min_value
print(find_min_with_for_loop(nums))

def find_max_with_for_loop(nums):
    max_value = nums[0]
    for i in nums:
        if i>=max_value:
            max_value=i
    return max_value
print(find_max_with_for_loop(nums))
      

#6.2

nums = [2024, 98, 131, 2, 3, 72]

def find_min_with_while_loop(nums):
    min_value = nums[0]
    c = 0 #use counters with while loops
    while c < len(nums):
        if nums[c] <= min_value:
            min_value = nums [c]
        c += 1
    return min_value #put return outside of while loop to make sure it goes thru all numbers

print(find_min_with_while_loop(nums))


#7
 
#approach 1

txt = "UC Berkeley, founded in 1868!"

def vowel_counter(txt):
    c=0
    vowel = 'aeiouyAEIOUY'
    for i in txt:
        if i in vowel:
            c = c+1
    return c


def consonant_counter(txt):
    c=0
    consonant = 'bcdefghjklmnpqrstvwxzBCDEFGHJKLMNPQRSTVWXZ' #if the color dims it means variable hasnt been used yet
    for i in txt:
        if i in consonant:
            c = c+1
    return c


#approach 2

def vowel_and_consonant_counter(txt): #define fxn
    v = 0 # vowels
    c = 0 # consonants

    vowel = 'aeiouyAEIOUY'
    consonant = 'bcdefghjklmnpqrstvwxzBCDEFGHJKLMNPQRSTVWXZ'

    for i in txt:
        if i.isalpha() == True: #define if i in txt is a letter
            if i in vowel: #if i in txt is vowel
                v = v + 1 #0+1+2 etc. 
            elif i in consonant: #otherwise if i in txt is consonant
                c = c + 1 #0+1+2 etc. 
    return (v,c) #produce/output a tuple of (v,c)

vowel_and_consonant_count = (vowel_and_consonant_counter(txt)) #attatch fxn to string
print(vowel_and_consonant_count) # print string


#8
num = 2468
def digital_root(num):
    sum=0
    while num>0:
        sum += num%10 #mod will seperate parts
        num = num// 10
    return sum
print(digital_root(num))
