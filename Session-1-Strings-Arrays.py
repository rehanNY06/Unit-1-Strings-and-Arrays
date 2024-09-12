#print("Hello World!")

#Problem 1
"""def welcome():
    print("Welcome to The Hundred Acre Wood")

welcome()"""

#Problem 2
"""def greeting(name):
    print("Welcome to The Hundred Acre Wood! " + "My name is " + name + ".")

greeting("Dariel")
greeting("Rehan")"""

#Problem 3
"""def print_catchphrase(character):
    if (character == "Pooh"):
        print("Oh bother!")
    if (character == "Tigger"):
        print("TTFN: Ta-ta for now!")
    if (character == "Eeyore"):
        print("Thanks for noticing me.")
    if (character == "Christopher Robin"):
        print("Silly old bear.")

print_catchphrase("Tigger")"""

#Problem 4
"""def get_item(items, x):
    if (x < 0 or x >= len(items)):
        print("None")
    if (x >= 0 & x < len(items)):
        item = items[x]
        return item

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2

print(get_item(items, x))"""

#Problem 5
"""def sum_honey(hunny_jars):
    sum_total = 0
    for jars in hunny_jars:
        sum_total = sum_total +jars
    return print(sum_total)

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)"""

#Problem 6
"""def doubled(hunny_jars):
    updated_list = []
    for jar in hunny_jars:
        updated_list.append(2*jar)
    return print(updated_list)

hunny_jars = [1, 2, 3]
doubled(hunny_jars)"""

#Problem 7
"""def count_less_than(race_times, threshold):
    list_checker = []
    for time in race_times:
        if (time >= threshold):
            list_checker.append(time)
    counter = len(list_checker)
    return print(counter)

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)"""

#Problem 8
"""def print_todo_list(task):
    print("Pooh's To Dos:")
    listNumber = 1
    for x in task:
        print(listNumber, ". ", x)
        listNumber = listNumber + 1

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)"""

#Problem 9
"""def can_pair(item_quantities):
    for x in item_quantities:
        if (x % 2 != 0):
            return print("false")
    return print("true")

item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

item_quantities = [1, 2, 3, 4]
can_pair(item_quantities)

item_quantities = []
can_pair(item_quantities) """

#Problem 10
"""def split_haycorns(quantity):
    listFactors = []
    for i in range(1, quantity + 1):
       if quantity % i == 0:
           listFactors.append(i)
    return print(listFactors)

quantity = 6
split_haycorns(quantity)"""