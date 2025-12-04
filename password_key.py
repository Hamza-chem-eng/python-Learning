password = "hamza"
while True:
    pas = input("Enter your password: ")
    if pas == password:
        print("Welcome back !")
        break
    else :
        print("Wrong password !")
    c +=1
    if c == 3 :
        print("system locked")
        break
