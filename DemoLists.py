#Create a list
#List is a data type that allows multiple values and cane be different data types
print("Lists : ")
values = [1, 2, "abc", 3.5, 5]
print("Here are list examples")
print(values);
print(values[0]);

print("outside of the for loop");
index=0;
for value in values:
        index = index +1 ;
        print("Inside for loop iteration number " + str(index));
        print(value);
print("End of for loop");

#Retrieves last element
print(values[-1]); #5
print(values[:-1]); #1,2,'abc',3.5
#Get specific sequenced elements
print(values[1:3]) # 2, "abc"
#Insert a value inside the list
values.insert(3, "xyz"); #[1, 2, 'abc', 'xyz', 3.5, 5]
print(values);
#Add an element at the end of the list
values.append("end") #[1, 2, 'abc', 'xyz', 3.5, 5, 'end']
print(values);
#update a value
values[2]= "def"; #[1, 2, 'def', 'xyz', 3.5, 5, 'end']
print(values);

#Tuples
print("Tuples : ")
val = (1,2,"abc",4,5);
print(val);
#val[3] = "def"; Error
#values.insert(5, "xyz"); Does not insert values
print(val);

#Dictionary
print("Dictionary : ")
dic = {"color":"pink", "name":"ana", 5:5, "age":25, "pet":"dog", "single":False};
print(dic);
print(dic["color"]);
print(dic[5]);

#create dictionary in runtime
dicRun ={}
dicRun["firstname"] = "Anita";
dicRun["lastname"] = "Patrick";
print(dicRun);
dicRun["dog"] = "Labrador";
print(dicRun);

#Exercise
fruits = "apple", "banana", "cherry", "date", "elderberry";
print("First fruit:", fruits[0])
print("Last Fruit:", fruits[-1])
print("Fruits from index 1 to 2:", fruits[1:3])

#Second Method
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# Print the first and last elements
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
# Slicing to print the second and third fruits
print(f"Fruits from index 1 to 2: {fruits[1:3]}")