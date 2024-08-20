# lists
# List is created using square  brackets
# list is mutable,changable
# you can append/add items into python list
# you can remove items from a list
# you can access the items in a list(ordered)
# list can accept duplicates

fruits=["Passion","Mango","Avocado","Apple","Pinneaple"]
print(fruits)
# check type
print(type(fruits))
# access items
print(fruits[0]) #first fruit
print(fruits[1]) #second fruit
print(fruits[2]) #third fruit
#negative inexing-access from last item
print(fruits[-1])#last item
print(fruits[-2])
# Append items to a list
fruits.append("Orange")
print(fruits)
# use extend to add more than one item
new_list=["Berries","pawpaw"]
fruits.extend(new_list)
print(fruits)
# trancate
print(fruits[0:5])
print(fruits[3:6])
numbers=[23,44,906,77,8556,889,44]
print(type(numbers))

# list can contain items of different types
list2=["yellow","red",585,3.142,78j,'blue']
print(list2)
print(type(list2))
# remove list items from a list
fruits.remove("Mango")
print(fruits)
# change items in a list
fruits[2]="Tomatoe"
print(fruits)
# fruits[0].append("Kiwi")
# print(fruits)
fruits[0]="Apple"
print(fruits)
print(fruits[-4:-2])
# insert item to a specific Index
# alt 1
fruit="kiwi"
fruits.insert(0,"Kiwi")
print(fruits[0])
# alt 2
fruits.insert(0,fruit)
print(fruits)
#  count the number of items in a list
print(len(fruits))
# create a list using list method
courses=list(("Python","Data Science","Web Development"))
print(courses)
print(type(courses))
# Boolean
print(30>20)

# delete the whole list
del fruits
print(fruits)

# append,remove etc are called method






