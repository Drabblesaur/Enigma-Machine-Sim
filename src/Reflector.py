class Reflector:

    def __init__(self, str):
        letterOrder =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        outputOrder = list(str)
        self.rotor = [letterOrder,outputOrder]

    def getOutput(self,str):
            index = self.rotor[0].index(str)
            output = self.rotor[1][index]
            print("REF " +str + "->" + output)
            return output

# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# YRUHQSLDPXNGOKMIEBFZCWVJAT
