# Write your code below this line ๐
import math

def prime_checker(number):
    if number < 2:
        print("It's not a prime number.")
    else:
        # ์์๋ ์ ๊ณฑ๊ทผ๊น์ง๋ง ํ์ธํ๋ฉด ๋จ. ์๋ํ๋ฉด ์ฝ์๊ฐ ์กด์ฌํ๋ค๋ฉด ์ ๊ณฑ๊ทผ์ ๊ธฐ์ค์ผ๋ก ๋์นญ์ผ๋ก ์กด์ฌํ๊ธฐ ๋๋ฌธ
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                print("It's not a prime number.")
                return
        print("It's a prime number.")


# Write your code above this line ๐

# Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
