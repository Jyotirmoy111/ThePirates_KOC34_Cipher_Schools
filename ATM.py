import time as t
user_pin=9876

user_balance=100000
user_name="Mr.ABC"
print("Welcome to your bank account", user_name, end="\n")
choice=9

while(True):
    print("\t\t0. Logout and Exit")
    print("\t\t1. View Account Balance")
    print("\t\t2. Withdraw Cash")
    print("\t\t3. Deposit Cash")
    print("\t\t4. Change Pin")
    print("\t\t5. Return Card")
    
    choice= int(input("Enter number to proceed: "))
    print("\n")

    if choice == 0:
        print("Exiting..")
        t.sleep(2)
        print("You have been logged out. Thank you! :)\n\n")
        break

    elif choice in (1,2,3,4,5):
        num_of_tries=3
        while (num_of_tries!=0):
            input_pin = int(input("Please enter your 4-digit PIN: "))

            if input_pin == user_pin:
                print("Account authorized!\n\n")

                if choice == 1:
                    print("Your current balance is $", user_balance,end="\n\n")
                    break
                elif choice == 2:
                    print("Opening Cash Withdrawal..")
                    t.sleep(1)

                    while(True):
                        withdraw_amt= float(input("Enter the amount you wish to withdraw: $"))

                        if withdraw_amt>user_balance:
                            print("Can't withdraw $", withdraw_amt)
                            print("Please enter a lower amount!")
                            continue

                        else:
                            print("Withdrwing $", withdraw_amt)
                            confirm = input("Confirm- Y/N:")
                            if confirm in ('y','Y'):
                                user_balance =withdraw_amt
                                print("Amount withdraw $",withdraw_amt)
                                print("Remaining balance $", user_balance)
                                break

                            else:
                                print("Cancelling transaction")
                                t.sleep(1)
                                print("Transaction cancelled\n\n")
                                break
                        
                    break
                elif choice == 3:
                    print("Loading Cash Deposit..")
                    t.sleep(1)

                    deposit_amt = float(input("Enter the amount you wish to deposit: $"))
                    print("Deposit $", deposit_amt)  
                    confirm = input("Confirm: Y/N: ") 
                    if confirm in ("Y","y"):
                        user_balance+= deposit_amt
                        print("Amount deposit $", deposit_amt) 
                        print("Updated balance $",user_balance, end="\n\n") 
                    else:
                        print("Cancelling transaction ")
                        t.sleep(1)
                        print("Transaction cancelled!\n")
                    
                    break

                elif choice ==4:
                    print("Loading PIN change..")
                    t.sleep(1)

                    pin_new = int(input("Enter your new PIN:"))

                    print("Changing PIN to", pin_new)
                    confirm = input("Confirm? Y/N:")
                    if confirm in ('Y','y'):
                        user_pin = pin_new
                        print("PIN changed sucessful! \n")
                    
                    else:
                        print("Cancelling PIN change..")
                        t.sleep(1)

                        print("Process Cancelled!\n")

                    break

                else:
                    print("Loading Card Return..")
                    t.sleep(1)

                    print("Returning your ATM Card")
                    confirm= input("Confirm? Y/N:")
                    if confirm in ('Y','y'):
                        print("Card returned sucessful! \n")
                    
                    else:
                        print("Cancelling process..")
                        t.sleep(1)
                        print("Process Cancelled!\n")

                    break

            else:
                num_of_tries=-1
                print("PIN incorrect! Number of tries left -", num_of_tries, end=" \n")
            
        else:
            print("Existing..")
            t.sleep(1)

            print("You have logged out. Thank you!\n\n")
            break
    else:
        print("Invalid input!")
        print("\t\t0.Enter 0 to Logout and Exit!")
        continue
    
