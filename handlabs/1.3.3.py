file = open("devices.txt","a+") 

while True:
    newItem = input("Lav en ny enhed: ")

    if newItem == "exit":
        print("All done!")
        exit()
    else:
        file.write(newItem + "\n")
        print("Du har nu tilføjet " + newItem + " til listen over enheder!")
