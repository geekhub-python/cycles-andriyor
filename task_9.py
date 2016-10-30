import string

c = input()
out = 3
s = ord(c.lower()) + 1
for i in range(s, s + 3):
    if i > ord('z'):
        a = ord('a')
        for z in range(a, a + out):
            print(chr(z), end=' ')
        break
    print(chr(i), end=' ')
    out -= 1

print()

# other solution
alphabet = string.ascii_lowercase + 'abc'
index = alphabet.index(c)
for i in range(1, 4):
    print(alphabet[index + i], end=' ')

