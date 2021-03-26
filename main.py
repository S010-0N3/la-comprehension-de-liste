from csv import *

#exemple enumerate()
print("","\n","sans enumerate()")
students = ["Anna","Martin","Bob","Eric","Elise"]
ages = [16,15,18,20,20]

for students in students:
  print("etudiant")
  print(students)
  print("Age")

###enumerate()
print("","\n","Avec enumerate()")
for i, student in enumerate(students):
  print("Index Etudiant")
  print(i)
  print("Etudiant")
  print(students)

print("","\n","\n","\n","\n","Avec enumerate() et ajout de l'age")
for i, student in enumerate(students):
  print("Prenom")
  print(students)
  print("Age")
  print(ages[i])



########
print("","\n","autre exemple")

cars = [["Noir","Astin Martin","234"],["Bleu","bmw","45"]]
price = [1615,1820]

for i, car in enumerate(cars):
  car.append(price[i])

print(cars)