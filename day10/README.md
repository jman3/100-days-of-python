day 10 - Functions with outputs

## Note
### 파이썬 함수를 dictionary의 value로 저장해두고 사용하기
- day10에서 계산기 구현 시 dictionary에 함수를 value로 저장해두고
- 입력값에 따라 서로 다른 함수를 호출해서 사용한 것을 보고 노트를 남김
- Store Function as dictionary value
- https://www.geeksforgeeks.org/python-store-function-as-dictionary-value/

```python
# 함수를 하나 정의하고
def print_key1():
    return "This is Gfg's value"
  
# 정의한 함수를 dictionary의 value 값으로 저장한다
test_dict = {"Gfg": print_key1, "is" : 5, "best" : 9}
  
# dictionary 출력 결과
print("The original dictionary is : " + str(test_dict))
  
# dictionary의 키 값을 통해 함수를 가져와서 ()를 추가해 함수를 호출하고 그 결과를 res에 저장 
res = test_dict['Gfg']()
  
# printing result 
print("The required call result : " + str(res)) 

# 이때, res = test_dict['Gfg'] 로 함수를 변수에 저장해두고
# res()로 함수를 호출할 수도 있다

# 이는 매개변수가 있는 함수의 경우에도 동일하다
# 예를 들어, print_key1 함수가 원래 2개의 매개변수를 가진다면, 
# res = test_dict['Gfg'] 로 함수를 저장해두고
# res(x, y) 와 같이 함수를 호출할 수 있게 되는 것이다
```


### flag
- 보통 2개의 값 중 하나를 가짐. 그 값은 주로 boolean(참 or 거짓) 타입.
- 어떤 일이 발생했는지 혹은 발생하지 않았는지 구분해주는 상태 값을 저장할 때 주로 사용
```python
end_of_game = True
is_instock = True

# 위와 같이 처음 True or False로 지정해두고 반복되는 작업을 수행하면서
# 특정 조건이 충족될때 True or False로 바뀌면서 반복문을 종료하는 등에 이용된다
```

### Docstring
클래스나 함수를 정의할 때 첫 줄에 작성하는 문자열로, 주로 클래스나 함수의 의도 및 기능에 대해 더 잘 이해할 수 있도록 내용을 적어두는 것이다
```python
def my_function():
    """docstring을 적는 곳"""
    return

# 이렇게 적은 docstring은 아래와 같이 함수 속성으로 접근할 수 있다
print(my_function.__doc__)
```