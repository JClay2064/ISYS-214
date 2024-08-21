
# User enters annual income
citizen_income = float(input("Enter the annual income"))

# Tax brackets formulas  
ltb = round((citizen_income * 0.18) - 556.2) 
htb =  round((citizen_income - 85528) * 0.32 + 14839.2 ) 
no_tax = float(citizen_income * 0)

# Conditional Statements
if citizen_income < 85528 :
      print("Your tax = " , ltb ,"thalers")
elif citizen_income > 85528:
      print("Your tax =", htb , "thalers")
else:
      print("You have no taxes to pay at this time ")