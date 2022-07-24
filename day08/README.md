day 8 - Function Parameters & Caesar Cipher

## Note

### Positional arguments vs Keyword arguments
1. positional arguments - 함수에 정의된 매개변수 위치에 맞게 인자를 입력하는 방식
3. keyword arguments - 함수에 정의된 매개변수 이름에 직접 인자를 할당하는 방식. 함수 정의 시에 설정했던 매개변수의 순서와 전달하는 인자의 순서가 동일하지 않아도 괜찮음

```python
def my_function(a, b, c):
# do this with a
# then do this with b
# finally do this with c

my_function(1, 2, 3) # positional arguments
my_function(a = 1, b = 2, c = 3) # keyword arguments
```


