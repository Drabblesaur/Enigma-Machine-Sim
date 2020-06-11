class Rotor:
    rotation = 0

    def __init__(self, str):
        self.letterOrder =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        outputOrder = list(str)
        self.rotor = [self.letterOrder,outputOrder]
        # print(self.letterOrder)
        # print(outputOrder)

    def rotate(self):
        outputList = self.rotor[1]
        newRotor = [outputList[(i - 1) % len(outputList)] for i, x in enumerate(outputList)]
        self.rotor[1] = newRotor
    
    def setRing(self,str):
        shift_index = self.letterOrder.index(str)
        outputList = self.rotor[1]
        for k in range(0,26):
            letter = outputList[k]
            letter_index = self.letterOrder.index(letter)
            total_shift = letter_index+shift_index
            if total_shift == 26:
                total_shift = 0
            outputList[k] = self.letterOrder[total_shift]
        self.rotor = [self.letterOrder,outputList]
        # print(outputList)

    def incrementRotation(self):
        self.rotate()
        self.rotation += 1
        if self.rotation >= 26:
            self.rotation = 0
            return True
        else:
            return False

    def printRotor(self):
        print(self.rotor)

    def getRotation(self):
        return self.rotation
    
    def getOutput(self,str):
        index = self.rotor[0].index(str)
        output = self.rotor[1][index]
        print(str + "->" + output)
        return output

