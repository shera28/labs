class myClass:
    def getString(self):
        self.inp = input()

    def printString(self):
        print(self.inp.upper())


t = myClass()
t.getString()
t.printString()