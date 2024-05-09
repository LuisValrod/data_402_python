print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def divisors_list(n):
    div_lst = []
    for i in range(1, n+1):
        if n % i == 0:
            div_lst.append(i)
    return div_lst

print(divisors_list(12))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def factor_checking(a, b):
    if a%b == 0 or b%a == 0:
        return True
    return False
print(factor_checking(8, 16))


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def char_index(a):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    return alphabet.index(a.lower())
print(char_index('a'))



print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def id_creator(name):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", " "]
    person_id =''
    for n in name.lower():
        person_id += str(alphabet.index(n))
    return person_id
print(id_creator('Bob'))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def password_generator(name):
    num = int(id_creator(name))
    for n in str(num):
        num -= int(n)
    password = str(num)
    return password
print(password_generator('Bob'))


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

def prime_checker(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(prime_checker(101))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def robust_prime_checker(n):
    if type(n) != int:
        return "Enter a whole number next time. This function can't work with any other input"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(robust_prime_checker('9'))


# -------------------------------------------------------------------------------------- #






