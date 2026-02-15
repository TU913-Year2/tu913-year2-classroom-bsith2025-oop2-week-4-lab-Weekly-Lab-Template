from myClass import Account

# This programme impirts the Account attribute and then implements it as
# two seperate instances, one for Jane Doe and one for John
# Enlarge the programme so that you can
# 1) print the details of each account set up
# 2) make a withdrawal from an account
# 3) update the balance of the account (ensure that you cant make an overdraft)

def main():
    acc1 = Account("Jame Doe", "Deposit", "A123456789", 345612.45)
    acc2 = Account("John Doe", "Current", "A123456790", 300.45)
    print(acc1.getName())
    print(acc2.getName())

main()
