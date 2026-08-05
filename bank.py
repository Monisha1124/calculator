def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        return "Insufficient funds"
    return balance - amount

def add_interest(balance, rate):
    return balance + (balance * rate / 100)

if __name__ == "__main__":
    balance = 1000
    balance = deposit(balance, 500)
    print("Balance:", balance)