import random
n = random.randrange(1,10)
guess = int(input("introduzca un numero : "))
while n!= guess:
    if guess < n:
        print("ese no es")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print(" ya casi !")
        guess = int(input("Enter number again: "))
    else:
      break
print("adivinaste ese si es !!")