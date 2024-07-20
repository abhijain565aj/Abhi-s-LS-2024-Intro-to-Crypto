from sympy import mod_inverse, totient
n1 = 23270927
e1 = 65537
c1 = 3872687

n2 = 119750403
e2 = 257
c2 = 58519946


def number_to_string(n):
    result = ""
    while n > 0:
        result = chr(n % 256) + result
        n = n // 256
    return result


d1 = mod_inverse(e1, totient(n1))
d2 = mod_inverse(e2, totient(n2))

print(number_to_string(pow(c1, d1, n1)))
print(number_to_string(pow(c2, d2, n2)))
# 835,e0f
