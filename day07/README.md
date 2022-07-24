day 7 - Hangman

## Note

### List comprehension
string이나 다른 리스트로부터 리스트를 생성하는 간결하고 간편한 방법. List comprehension의 구조는 다음과 같다.
```
[expression for element in iterable if condition]
```

만약, 선택된 단어(chosen_word)의 글자 수만큼 underscore(_)를 추가한 리스트를 만들어야 한다면, 아래와 같이 두 가지 방법 중 하나를 선택할 수 있다.
1. 반복문을 통해 리스트 생성하기
```python
chosen_word = "Understanding"
display = []
for _ in chosen_word:
    display.append('_')
```

2. List comprehension을 이용해 리스트 생성하기
```python
chosen_word = "Understanding"
display = ['_' for letter in chosen_word]
```

