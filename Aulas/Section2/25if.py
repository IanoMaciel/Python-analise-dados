from typing import AsyncGenerator


print("\n")

age = 15

if age >= 18:
    print('Maior de idade')
elif age >= 15 and age <= 17:
    print('Você precisa da autorização de seus pais')
else:
    print('Menor de idade')