#Classes are user defined blueprint or prototype
#Self keyword is mandatory for calling variables into method
#instance and class variables have whole different purpose
#constructors should be __init__

class Calculator:
    num =100; #Class variable
    #Default constructor - first method called in a class
    def __init__(self,a,b):
        self.firstnumber=a;
        self.secondnumber=b;
        print("I am called automatically when an object is created");

    def getData(self):
        print("I am now executing as method in class.");
    def sum(self):
        return self.firstnumber + self.secondnumber;
    def substract(self):
        return self.firstnumber - self.secondnumber;
    def multiply(self):
        return self.firstnumber * self.secondnumber;
    def divide(self):
        return(self.firstnumber / self.secondnumber);
    def sumTimes100(self):
        #return(self.firstnumber + self.secondnumber * Calculator.num); this is also an option
        return((self.firstnumber + self.secondnumber) * self.num); #constructor will also read from variables of the class

object = Calculator(20,30);

object.getData();
print(f"Sum: {object.sum()}");
print(f"Substract: {object.substract()}");
print(f"Multiply: {object.multiply()}");
print(f"Divide: {object.divide()}");
print(f"Sum times 100: {object.sumTimes100()}");