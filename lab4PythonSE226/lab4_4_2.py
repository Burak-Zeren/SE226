divided = {'Tony  ': 41, 'Rhodey': 43, 'Nat   ': 35}
we_fall = {'Steve ': 39, 'Clint ': 35, 'Wanda ': 28}

united_we_stand = {"Name": "  Age"}
united_we_stand.update(divided)
united_we_stand.update((we_fall))
for key,value in united_we_stand.items():
    print(key,"  ",value)

print("--------------------------------")
united_we_stand.pop('Nat   ')
for key,value in united_we_stand.items():
    print(key,"  ",value)

sortedItems = sorted(united_we_stand.keys())


print("--------------------------------")
for key in sortedItems:
    print(key)

#This kod is not working because of Age value

#sortedValues=sorted(united_we_stand.values())
#print(f"Minimum number is {sortedValues[0]}")
#print(f"Maximum number is {sortedValues[len(sortedValues)-1]}")

print("--------------------------------")
values=united_we_stand.values()
min = list(values)[1]
max = list(values)[1]
for i in range(1,len(list(values))):
    if list(values)[i]>max:
        max=list(values)[i]
    if list(values)[i]<min:
        min=list(values)[i]
print(f"Minimum number is {min}")
print(f"Maximum number is {max}")

