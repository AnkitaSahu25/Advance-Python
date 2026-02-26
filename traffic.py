def red_light():
    print("RED Light - Stop")

def yellow_light():
    print("YELLOW Light - Wait")

def green_light():
    print("GREEN Light - Go")

while True:
    print("\nTraffic Light Simulation")
    print("1. Red Light")
    print("2. Yellow Light")
    print("3. Green Light")
    print("4. Automatic Cycle")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        red_light()
    elif choice == "2":
        yellow_light()
    elif choice == "3":
        green_light()
    elif choice == "4":
        red_light()
        yellow_light()
        green_light()
    elif choice == "5":
        print("Program Ended")
        break
    else:
        print("Invalid Choice")