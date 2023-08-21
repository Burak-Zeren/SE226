myDict=dict()
for i in range(1, 31):
    if i == 1:
        myDict[i] = 0
    else:
        myDict[i] = i * (i-1)

for key, value in myDict.items():
    print(key,"-",value)

sumNumber=0
for key in myDict:
    sumNumber=sumNumber+myDict[key]
print(f"Sum of value is {sumNumber}")

number = int(input("Please enter number that you want to delete from dictionary : "))

flag=False
while(flag==False):
    for key in myDict:
        if key == number:
            flag=True
    if flag:
        print(f"{number} key is deleted from dictionary ! ")
        my_pop = myDict.pop(number)
        print(f"Deleted value is {my_pop}")
    else:
        print(f"{number} key is not one of the key of dictionary !")
        number = int(input("Please enter number that you want to delete from dictionary : "))