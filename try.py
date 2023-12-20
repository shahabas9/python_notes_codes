class fibonacci:
    def __init__(self):
        self.sequence = []

    def generate(self, length):
        if length <= 0:
            return self.sequence 
        elif length == 1:
            return [0]  
        elif length == 2:
            return [0, 1]  
        else:
            self.sequence = self.generate(length - 1)  
            self.sequence.append(self.sequence[-1] + self.sequence[-2]) 
            return self.sequence  
        


fibLength = 5
fibGenerator = fibonacci()
fibSequence = fibGenerator.generate(fibLength)
print(fibSequence)






