Molar_mass = {
    "h2o":18.015,
    "cl2":35.45,
    "ba(oh)":137.33
}
while True:
    e = input("Choose the element (H2O,CL2,BA(OH) : ").lower()
    if e == "q":
        print("goodbye")
        break
    mas = float(input("enter the mas in (g) : "))
    if e in Molar_mass:
        print("The number of mol is ", mas / Molar_mass[e])
    else:
        print("The value is not defined")

