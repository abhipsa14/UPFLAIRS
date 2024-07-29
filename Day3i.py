name=input("Enter your name:")
print("Hello",name)
message="""
How can I help you?
Type 1: Check your Balance.
Type 2: Deposit
Type 3: Withdrawal
"""
print(message)
task= int(input("Choose an option:"))
available_amount= 5000
# print(task)
# print(type(task))

if(task>=1 and task<=3):
    print("Welcome to your virtual bank.")
    if task==1:                                       #'...' repalcement of pass keyword
        #check balance
        print("Your available balance is:",available_amount
              )
        
    elif task==2:
        #deposit
        deposit_amount=int(input("enter your deposit amount:"))
        if(deposit_amount>=500):
            #deposit_task
            available_amount+=deposit_amount
            print("You have successfully deposited your money.")
            print("Your available balance is:",available_amount)
        else:
            print("Deposit at least 500 Rupees!")
    else:
        #withdrawal
        withdrawal_amount=int(input("Enter a withdrawal amount:"))
        if(withdrawal_amount<available_amount):
            available_amount-=withdrawal_amount
            print("Your available balance is:",available_amount)
        else:
            print("Not available amount.")

else:
    print("Please enter valid option.")


