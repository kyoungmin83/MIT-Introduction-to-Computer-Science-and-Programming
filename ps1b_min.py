# Enter the input
outstanding_Balance = float(raw_input('Enter the outstanding balance on your credit card: '))
ann_Interest_Rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))

# Initialize variable
monthly_Interest_Rate = ann_Interest_Rate / 12.0
remain_Balance = outstanding_Balance 
min_Month_Payment = 10.0
num_Of_Month = 0

# Initialize num_of_Month and remain_Balance if they do not meet the sub-loop condition
while remain_Balance > 0:
    num_Of_Month = 0
    remain_Balance = outstanding_Balance 

    # Increment num_Of_Month and remain_Balance by min_Month_Payment
    while(remain_Balance > 0 and num_Of_Month < 12):
 
        interest = monthly_Interest_Rate * remain_Balance
        num_Of_Month += 1
        remain_Balance -= min_Month_Payment
        remain_Balance += interest

        # Print result if remain_Balance to paid off debt in year
        if remain_Balance <= 0:
            print 'RESULT'
            print 'Monthly payment to pay off debt in 1 year: ', min_Month_Payment
            print 'Number of months needed: ', num_Of_Month
            print 'Balance: ', round(remain_Balance, 2)

    # Increment min_Month_Payment by 10 if min_Month_Payment is not sufficient to payoff debt in year
    if remain_Balance > 0:
        min_Month_Payment += 10
    
        
        
        
    
    
    
