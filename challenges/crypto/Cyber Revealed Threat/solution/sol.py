def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('cannot mod inverse')
    else:
        return x % m

def chinese_remainder_theorem(nums, rems):
    prod = 1
    for n in nums:
        prod *= n

    result = 0
    for n, a in zip(nums, rems):
        pp = prod // n
        result += a * modinv(pp, n) * pp
    return result % prod

def num_to_flag(num):
    return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big').decode('utf-8')

num = [1000000000039, 2000000000033, 3000000000013, 4000000000037, 5000000000041]
rem = [304225373519, 659380177035, 1313560272604, 3219557421014, 1664423823579]

# To retrieve the flag using the residues
flag= chinese_remainder_theorem(num, rem)
decoded_flag = num_to_flag(flag)
print(f"Decoded Flag: {decoded_flag}")