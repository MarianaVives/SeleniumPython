#Get logic from parent class OOpsDemo
from OopsDemo import Calculator


class ChildImplementationClass(Calculator):
    num2=200;

    def __init__(self):
        Calculator.__init__(self, 1, 2);

    def getCompleteData(self):
        return self.num2 + self.num + self.sumTimes100(); #200 +100 + (1+2)*100

obj = ChildImplementationClass()
print(obj.getCompleteData());
