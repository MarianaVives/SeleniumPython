with open("text.txt") as reader:
    count= sum(1 for line in reader)
    print(f"Total number of lines: {count}")
