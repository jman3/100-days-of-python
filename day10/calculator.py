from art import logo
from replit import clear


def calc(first_num):
    operator = input("+\n-\n*\n/\nPick an operation: ").lower()
    second_num = float(input("What's the next number?: "))
    if operator == '+':
        result = first_num + second_num
    elif operator == '-':
        result = first_num - second_num
    elif operator == "*":
        result = first_num * second_num
    elif operator == "/":
        result = first_num / second_num
    print(f"{first_num} {operator} {second_num} = {result}")
    return result


def main():
    print(logo)

    starting_number = float(input("What's the first number?: "))
    calc_result = calc(starting_number)
    continue_cal = "y"
    while True:
        continue_cal = input(f"Type 'y' to continue calculating with {calc_result}, or type 'n' to start a new calculation: ").lower()
        if continue_cal == "y":
            calc_result = calc(calc_result)
        else:
            # 새로운 연산을 시작하고 싶다면 화면을 초기화하고 다시 main 함수를 처음부터 실행한다
            clear()
            main()

main()