Children = 3
Hometown = "Lahti"

# # Lista
TownsInFinland = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

RandomInformation = ["Jere", 34, True, Children, Hometown]

print(TownsInFinland[-1])
TownsInFinland.append("Rovaniemi")
print(TownsInFinland)

NumOfTowns = len(TownsInFinland) # Vastaus: 6 kaupunkia
print(TownsInFinland[NumOfTowns-1])

Municipalities = ["Asikkala", "Hollola", "Karvia", "Kempele"]
Towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

MunicipalitiesAndTowns = [Municipalities, Towns]

print(MunicipalitiesAndTowns[1][-2])

Towns.sort()
print(Towns)

Teacher = {
    'name': 'Juha',
    'age': 50,
    'city': 'Lahti'
}

print(Teacher["name"])

Teacher['email'] = 'juha.hyytiainen@lab.fi'

print(Teacher)

for key in Teacher:
    print(key, end=' ')
    print(Teacher[key])

Student = [
    {'name': 'Mikko', 'age': 25, 'city': 'Tampere'},
    {'name': 'Maija', 'age': 30, 'city': 'Espoo'},
    {'name': 'Seppo', 'age': 35, 'city': 'Helsinki'}
]   
print(Student[0])

Cities = {
    'Finland':['Tampere', 'Espoo', 'Helsinki'],
    'Sweden':['Stockholm', 'Malmö']
}
print(Cities['Finland'][0])

#Towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]
for town in Towns:
    print(f"The town of {town}")
print(f"All of the towns {Towns}")

for i in range(1,10):
    print(i)

for i in range(1,10):
    print(i, end=' ')

print("")
for i in range(1, 10, 3):
    print(i)

print("")
Total = 0
for i in range(1,101):
    Total +=i
    print(Total)

print(Total)   

for i in range(9):
    if (i == 3):
        continue
    print(i)

# Opiskele loopit for ja while, sekä niihin liittyvät komennot: continue ja break
 
# while 1 < 10:
#     print("Do not try me at home xD")    

i = 0
while i < 10:
    print(f"Iteration numer: {i}")
    i += 1
    # i = i + 1

continueLoop = True
while continueLoop == True:
    if input("Do you want to continue? ") != "yes":
        continueLoop = False    

while True:
    if input("Do you want to continue?") != "yes":
        break
    else:
        continue
    
           