class Sample:
    def addtion(self):
        print("addtion value is :",self.a + self.b)
    def subtraction(self, a, b):
        print("subdstration value is :",self.a - self.b)
    



callingClass = Sample()
callingClass.a = 10
callingClass.b = 20
callingClass.addtion()

