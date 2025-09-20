import time
import os
while True:
    print("=== Welcome To Our World ===")
    print("1. Hollywood movie")
    print("2. Bollywood movie")
    print("3. South movie")
    print("4. Exit")

    choice=input('Enter (1-4): ').split()

    valid = {"1", "2", "3", "4"}

    if not set(choice).issubset(valid):
        print("\nInvalid Input!")
        print("Please check Your Input")
        print("Refreshing page in 5s.....")
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        continue

    if "1" in choice:
        print("Welcome to Hollywood Movie World")
       
        
    if "2" in choice:
        print("Welcome to BollywoodMovie World")
        
        
    if "3" in choice:
        print("Welcome to South Movie World")
       
        
    if "4" in choice:
        print("Thank You for Exploring Our World")
        break
       
    time.sleep(1)
    os.system("cls" if os.name =="nt" else "clear")
        