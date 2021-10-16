#Write a program in python check the person age then show him the price of train ticket that fit his age in dollars:¶
#children until 18 years ticket = 2
#old people bigger than or equal 60 years ticket = 5
#young people from 18 - 59 year ticket = 10
#and don't forget to declare your age:

#while(True):

def entregarPrecioPasaje():

    edad = int(input("Digite su edad = "))



    if (0< edad < 18):

        precio = 2

    elif(18<edad<59):

        precio = 10

    else:

        precio = 5

    
    return "El precio de su pasajes es de = ",precio, "Ya que su edad es de: ", edad


print("-------------------")

#Using for loop write a python code that gives the multiply of the following list:
my_list =[1,4,20,50,100,2000,10000,6]


def multiplicarLista(Lista):
    multiplicacion = 1

    for i in Lista:
        multiplicacion *= i

    return multiplicacion


print(multiplicarLista(my_list))
