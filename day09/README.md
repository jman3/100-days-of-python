day 9 - Dictionaries, Nesting and the Secret Auction

## Note

### lambda
- 함수의 형태를 더욱 짧게 쓸 수 있도록 해주는 문법
- 익명함수라고도 부름
```python
# 기본 구조
lambda 매개변수: 리턴값으로 사용할 식

# 활용 예시 1)
(lambda x: x + 5)(5)

# 활용 예시 2)
add = lambda x, y: x + y
print(add(3, 4))

# 함수의 정의 과정이 매우 짧아지고 간편해진다
```
- lambda를 if, else와 같이 쓰기
```python
# 기본 구조
lambda <arguments> : <조건이 참일때 리턴값> if <condition> else <조건이 거짓일때 리턴값>

# 활용 예시
# 1부터 100중 짝수는 제곱을 하고 홀수는 -1을 한 리스트를 구하라
a = list(map(lambda x: x ** 2 if x % 2 == 0 else x - 1, range(1, 101)))
print(a)
# [0, 4, 2, 16, 4, 36, 6, 64, 8, 100, 10, 144, 12, 196, 14, 256, 16, 324, 18, 400, 20, 484, 22, 576, 24, 676, 26, 784, 28, 900, 30, 1024, 32, 1156, 34, 1296, 36, 1444, 38, 1600, 40, 1764, 42, 1936, 44, 2116, 46, 2304, 48, 2500, 50, 27, 04, 52, 2916, 54, 3136, 56, 3364, 58, 3600, 60, 3844, 62, 4096, 64, 4356, 66, 4624, 68, 4900, 70, 5184, 72, 5476, 74, 5776, 76, 6084, 78, 6400, 80, 6724, 82, 7056, 84, 7396, 86, 7744, 88, 8100, 90, 8464, 92, 8836, 94, 9216, 96, 9604, 98, 10000]
```



### lambda와 자주 쓰이는 함수 1) map()
```python
# 기본 구조
map(function, iterable)
```
- 여기서 function은 함수, iterable은 iterable한 객체(리스트, 튜플 등)를 의미한다
- 즉, 특정 함수 function을 iterable의 각 원소에 적용한 결과를 map 객체로 돌려주는 함수가 map()이다
```python
# 활용 예시 1)
def add(x):
    return x + 10

a = [1, 2, 3, 4]
print(list(map(add, a)))
# [11, 12, 13, 14]

# 활용 예시 2) map 함수의 인자로 2개 이상의 iterable을 줄 수도 있다
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

my_function = lambda a, b: a + b
result = map(my_function, list1, list2)
# 이렇게 하면 result에는 map object가 담기게 된다. 

# 이걸 리스트로 바꾸려면 list()안에 map object를 넣어주면 된다.
print(list(result))
```

### lambda와 자주 쓰이는 함수 2) filter()
```python
# 기본 구조
filter(function, iterable)
```
- filter는 iterable의 각 요소가 function를 활용해 참인지 거짓인지 판별할때 사용한다
- function에 의해 참이라고 판정된 요소들만 남긴 iterator를 리턴해준다

```python
# 활용 예시 1
def vowel_checker(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter in vowels:
        return True
    else:
        return False

phrase = "Hello world! I just started Python"
letters_in_phrase = list(phrase.lower())

vowels_in_phrase = filter(vowel_checker, letters_in_phrase)
# 이때 filter된 결과는 filter 객체라서 list 같은걸로 만들어주고 싶으면 list()에 넣으면 됨
# loop에서 쓰려면 그냥 아래처럼 써도 무방함
for vowel in vowels_in_phrase:
    print('This vowel is included: ', vowel)
```