#Question1
n=int(input("Enter one number: "))
x=int(input("Enter another number: "))

calc=lambda a:1 if a==0 else a*calc(a-1)

condition=[n**(a+1)/calc(a+1) for a in range(x)]

result=1+sum(condition)

print(f"e^{n} = {result}")

