import math as m

angulo=int(input("\ndigite um angulo em graus:"))

Rang=((angulo*3.14)/180)

print(f'\nSeno{m.sin(Rang)}')
print(f'\nco-seno: {m.cos(Rang)}')
print(f'\ntangente: {m.tan(Rang)}')
print(f'\nco-secante:{1/m.sin(Rang)}')
print(f'\nncotangente{1/m.tan(Rang)}')
print("\n")