string = input("input your string: ")
x = 0
o = 0

for i in string:
    if i == 'x':
        x += 1
    elif i == 'o':
        o += 1

print(x == o)
