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