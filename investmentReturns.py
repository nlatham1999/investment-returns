import math

def main():
    yearlyamount = float(input("how much are you putting in each year? --> "))
    interest = float(input("what is the average anual return you are expecting? -->")) 
    years = int(input("how many years do you want to iterate over? --> "))
    interest = (interest *.01) +1
    count = 0
    total = 0
    while(count < years):
        total += yearlyamount
        total *= interest
        count += 1
    print("amount  put in: ", int(yearlyamount*years))
    print("total returned: ", int(total))
    print("amount earned: ", int(total-(yearlyamount*years)))
main()


