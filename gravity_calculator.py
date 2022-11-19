import math
gconstant = float(.0000000000667)


def main_math(mass1, mass2, radius):
    masscalc = (float(mass1)) * (float(mass2))
    masscalc2 = (float(radius) * float(radius))
    masscalc3 = (float(masscalc) / float(masscalc2))
    finalmath = (float(gconstant) * float(masscalc3))
    return finalmath


m1 = input('What is the mass of your first object?: ')
m2 = input('What is the mass of your second object?: ')
r = input('What is the distance between the two objects?: ')

result = main_math(m1, m2, r)
print(str(result) + ' is the force of gravity between those two objects!')
