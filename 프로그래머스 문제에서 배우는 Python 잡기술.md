# 프로그래머스 문제에서 배우는 Python 잡기술

하나하나 실력을 늘려나갑시다.



### 1. any

```python
if any(a[0] < p[0] for p in new_priorities):
    new_priorities.append(a)
else:
```

조건문 형식으로 사용한다. 하나라도 조건을 만족하지 않는게 있다면!!!

any가 있으면 every도 있겠다 근데...?



### 2. 문자열.ljust, .rjust

```python
str_number = str_number.ljust(4, '-')
['3---', '30--', '34--', '5---', '9---']
str_number = str_number.rjust(4, '-')
['---3', '--30', '--34', '---5', '---9']
```

나름 재밌는!!! 채우는거다. 뭔지는 알겠지?



### 3. 2차원 set 배열 만들기

```python
front = [ set() for _ in range(n + 1) ] # O
back = [ set() ] * (n + 1)			   # X
```

위처럼 하면 맞고, 아래처럼 하면 틀림



### 4. Python and 선후관계

```python
a = [1,1]

if a[0] == 1 and a[1] == 2 and a[135097] == 1:
    print('정답')
else:
    print('오류안뜸')
```

지금까지 몰랐는데, 앞의 조건이 성립하지 않으면 뒤까지 가지도 않는다.

이걸 이제 알았네...ㅋㅋ

