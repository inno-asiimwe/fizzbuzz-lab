def fizz_buzz(number):
    if isinstance(number, int) or isinstance(number, float):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return number
    else:
        raise(TypeError, "only intergers and floats allowed")


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(16))
print(fizz_buzz(-3))
print(fizz_buzz(17))
