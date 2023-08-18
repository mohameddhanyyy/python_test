# write a program that can take name in lower case and return it in upper case
def uppercase(name):
    return name.upper()


names = input("Enter names in lowercase: ").split()
uppercase_names = list(map(uppercase, names))
print("Names in uppercase:", uppercase_names)

# write a program that can check if the number prime or not


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


numbers = input("Enter number to check if it prime or not: ")
numbers = list(map(int, numbers))

prime_flags = list(map(is_prime, numbers))

for number, is_prime in zip(numbers, prime_flags):
    if is_prime:
        print(number, "is prime")
    else:
        print(number, "is not prime")
