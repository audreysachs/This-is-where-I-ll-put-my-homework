nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #pythons interprets [] as list
planets = ["Saturn", "Jupiter", "Venus"] # for strings must put in ''
mixed = [1, "Python", True, 3.14]
nested = [[1,2], [3,4]] #nest is list in list
empty = []

nums.append (11) #append adds a number at end
print (nums)

planets.insert (1, "Mercury") #insert adds a number in specific location 
print (planets)

mixed[1] = 222 #indexing like this replaces value with another value
print (mixed)

print (planets)
planets.remove("Jupiter") #remove allows to remove object
print(planets)

print (planets)
planets.pop(1) #pop allows to remove object at index
print (planets)

#introduction to dictionaries
fourth_planet = {
    "name" : "Mars", 
    "moons" : ["Phobos", "Deimos"],
    "diameter_km" : 6337,
    "atmosphere" : False,}
 #dict uses {} and goes key->value, something is wrong here

print(fourth_planet)
print(fourth_planet["name"])

fourth_planet.get('moons')

fourth_planet ["atmosphere"] = True # modifying a dict
fourth_planet ["color"] = "Red" # adding to dictionary 


#advanced section 
#Concetemating (adding lists together)

list1 = [1, 2, 3] #order matters
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

list4= list1.append(list2)
print(list1)

#slicing 
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[1:5])

#striding : allows to skip numbers #[start:stop:skip]
strid_nums = numbers[::2] #nothing in start stop, so skip every 2
print (strid_nums)

reverse_nums = numbers [::-1] #this will reverse no skip
print (reverse_nums)

funk_list = numbers [2:7:2] #start at 2, stop at 7, skips 2
print(funk_list)

#Enumerating: allows you to print index next to values
for index, value in enumerate(mixed):
    print(index, value) #shows the index number next to the values

#sorting
unsorted_list = [3, 1, 4, 5, 9]
unsorted_list.sort()  #prints form smallest to biggest values
print(unsorted_list)

#Example 1
desserts = ["cookie", "icecream", "brownie", "candy"]
c_words= []

for desserts in desserts:
    if desserts.startswith('c'):
        c_words.append(desserts.upper())
print(c_words)

words_c = [dessert.upper() for dessert in desserts if dessert.startswith('c')]
print(words_c)

#Example 2 #take average of all theese peoples favorite numbers 
fav_nums = {
    "Alice" : [5, 101, 66],
    "Bob" : [7, 23, 111],
    "Chuck" : [26, 82, 84]
}
average_nums={name : sum(num)/len(num) for name, num in fav_nums.items()}
print(average_nums)
