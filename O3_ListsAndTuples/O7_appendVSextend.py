even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.append(odd)
print(even)

even = [2, 4, 6, 8]

even.extend(odd)
print(even)

even.sort(reverse=True)
print(even)

even.sort()
print(even)

print('#' * 80)

# Another Example

str1 = ['alpha', 'beta', 'gamma']
str2 = ['kilo', 'omega']

str1.append(str2)
print(str1)
str1.append('epsilon')
print(str1)

print('-' * 80)

str1 = ['alpha', 'beta', 'gamma']
str1.extend(str2)
print(str1)
str1.extend('epsilon')
print(str1)

str1 += 'chi'
print(str1)
