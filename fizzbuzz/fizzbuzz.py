def fizzbuzz(self, n: int) -> str:
    result: str = ""
    if n % 3 == 0:
        result = "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    elif not result:
        result = str(n)

    return result