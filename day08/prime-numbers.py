# Write your code below this line 👇
import math

def prime_checker(number):
    if number < 2:
        print("It's not a prime number.")
    else:
        # 소수는 제곱근까지만 확인하면 됨. 왜냐하면 약수가 존재한다면 제곱근을 기준으로 대칭으로 존재하기 때문
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                print("It's not a prime number.")
                return
        print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
