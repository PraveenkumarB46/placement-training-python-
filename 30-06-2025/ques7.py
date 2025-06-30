def sum_even_digits(n):
    return sum(int(d) for d in str(n) if int(d) % 2 == 0)
print(sum_even_digits(123456)) 
