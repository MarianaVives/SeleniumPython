ItemsInCart = 0;

#fail program if condition not met
#if ItemsInCart != 2:
#    raise Exception("Products cart count not matching");

#Assertions
#assert(ItemsInCart == 2); #if False it will break test

#try and catch: makes code to not break/fail

#customized exception error
try:
    with open("abc.txt") as file: #File does not exits
        file.read();
except:
    print("Failed to find file")

#File is found
try:
    with open("text.txt") as file: #File does not exits
        file.read();
        print("File read successfully");
except:
    print("Failed to find file");

#Python exception
try:
    with open("filelog.txt") as file: #File does not exits
        file.read();
        print("File read successfully");
except Exception as e:
    print(e);

#Finally block will always get executed
try:
    with open("text.txt") as file: #File does not exits
        file.read();
        print("File read successfully again");
except Exception as e:
    print(e);
finally:
    print("Closing block");