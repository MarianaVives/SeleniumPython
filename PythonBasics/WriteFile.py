#Optimized way to open file = w for write mode ; r for read mode
with open("text.txt", "r") as reader:
    content = reader.readlines(); #all lines stored in a list
    with open("text.txt", "w") as writer:
        for line in reversed(content): #Write in reversed order back to the file
            writer.write(line)