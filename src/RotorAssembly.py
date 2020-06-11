from Rotor import Rotor
from Reflector import Reflector

class RotorAssembly():
    def __init__(self,r1,r2,r3,rf):
        self.rotor1 = r1
        self.rotor2 = r2
        self.rotor3 = r3
        self.reflector = rf
    
    def getOutput(self,str):
        self.increment()
        print("======")
        val1 = self.rotor3.getOutput(str)
        val2 = self.rotor2.getOutput(val1)
        val3 = self.rotor1.getOutput(val2)
        val4 = self.reflector.getOutput(val3)
        val5 = self.rotor1.getOutput(val4)
        val6 = self.rotor2.getOutput(val5)
        out = self.rotor3.getOutput(val6)
        print(out)



    def increment(self):
        is_r3_cycle = self.rotor3.incrementRotation()
        if is_r3_cycle:
            is_r3_cycle = False
            is_r2_cycle = self.rotor2incrementRotation()
            if is_r2_cycle:
                is_r2_cycle = False
                self.rotor1.incrementRotation()

r1 = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
#r1.setRing('B')
r2 = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE')
#r2.setRing('B')
r3 = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO')
#r3.setRing('B')
rf = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
asssembly = RotorAssembly(r1,r2,r3,rf)
asssembly.getOutput('A')


