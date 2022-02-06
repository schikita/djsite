n = int(input())
lst = []
while n > 0:
    i = n % 10
    lst.append(i)

lst.reverse()
print(lst)
