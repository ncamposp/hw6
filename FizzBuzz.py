def FizzBuzz(x):
    if x % 5 == 0 and x % 3 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz."
    else:
        return str(x)