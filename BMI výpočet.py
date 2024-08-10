height = float(input("Vložte svou výšku v metrech: "))
weight = float(input("Vložte svou váhu v kg: "))

bmi = (round(weight / (height**2), 1))

if bmi <= 18.5:
    print(f"Vaše bmi je {bmi} a spadáte do skupiny podvýživy.")
elif bmi <= 24.9:
    print(f"Vaše bmi je {bmi} a spadáte do skupiny normální.")
elif bmi <= 29.9:
    print(f"Vaše bmi je {bmi} a spadáte do skupiny nadváhy.")
elif bmi <= 34.9:
    print(f"Vaše bmi je {bmi} a spadáte do skupiny obezity.")

else:
    print(f"Vaše bmi je {bmi} a spadáte do skupiny těžké obězity.")

#print(round(bmi, 1))