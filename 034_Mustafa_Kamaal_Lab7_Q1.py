# Name: Mohd Mustafa Kamaal
# Roll no: 34
# Enrl no: A180571
while 1:
    elements = input("Enter the integers in the file or enter '101' to exit :\n")
    try:
        elements = int(elements)
        if elements != 101:
            file = open("integers.txt","a")
            file.write(str(elements))
            file.write("\n")
            file.close()
            continue
        else:
            file.close()
            break
    except ValueError:
        print("Enter numbers only.")
        #file.close()
        continue   
f = open("integers.txt","r")
while True:
    line = f.readline()
    try:
        line = int(line)
        if line%2 == 0:
            f1 = open("even.txt", "a")
            f1.write(str(line))
            f1.write("\n")
            f1.close()
        else:
            f2 = open("odd.txt","a")
            f2.write(str(line))
            f2.write("\n")
            f2.close()
        if not line:
            break
    except ValueError:
        break
print(f1.name)
print(f2.name)
f.close()
