import random

class Account:
    def __init__(self, card_number, pin, balance):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

class ATM:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def validate_card(self, card_number):
        for account in self.accounts:
            if account.card_number == card_number:
                return account
        return None

    def generate_otp(self):
        generated_otp = random.randint(1000, 9999)
        print("Generated OTP:", generated_otp)
        return generated_otp
        #return random.randint(1000, 9999)

    def validate_otp(self, entered_otp, generated_otp):
        return entered_otp == generated_otp

    def perform_transaction(self, account):
        while True:
            print("1. Balance Inquiry")
            print("2. Cash Withdrawal")
            print("3. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Your balance is:", account.balance)
            elif choice == 2:
                amount = int(input("Enter the amount to withdraw: "))
                if account.withdraw(amount):
                    print("Withdrawal successful!")
                else:
                    print("Insufficient funds!")
            elif choice == 3:
                print("Thank you for using our ATM.")
                break
            else:
                print("Invalid choice. Please try again.")

# Demo
atm = ATM()

# Creating sample accounts
account1 = Account("1234567890123456", "1234", 10000)
account2 = Account("9876543210987654", "4321", 5000)

# Adding accounts to the ATM
atm.add_account(account1)
atm.add_account(account2)

# Simulating ATM functionality
card_number = input("Please insert your card: ")
account = atm.validate_card(card_number)

if account:
    pin = input("Enter your PIN: ")
    if pin == account.pin:
        generated_otp = atm.generate_otp()
        print("An OTP has been sent to your registered mobile number.")
        entered_otp = int(input("Enter the OTP: "))

        if atm.validate_otp(entered_otp, generated_otp):
            print("OTP verification successful!")
            atm.perform_transaction(account)
        else:
            print("Invalid OTP. Transaction aborted.")
    else:
        print("Incorrect PIN. Transaction aborted.")
else:
    print("Invalid card number. Transaction aborted.")
