Molar_mass = {
    "h2o":18.015,
    "cl2":35.45,
    "ba(oh)":137.33
}
e = input("Choose the element (H2O,CL2,BA(OH) : ").lower()
mas = float(input("enter the mas in (g) : "))
if e in Molar_mass:
    print("The mol you is ",mas*Molar_mass[e])
else:
    print("The value is not defined")
