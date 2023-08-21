list1 = [5,9,14,17,21,25,29,31,35,44,51]

def myFunction(list1):
    list2 = []
    for num in list1:
        prime = [True for i in range(num + 1)]
        p = 2
        while (p * p <= num):
            if (prime[p] == True):
                for i in range(p * p, num + 1, p):
                    prime[i] = False
            p += 1
        for p in range(2, num + 1):
            if prime[p]:
                if num == p:
                    list2.append(num)
    return list2
