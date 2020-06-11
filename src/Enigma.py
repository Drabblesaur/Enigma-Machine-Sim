STATIC_KEY = list(range(1,27))
# print(len(STATIC_KEY))


r1 = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
r1.printRotor()
print('+++')
for i in range(1,26):
    r1.rotate()
r1.printRotor()
print('+++')
r1.rotate()
r1.printRotor()
r1.printRotation()


