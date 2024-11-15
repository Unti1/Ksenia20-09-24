lst = [1,2,3,4,5,6,7,8]

# lst = ['строка',True, [1,2,3], 205, .5]
# for i in range(len(lst)):

# for val in lst:
#     print(f"{val=}")
#     print('S[окр] =', 3.14*val**2)

print(range(20))
print(range(5,10))
print(range(2, 19, 2))

# for ind in range(2,19,2):
#     print(f'{ind=}')
    

lst = [1,2,3,4,5,6,7,8]
lst2 = []
for i in range(0, len(lst), 1):
    if lst[i] % 2 == 0:
        print(f'{i=} | {lst[i]} - чёт.')
        lst2.append(lst[i])
    # elif lst[i] % 2 == 1:
    else:
        print(f'{i=} | {lst[i]} - нечёт.')

print(lst2)


lst = [1,2,3,4,5,6,7,8]
lst2 = []
for x in lst:
    if x % 2 == 0:
        print(f'{x=} - чёт.')
        lst2.append(x)
    else:
        print(f'{x=} - нечёт.')
else:
    print('Цикл закончился')

print(f'{lst2=}')