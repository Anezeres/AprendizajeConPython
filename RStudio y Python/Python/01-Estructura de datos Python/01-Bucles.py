primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

""" for i, p in enumerate(primos):
    print(i,p) """

primos2 = []

for i in range(101):
    primos2.append(i)


for p in primos2:
    restriccion = (p%2==0)
    restriccion2 = (p%3==0)

    if restriccion or restriccion2:
        primos2.remove(p)




print(primos2)
print(primos)



