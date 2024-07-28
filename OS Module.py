import os

print("Do you want to see:\n1. Trees\n2. Flowers")
choice = input("Please choose a number from the list above: ")


if choice == "1":
    try:
        with open("trees.txt")as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
elif choice == "2":
    try:
        with open("flowers.txt") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")
else:
    print("Please choose '1' or '2': ")
 
