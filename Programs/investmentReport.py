amount = float(input("Enter the investment amount : "))
years = int(input("Enter the no.of years : "))
rate = int(input("Enter the rate as a % : "))
total_interest = 0.0
print("Year\t\tStarting Balance\t\tInterest\t\tEnding Balance")
for i in range(1,years+1):
    interest = (amount/100)*rate
    balance = amount + interest
    print(f"{i}\t\t{amount:12.2f}\t\t    {interest:10.2f}\t\t  {balance:14.2f}")
    amount = balance
    total_interest += interest
print("Ending Balance : $",balance)
print("Total interest earned : $",total_interest)
    
