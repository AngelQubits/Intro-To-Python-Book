ibalance = round(float(input("What is your initial balance? ")), 2)
interest = (float(input("What is your yearly compounded interest rate? "))/100)
years = int(input("For how many total years will you be compounding? "))
balance = round((ibalance * ((1 + interest)**years)), 2)

print(f"Based on your initial balance of {ibalance}, "
      f"with a yearly compounded rate of {interest}, "
      f"and a total compounding period of {years} years, "
      "your final total balance will be: "
)

print(balance)