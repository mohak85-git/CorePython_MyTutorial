with open(file='binary', mode='wb') as bin_file:
    bin_file.write(bytes(range(17)))

with open(file='binary', mode='rb') as bin_file:
    for i in bin_file:
        print(i)

a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
d = 2998302     # 00 20 C0 1E

with open("binary2", 'wb') as bin_file2:
    bin_file2.write(a.to_bytes(2, 'big'))
    bin_file2.write(b.to_bytes(2, 'big'))
    bin_file2.write(c.to_bytes(4, 'big'))
    bin_file2.write(d.to_bytes(4, 'big'))
    bin_file2.write(d.to_bytes(4, 'little'))

with open("binary2", 'rb') as bin_file2:
    e = int.from_bytes(bin_file2.read(2), 'big')
    f = int.from_bytes(bin_file2.read(2), 'big')
    g = int.from_bytes(bin_file2.read(4), 'big')
    h = int.from_bytes(bin_file2.read(4), 'big')
    i = int.from_bytes(bin_file2.read(4), 'big')

print(e)
print(f)
print(g)
print(h)
print(i)
