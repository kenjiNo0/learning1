def calc_tax(u):
    y = u * 1.1
    return(y)

goods = [1000,763,999]

total = 0
for i in range(0,len(goods)):
    total += goods[i]
total = calc_tax(total)
print(int(total))