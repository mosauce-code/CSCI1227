#Coding the ATM again, using defined chunks of code, using try and except.

PIN = "3741" #Used random number generators for these numbers
balance = 10910


menuOptions = """Menu Options:
            1. Set a new PIN
            2. View Balance
            3. Withdraw
            4. Deposit
            5. Exit

        """

bye = "Thanks for using mosaucebank. Goodbye!"

# UPDATE - change your name in the welcome message at the terminal
print("Welcome to Moses' mosaucebank! \n")
def _main(PIN): #Main function, to check if the initial PIN is correct. 
  attempts = 3
  while attempts > 0:
    pin = input("Enter your PIN: ")
    if pin == PIN:
      print("Access granted. Welcome to mosaucebank!")
      attempts = 0
      return True
    else:
      print(f"Access denied. You have {attempts-1} attempt(s) left. ")
      attempts -= 1
      if attempts == 0:
        print("Too many incorrect attempts. Terminating program. ")
        break


def _change_pin(PIN): 
    attempts = 3
    while attempts >= 0:
        old_pin = input("Enter your current PIN: ")
        if old_pin == PIN:
          new_pin = input("Enter a new 4-digit PIN: ")

          while len(new_pin) != 4 or not new_pin.isdigit():
            print("Invalid PIN! Please enter a 4-digit number. ")
            new_pin = input("Enter a new 4-digit PIN: ")

          PIN = new_pin
          print("PIN changed successfully. ")  
          return PIN

        else:
          print(f"Incorrect PIN. You have {attempts-1} attempt(s) left. ")
          attempts -= 1
          if attempts == 0:
            print("Too many incorrect attempts. Redirecting to menu.  ")
            return PIN
            
            
            
           


def _view_balance(balance): 
    print(f"Your current balance is ${balance}.")

def _withdraw(balance): 
  try:
      withdraw_amount = int(input("How much would you like to withdraw?"))
      if withdraw_amount > balance:
        print("Insufficient funds.")
      else:
        balance -= withdraw_amount
        print(f"Your new balance is ${balance}.")
  except ValueError:
    print("Invalid input. Please enter a valid number.")
  return balance

def _deposit(balance):
  try:
    deposit_amount = int(input("How much would you like to deposit?"))
    balance += deposit_amount
    print(f"Your new balance is ${balance}.")
  except ValueError:
    print("Invalid input. Please enter a valid number.")
  return balance


if _main(PIN):
  while True:
    print(menuOptions)
    choice = input("Enter your choice: ")
    
    match choice:
      case "1":
        PIN = _change_pin(PIN)
      case "2":
        _view_balance(balance)
      case "3":
        balance = _withdraw(balance)
      case "4":
        balance = _deposit(balance)
      case "5":
        print(bye)
        break 
      case _:
        print("Invalid choice. Please try again.")

