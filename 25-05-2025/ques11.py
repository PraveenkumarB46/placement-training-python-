def sum_digits(n):
    return n if n < 10 else n % 10 + sum_digits(n // 10)

print(sum_digits(1234))  
