def main():
    print("Welcome to the tip calculator.")
    bill = float(input("What was the total bill? $"))
    people_count = int(input("How many people to split the bill? "))
    tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    tip_calculator(bill, people_count, tip_percent)


def tip_calculator(bill, people_count, tip_percent):
    # 1. Bill + Tip = Total amount
    bill_plus_tip = bill + (1 + (tip_percent / 100))

    # 2. Divide the total amount by head count
    each_pay = bill_plus_tip / people_count

    # 3. round {each_pay} to 2 decimal places
    each_pay_final = round(each_pay, 2)

    # 4. print out how much each person should pay
    print(f"Each person should pay: ${each_pay_final}")


main()
