print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
print("Possible answer:\n- x[:5]")
print(x[:5])



print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
b = [n for n in x if n%2 == 0]
#Also
c = list(filter(lambda n: n%2 ==0, x))
print("Possible answers:\n - [n for n in x if n%2 == 0]\n - list(filter(lambda n: n%2 ==0, x))")
print(b)


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
b = [n for n in x[0:5] if n%2 == 0]
#Also
c = list(filter(lambda n: n%2 ==0, x[0:5]))
print("Possible answers:\n - [n for n in x[:5] if n%2 == 0]\n - list(filter(lambda n: n%2 ==0, x[0:5]))")
print(c)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
initials = [n[0] for n in names]
print("Possible answer:\n-initials = [n[0] for n in names]")
print(initials)



print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
space_indexes = [n.index(" ") for n in names]
print("Possible Answer:\n- space_indexes = [n.index(" ") for n in names]\n(NOTE: Indexes from 0)")
print(space_indexes)




print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
first_last_initial = [n[0] + n[n.index(' ')+1] for n in names]
print("Possible Answer:\n- first_last_initial = [n[0] + n[-1] for n in names]")
print(first_last_initial)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:
print("Possible Answer:\n- for lst in list_of_lists:\n      if len(lst) == len(set(lst)):\n         print(lst)")
for lst in list_of_lists:
    if len(lst) == len(set(lst)):
        print(lst)


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
request_on = True
while request_on:
    try:
        num = int(input('Please, enter a number greater than 100:\n '))
    except:
        print("Incorrect input")
    else:
        if num > 100:
            request_on = False
        else:
            print("That number is not greater than 100")
print(num)

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
prime_or_not_prime = "prime"
for n in range (2, int(num**0.5)+1):
    if num % n == 0:
        prime_or_not_prime = "not prime"
print(prime_or_not_prime)




