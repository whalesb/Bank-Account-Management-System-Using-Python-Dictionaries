# Bank_details.py
Bank_database = dict()
def Add_newuser():
    while True:
        username = input("Username: ")
        account_name = input("Enter Account Name: ")
        account_number = int(input("Enter Account Number: "))
        balance = float(input("Enter Account Balance Amount: "))
        pin = int(input("Security Pin: "))

        user = dict()
        user['account_name'] = account_name
        user['account_number'] = account_number
        user['balance'] = balance
        user['pin'] = pin

        Bank_database[f'{username}'] = user
        print(Bank_database.items())
        res = input("Do you want to continue: (y) Yes, (n) No")
        if res.lower() == 'y':
            continue
        else:
            break
def view_database():
    for key, value in Bank_database.items():
        print("Username:", key)
        for x, y in value.items():
            print({x: y})
def withdraw(username):
    user = Bank_database[username]
    userpin = int(input("Enter your pin: "))
    if userpin == user['pin']:
        balance=user['balance']
        amount=int(input('how much do you want to withdraw'))
        if amount > balance:
            print('insufficient funds')
        else:
            balance = balance - amount
            print("your balance is:", balance)
            user['balance'] = balance
            print(user)
    else:
        print("Pin Incorrct")

def deposit(username):
    user = Bank_database[username]
    userpin = int(input("Enter your pin: "))
    if userpin ==user['pin']:
        balance=user["balance"]
        amount=int(input('how much do you want to deposite'))
        balance=balance+amount
        user["balance"] = balance
        print(user)
    
    else:
        print('incorrect pin pls try again')

