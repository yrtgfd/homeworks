a = input().split(',')
print(a)
line1 = (int(a[3])-int(a[1]))/(int(a[2])-int(a[0]))
line2 = (int(a[7])-int(a[5]))/(int(a[6])-int(a[4]))
if line1 == line2:
    print('YES')
else:
    print('NO')