def getmodifier(bullet):
    a = 1.0474368231046931
    b = 1.3008765432098766
    return a*(b**(bullet-1))
for i in range(5):
    print(getmodifier(i))