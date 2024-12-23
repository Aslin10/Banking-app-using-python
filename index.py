class Bank:
    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount

    def log_transaction(self, transaction_string):
        with open("transaction.txt", "a") as file:
            file.write(f"{transaction_string}\n")

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0

        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.log_transaction(f"Withdrew amount: {amount}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount entered for withdrawal.")

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0

        if amount > 0:
            self.balance += amount
            self.log_transaction(f"Deposited amount: {amount}")
        else:
            print("Invalid amount entered for deposit.")

# Initialize the account with a balance of 50.50
account = Bank(50.50)

while True:
    try:
        action = input("What kind of action do you want to take? (withdrawal/deposit/exit): ").strip().lower()
    except KeyboardInterrupt:
        print("\nLeaving the ATM. Goodbye!")
        break

    if action == "exit":
        print("Leaving the ATM. Goodbye!")
        break

    if action in ["withdrawal", "deposit"]:
        try:
            amount = input("Enter the amount: ").strip()
            if action == "withdrawal":
                account.withdrawal(amount)
            elif action == "deposit":
                account.deposit(amount)
        except Exception as e:
            print("An error occurred:", e)
    else:
        print("Invalid action. Please choose either 'withdrawal', 'deposit', or 'exit'.")

    print(f"Your current balance is: {account.balance:.2f}")
