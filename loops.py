#printing even odd number in given range 

for i in range (1,100):
    if i%2 == 1:
        print(i)
    elif i%5 != 0:
        print(i)
    else:
        print("Its not divisible by 5")

    