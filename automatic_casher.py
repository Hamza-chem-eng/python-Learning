t = 0
c=0
while True:
    x = float(input("Enter a cost of your bought : "))

    if x == 0 :
        print("The bought cost is "+str(t)+" for "+ str(c)+" items")
        break
    t += x
    c += 1
