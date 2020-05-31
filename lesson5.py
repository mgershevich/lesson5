# 1 проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);

def is_prime(num):
    i = 2
    while num > i:
        if num % i == 0:
            break
        i += 1
    return i == num
print(is_prime(765))

# 2 выводит список всех делителей числа;
def all_dividers(num):
    result = []
    i = 2
    while i * i <= num:
        if num % i == 0:
            num //= i
            result.append(i)
        else:
            i += 1
    if  num > 1:
        result.append(num)
    return result
print(all_dividers(4689))

# 3) выводит самый большой простой делитель числа.
def greatest_pr_div(num):
    prime_num = all_dividers(num)
    max_num = 0
    for i in prime_num:
        if i > max_num:
            max_num = i
    return(max_num)
print(greatest_pr_div(86543))