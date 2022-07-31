def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(y, m):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 입력된 연도와 월이 leap year 이면서 2월인 경우만 29, 나머지는 모두 month_days에서 월별로 정해진 일수 return
    if is_leap(y) and m == 2:
        return 29
    else:
        return month_days[m-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)