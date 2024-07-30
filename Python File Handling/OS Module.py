import os

path = input("Enter the directory you want to read: ")
try:
    with open(path, "r") as file:
        for line in file:
            print(line)
except Exception as e:
    print(f"An error occurred: {e}")