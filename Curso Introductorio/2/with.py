#Write  a program in python to declare four messages to the community of 
# technology othat the Python programming language is wonderful but describe pythn with  
# a different description in each message you will write , so with one message withe 
# one python description then answer the following questions:
#How long each message you write is?
#what is the count of a specific letter in each message you will write?
#are the codes you write end with "l"?
#are the codes you write start with "T"?

mensaje = "Ta different description in each message you will write , so with one message withe"

print(len(mensaje))

vocales = ["a","e","i","o","u"]

for i in vocales:
    print("tiene ",mensaje.count(i)," ",i," vocales")

print(mensaje.endswith("l"))
print(mensaje.startswith("T"))