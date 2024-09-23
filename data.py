a = 45
print(bin(a))

b = "1010101"
print(int(b, 2))

c = "10111"
d = "1101"
resultaat_bin = int(c, 2) + int(d, 2)
print(bin(resultaat_bin))

e = 255
print(hex(e))

f = "2A"
print(int(f, 16))

g = "C4"
h = "3A"
resultaat_hex = int(g, 16) + int(h, 16)
print(hex(resultaat_hex))

i = "1101"
print(int(i, 2))

j = "F0"
print(int(j, 16))

k = 123
l = 456
resultaat_dec = k + l
print(resultaat_dec)

m = 157
print(f"bin: {bin(m)}, hex: {hex(m)}.")

n = "11101101"
n_dec = int(n, 2)
n_hex = hex(n_dec)
print(f"dec: {n_dec}, hex: {n_hex}")

o = "AB4"
o_dec = int(o, 16)
o_bin = bin(o_dec)
print(f"dec: {o_dec}, bin: {o_bin}")
