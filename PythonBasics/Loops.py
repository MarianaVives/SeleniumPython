# Loops

#If loop
greeting = "Good Morning";
print("Conditionals: ");

if greeting == "Morning":
    print("matches");
else:
    print("not matches");

print("Outside if conditional loop")

#For Loop
print("For Loop: ");
obj={2,3,4,5,6,7,8,9,10};
even=[];
uneven=[];
sum = 0;
for o in obj:
 #Sum all numbers
    sum=sum+o;
    print(sum);
print("End of sum loop");

for m in range(10):
    print(m); #Will print till m-1 so until 9

for t in range(0, 20, 2):
    print(t); #Will print 2,4,6,8..18

print("Start of even/uneven loop");
for o in range(0,10):

    if o%2 == 0:
        even.append(o);
    else:
        uneven.append(o);
print("Even: "+ str(even));
print("Uneven: " + str(uneven));


# If/elif/else
user = 16;

if user <= 11 and user >= 5:
    print("Good Morning");
elif user >= 12 and user <= 17:
    print("Good Afternoon");
elif user >= 18 and user <= 21:
    print("Good Evening");
else:
    print("Good Night");

print("Greeting code has completed");