str = "RahulShettyAcademy.com";
str1 = " Consulting firm";
str3 = " RahulShetty";
str4 = " Hello my viewer "

print(str[1]); #can be read like a list - starting from the 1st letter in the first index 0
print(str[0:5]) #Get a substring

print(str + str1);

print(str3 in str); #Returns boolean, it is within the string
splitTxt = str.split(".");
print(splitTxt); #split text
print(splitTxt[0]); #Get the first text

print(str4.strip()) #remove spaces beginning and end
print(str4.lstrip()) #remove left space
