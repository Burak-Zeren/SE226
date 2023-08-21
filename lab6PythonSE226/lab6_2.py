#Question 2
n=int(input("Enter one number: "))
total=0
def myFunction(n):
    k = n
    global total
    if k==0:
        print(total)
    else:
        total = total + ((-1) ** (k + 1) / k)
        myFunction(n-1)
myFunction(n)
