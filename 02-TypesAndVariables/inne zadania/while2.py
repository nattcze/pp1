# loop that copies its input until the user types “done”, but
# treats lines that start with the hash character as lines not to be printed
while True :
    line = input("> .")
    if line[0] == "#":
        continue
    if line == "done" :
        break
    print(line)
    print("Done!")

