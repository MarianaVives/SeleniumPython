file=open("text.txt");

#read all contents from the file
#print(file.read());
#print(file.read(5)); #Reads 3 bytes

#Read one line at a time
#print(file.readline());

#iterate the list and read each line
#line = file.readline();
#listLine=[];
#while line!="":
#    print(line);
#    listLine.append(line); #Store values in a list
#    line = file.readline();
#print(listLine);
#file.close();

#read using for Loop
for l in file.readlines():
    print(l);