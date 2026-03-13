#1. Assign data to variables
principal = 172000
boe_rate = 2.25
fixed_margin = 1.49

#2.Calculate the total annual interest rate (as a percentage)
total_annual_rate = boe_rate + fixed_margin

#3.Compute the annual interest amount
#We divide by 100 to convert the percentage to a decimal 
annual_interest_amount = principal * (total_annual_rate / 100)

#4.Compute the monthly interest (spread equally over 12 months)
interest = annual_interest_amount / 12

#Output the result for verification
print(f"Monthly interest payable: ${interest:.2f}")