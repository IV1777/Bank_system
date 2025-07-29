# Create a class to represent a bank account
class BankAccount:
    def __init__(self, name, number):
        self.account_holder = name      # Name of the account holder
        self.account_number = number    # Account number
        self.balance = 0                # Starting balance is zero

    # Deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} added successfully.")
        else:
            print("Amount must be greater than zero.")

    # Withdraw money from the account
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Invalid amount or insufficient balance.")

    # Show account details
    def show_details(self):
        print("\n--- Account Info ---")
        print("Name: ", self.account_holder)
        print("Account Number: ", self.account_number)
        print("Balance: ₹", self.balance)

# Main program
def main():
    print("Welcome to Simple Bank")

    name = input("Enter your name: ")
    number = input("Enter your account number: ")

    # Create an account object
    my_account = BankAccount(name, number)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Account Info")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amt = float(input("Enter amount to deposit: ₹"))
            my_account.deposit(amt)

        elif choice == '2':
            amt = float(input("Enter amount to withdraw: ₹"))
            my_account.withdraw(amt)

        elif choice == '3':
            my_account.show_details()

        elif choice == '4':
            print("Thank you for using Simple Bank!")
            break

        else:
            print("Invalid choice. Try again.")

# Run the main function
if __name__ == "__main__":
    main()
