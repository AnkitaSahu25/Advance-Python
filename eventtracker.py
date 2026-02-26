# Event Tracker using Set
entered_set = set()
requested_set = set()
n = int(input("Enter number of invited students: "))
for i in range(n):
    name = input(f"Enter invited student {i+1} name: ")
    requested_set.add(name)
m = int(input("\nEnter number of students who entered the event: "))
for i in range(m):
    name = input(f"Enter entered student {i+1} name: ")
    if name in entered_set:
        print("Duplicate name rejected!")
    else:
        entered_set.add(name)
not_entered = requested_set - entered_set
print("\nEntered Students:", entered_set)
print("Not Entered Students:", not_entered)
print("Total people in event:", len(entered_set))
