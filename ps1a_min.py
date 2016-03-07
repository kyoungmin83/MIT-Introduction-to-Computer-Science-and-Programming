
# Enter the inputs
outstanding_balance = float(raw_input('Enter the outstanding balance on your credit card: '))
ann_IR = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
min_Mon_rate = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))

# Initialize variables
remain_Balance = outstanding_balance
monthly_interest_Paid = ann_IR / 12.0
min_Mon_pay = min_Mon_rate * remain_Balance
principal_Paid = min_Mon_pay - (monthly_interest_Paid * remain_Balance)
total_amount = 0.0

for month in range(1, 13):
    min_Mon_pay = round(min_Mon_rate * remain_Balance ,2)
    interest_Paid = round(monthly_interest_Paid * remain_Balance, 2)
    principal_Paid = round(min_Mon_pay - interest_Paid, 2)

    print 'Month: ' , month
    print 'Minimum monthly payment: ' +'$'+ str(min_Mon_pay)
    print 'Principal paid: ' + '$' + str(principal_Paid)
    remain_Balance -= principal_Paid
    print 'Remaining balance: ' + '$' + str(remain_Balance)
    total_amount += min_Mon_pay
    
print 'RESULT'
print 'Total amount paid: '+ '$' + str(total_amount)
print 'Remaining balance: ' + '$' + str(remain_Balance)

 



