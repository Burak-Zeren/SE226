from abc import ABC

class Abstract(ABC):
    address=None

    def __init__(self, address):
        self.address=address

    def calculateFreqs(self):
        pass

class ListCount(Abstract):

    def calculateFreqs(self):
        numbera = 1
        count = 0
        originalList = list()
        listHolder = list()
        holderAll = list()
        with open(self.address, 'r') as file:
            content = file.read()
            for char in content:
                if char.isalpha():
                    char = char.lower()
                    holderAll.append(char)
                    if char not in listHolder:
                        listHolder.append(char)
                        listHolder.sort()
            for charr in listHolder:
                for uniqueChar in holderAll:
                    if charr == uniqueChar:
                        count += 1
                if numbera == 1:
                    originalList.append(f"List-> {charr}"+"  "+f"Resulting List -> {charr} = {count}")
                else:
                    originalList.append(f"       {charr}" + "  " + f"                  {charr} = {count}")
                numbera = 0
                count = 0
        for items in originalList:
            print(items)

class DictCount(Abstract):

    def calculateFreqs(self):
        dictHolder = dict()
        with open(self.address, 'r') as file:
            content = file.read()
            for char in content:
                if char.isalpha():
                    char = char.lower()
                    if char in dictHolder:
                        dictHolder[char] += 1
                    else:
                        dictHolder[char] = 1
        number = 1
        sorted_char = sorted(dictHolder.keys())
        for sortedChar in sorted_char:
                if number == 1:
                    print(f"Dict -> {sortedChar}" + "  " + f"Updated Dist -> {sortedChar} = {dictHolder[sortedChar]}")
                else:
                    print(f"        {sortedChar}" + "  " + f"                {sortedChar} = {dictHolder[sortedChar]}")
                number = 0


file_adress = "weirdWords.txt"
list_counter = ListCount(file_adress)
dict_counter = DictCount(file_adress)
list_counter.calculateFreqs()
print("-------------------------------------------------")
dict_counter.calculateFreqs()
