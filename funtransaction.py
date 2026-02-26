def login():
    password = "123"
    count = 0
    
    while count < 3:
        p = input("Enter password: ")
        if p == password:
            print("Login successful")
            return True
        else:
            count += 1
            print("Wrong password")
    
    print("Access denied")
    return False

def deposit(balance, transactions):
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        transactions.append(f"Deposited: ${amount:.2f}")
        print(f"${amount:.2f} deposited successfully.")
    else:
        print("Invalid amount.")
    return balance

def withdraw(balance, transactions):
    amount = float(input("Enter withdrawal amount: "))
    if 0 < amount <= balance:
        balance -= amount
        transactions.append(f"Withdrew: ${amount:.2f}")
        print(f"${amount:.2f} withdrawn successfully.")
    else:
        print("Invalid amount.")
    return balance


def check_balance(balance):
    print(f"Current balance: ${balance:.2f}")

def view_transactions(transactions):
    if transactions:
        print("Transaction History:")
        for t in transactions:
            print(t)
    else:
        print("No transactions yet.")

def main():
    if not login():
        return
    
    balance = 0
    transactions = []
    
    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            balance = deposit(balance, transactions)
        elif choice == '2':
            balance = withdraw(balance, transactions)
        elif choice == '3':
            check_balance(balance)
        elif choice == '4':
            view_transactions(transactions)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice.")
main()
