# Enter the inputs

balance = float(raw_input('Enter the outstanding balance on your credit card: '))
annual_IR = float(raw_input('Enter the annual credit card interest rate as a decimal: '))

# Initialize varialbes

lower_Bound = balance / 12.0
upper_Bound = (balance*(1 + (annual_IR / 12.0))**12.0) / 12.0

remain_Balance = balance
min_Month_Payment = (lower_Bound + upper_Bound) / 2.0
numOfMonth = 0

# Use bisection search until the search space is sufficiently small
while (upper_Bound - lower_Bound > 0.0001):
    
    # Recompute numOfMonth, remain_Balance and min_Month_Payment
    numOfMonth = 0
    remain_Balance = balance
    min_Month_Payment = (lower_Bound + upper_Bound) / 2.0

    # Inrement numOfMonth and remain_Balance
    while (remain_Balance > 0 and numOfMonth < 12):
        interest = annual_IR / 12.0 * remain_Balance
        numOfMonth += 1
 
        remain_Balance -= min_Month_Payment
        remain_Balance += interest

    # Adjust min_Month_Payment in case that too much paid    
    if remain_Balance < - 0.01:
         upper_Bound = min_Month_Payment

    # Adjust min_Month_Payment in case that too little paid
    elif remain_Balance > 0:
         lower_Bound = min_Month_Payment
    
    # Print results if remain_Balance is paid off in year
    if remain_Balance <= 0 and remain_Balance > -0.01:
        
        print 'RESULT'
        print 'Monthly payment to payoff debt in 1 year: ', round(min_Month_Payment, 2)
        print 'Number of months needed: ', numOfMonth
        print 'Balance: ', round(remain_Balance, 2)
        break

        
                
                

        
    


    
