# Description: Program introducing report generation, a payment due report modified from class
#              example with addition of return date functions and phone number accumulator.
#              Calls for data from Customers.dat file.
# Author: MB, DCE
# Date(s): July 16, 2024
 
 
# Define required libraries.
import datetime

 
 
# Define program constants.
CUR_DATE = datetime.datetime.now()
yr_now = CUR_DATE.year
mth_now = CUR_DATE.month
day_now = CUR_DATE.day
MIN_PAY_RATE = .10
 
# Define program functions.

def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##. A MB Original from his Format Values file.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def DueDate1():
    #Returns Next Payment Date for balances under $200.
    nxt_pay = CUR_DATE + datetime.timedelta(days=14)
    nxt_pay_dsp = nxt_pay.strftime("%d-%b-%y")
    return nxt_pay_dsp

def DueDate2():
    #Returns Next Payment Date for balances over $200 and under Credit Limit.
    nxt_mth = mth_now + 1
    yr_now = 2024
    if mth_now == 12:
        nxt_mth = 1
        yr_now += 1
    if day_now < 25:
        nxt_pay = datetime.datetime(yr_now, nxt_mth, 1)
        nxt_pay_dsp = nxt_pay.strftime("%d-%b-%y")
    else:
        nxt_mth +=1
        if nxt_mth == 13:
            nxt_mth = 1
            yr_now += 1
        nxt_pay = datetime.datetime(yr_now, nxt_mth, 1)
        nxt_pay_dsp = nxt_pay.strftime("%d-%b-%y")
    return nxt_pay_dsp
 
def DueDate3():
    #Returns Next Payment Date for balances over Credit Limit.
    nxt_pay = CUR_DATE + datetime.timedelta(days = 60)
    nxt_pay_dsp = nxt_pay.strftime("%d-%b-%y")
    return nxt_pay_dsp
 
# Main report processing starts here.
 
 
# Generate report headings.
print()
print("                             WIDGITS INCORPORATED")
print()
CurDateDsp = datetime.datetime.strftime(CUR_DATE, "%d-%m-%Y")
print(f"                    PAYMENT DUE REPORT AS OF {CurDateDsp:<10s}")
print()
print(" ACCOUNT       CUSTOMER        BALANCE     MINIMUM    NEXT DUE     PHONE")
print(" NUMBER          NAME            DUE       PAYMENT      DATE       NUMBER")
print(" ========================================================================")
 
# Initialize counters and accumulators.
CustCtr = 0
BalDueAcc = 0
MinPayAcc = 0
OverLimAcc = 0
 
# Open the data file.
f = open("Customers.dat", "r")
 
# Process each line (record) in the file in a loop.
for CustRecord in f:
   
    # Read the record.  Grab values from the list.
     # The following line reads the first record in the file and creates a list.
    CustLst = CustRecord.split(",")
 
    # Now grab the values from the list and assign to variables.
    # You may not need all the fields.
    CustNum = CustLst[0].strip()
    CustName = CustLst[1].strip()
    BalDue = CustLst[5].strip() # Read from the file as a string.
    BalDue = float(BalDue)
    CredLim = CustLst[6].strip()
    CredLim = float(CredLim)
    cust_phone = CustLst[4].strip()
    
   
 
    # Perform required calculations.
    CredRem = CredLim - BalDue
    if BalDue <= CredLim:
        MinPay = BalDue * MIN_PAY_RATE
    else:
        MinPay = (BalDue * MIN_PAY_RATE) + (BalDue - CredLim)

    if BalDue < 200.00:
        nxt_due_date = DueDate1()
    elif BalDue < CredLim:
        nxt_due_date = DueDate2()
    elif BalDue > CredLim:
        nxt_due_date = DueDate3()
    
  
    
   
 
    # Display the detail line.
    if BalDue <= CredLim:
        print(f" {CustNum:<5s}     {CustName:<16s}  {FDollar2(BalDue):>9s}   {FDollar2(MinPay):>9s}   {nxt_due_date}")   
    else:
        print(f" {CustNum:<5s}     {CustName:<16s}  {FDollar2(BalDue):>9s}   {FDollar2(MinPay):>9s}   {nxt_due_date}   {cust_phone}")
        OverLimAcc +=1
    # Update counters and accumulators.
    CustCtr += 1
    BalDueAcc += BalDue
    MinPayAcc += MinPay
 
 
# Close the file.
f.close()
 
# Print summary data - counters and accumulators.
print(" ========================================================================")
print(f" Customers listed: {CustCtr:>3d}      {FDollar2(BalDueAcc):>10s}  {FDollar2(MinPayAcc):>10s}         Over Limit:  {OverLimAcc}")
print()
print("                         END OF LISTING")
