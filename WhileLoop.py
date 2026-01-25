it = 10;

while it>1:
    if it ==9:
        it=it-1;#Add this so it acutally removes -1 from it because continue will skip all statements
        continue #Skip this specific iteration.
    if it==3:
        break
    #Will keep executing until the condition becomes false
    print(it);
    it=it-1;
print("End of While loop");

