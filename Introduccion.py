x = 1000005;
y = 2;
print(x%y);


#Write a Python program to convert these numbers into string then into float types: 10,20,30,40,50,60,70,80,90,100#

listaNumeros = [10,20,30,40,50,60,70,80,90,100];
listaNumerosString = [];
listaNumerosFloat = [];
iterador = 0;

for i in listaNumeros:
    iterador=iterador+1;
    listaNumerosString.append(i);

    print(iterador," = ",type(str(i)));

iterador=0;

for x in listaNumeros:
    iterador=iterador+1;
    listaNumerosFloat.append(x);
    print(iterador," = ",type(float(x)))

print(listaNumerosString);
print(listaNumerosFloat);




    




