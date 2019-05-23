def fizzbuzz(limit=101):
    for num in range(1,limit):
        result = ""
        if num % 3 == 0: result += "Fizz"
        if num % 5 == 0: result += "Buzz"
        yield result if result else num

for digit in fizzbuzz():
    print(f"{digit}")
