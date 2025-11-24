def c_to_f(c):
    return (9/5)*c+32
def c_to_k(c):
    return c+273.15
c = float(input("enter the temp in c degrees: "))
f = c_to_f(c)
k = c_to_k(c)
print("the temp in k is : ", k)
print("the temp in f is :" ,f) 
