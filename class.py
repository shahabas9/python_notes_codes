class Sample:
    def addtion(self):
        print("addtion value is :",self.a + self.b)
    def subtraction(self,a,b):
        print("subtraction value is :",a-b)
    



callingClass = Sample()

callingClass.a = 10
callingClass.b = 20
callingClass.addtion()
callingClass.subtraction(10,20)