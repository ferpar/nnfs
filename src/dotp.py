a = [1, 2, 3]
b = [2, 3, 4]

def calc_dotp(a,b):
    if (len(a) == len(b)):
        dotp=0
        for x,y in zip(a,b):
            dotp+=x*y
        return dotp
    else:
        return "vectors must have same dimension for the dot product"

print(calc_dotp(a,b))
